import requests
import json
import time

# User inputs
filename = "uploads/Instructions.pdf"  # Change this to your actual PDF file name
from_format = "pdf"
to_format = "doc"

# Step 1: Request a Job from FreeConvert
body = {
    "tasks": {
        "import": {"operation": "import/upload"},
        "convert": {
            "operation": "convert",
            "input": "import",
            "input_format": from_format,
            "output_format": to_format,
            "options": {
                "bookmarks": "word",
                "create_pdfa": True,  
                "optimize_for": "screen",  
                "page_range_from": 1,  
                "page_range_to": 2,  
                "password_document": "sample_password"
            },
        }
    }
}

headers = {"Content-Type": "application/json"}

response = requests.post("https://api.freeconvert.com/v1/process/jobs", data=json.dumps(body), headers=headers)

if response.status_code != 200:
    print("Error:", response.text)
    exit()
else:
    print("Sucesses : ", response.text)

job_data = response.json()
job_id = job_data.get("id")

if not job_id:
    print("Error: No job ID received from API.")
    exit()

# Step 2: Extract Upload URL
import_task = job_data.get("tasks", [{}])[0]  # Get the import task
upload_url = import_task.get("result", {}).get("form", {}).get("url")
upload_params = import_task.get("result", {}).get("form", {}).get("parameters", {})

if not upload_url:
    print("Error: No upload URL received.")
    exit()

# Step 3: Upload the File to FreeConvert
with open(filename, "rb") as file:
    files = {"file": file}
    upload_response = requests.post(upload_url, files=files, data=upload_params)

if upload_response.status_code != 200:
    print("Error: File upload failed:", upload_response.text)
    exit()

print("File uploaded successfully. Waiting for conversion...")

# Step 4: Poll Job Status Until Conversion is Complete
job_url = f"https://api.freeconvert.com/v1/process/jobs/{job_id}"

while True:
    time.sleep(5)  # Wait before polling again
    job_status_response = requests.get(job_url, headers=headers)

    if job_status_response.status_code != 200:
        print("Error checking job status:", job_status_response.text)
        exit()

    job_status = job_status_response.json()
    status = job_status.get("status")

    if status == "completed":
        break  # Job is finished, exit loop
    elif status in ["failed", "error"]:
        print("Error: Conversion job failed.")
        exit()

print("Conversion completed!")

# Step 5: Extract the Download URL
download_url = None
for task in job_status.get("tasks", []):
    if task.get("operation") == "convert" and "output" in task.get("result", {}):
        download_url = task["result"]["output"][0]["url"]
        break

if not download_url:
    print("Error: No file download URL found.")
    exit()

print(f"Download your converted DOC file here: {download_url}")
