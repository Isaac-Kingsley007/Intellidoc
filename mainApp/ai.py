from openai import OpenAI
from api_config import *

endpoint = BASE_URL
model_name = GEMINI_2_0_FLASH
token = API_KEY

prompt1 = "Provide a structured summary of this document with the following sections: Introduction, Key Findings, and Conclusion. Ensure the summary is easy to understand, using clear and simple language while preserving the core meaning of the document. : \n"
prompt2 = "Provide a Summary of this document in Clear and Simple simple language while preserving the core meaning of the document. : \n"

def talkWithBot(prompt):

    client = OpenAI(
        base_url=endpoint,
        api_key=token,
    )

    completion = client.chat.completions.create(
        extra_body={},
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

def summarize_text(text):
    
    return talkWithBot(prompt2 + text)
