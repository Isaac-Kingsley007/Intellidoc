# import openai

# openai.api_key = "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"

# def summarize_text(text):
#     """Sends text to OpenAI for summarization."""
#     response = openai.Completion.create(
#         model="gpt-4",
#         messages=[{"role": "user", "content": f"Summarize this: {text}"}],
#         max_tokens=150
#     )
#     return response["choices"][0]["text"].strip()

# if __name__ == '__main__':
#     print(summarize_text("HI How are you you need not summarize this this is just testing"))

#open router config

# from openai import OpenAI

# client = OpenAI(
#   base_url="https://openrouter.ai/api/v1",
#   api_key="<OPENROUTER_API_KEY>",
# )

# completion = client.chat.completions.create(
#   extra_headers={
#     "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
#     "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
#   },
#   extra_body={},
#   model="deepseek/deepseek-r1:free",
#   messages=[
#     {
#       "role": "user",
#       "content": "What is the meaning of life?"
#     }
#   ]
# )
# print(completion.choices[0].message.content)

#Github marketplace No money mame

# from openai import OpenAI

# endpoint = "https://models.inference.ai.azure.com"
# model_name = "DeepSeek-R1"
# token = "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"

# def summarize_text(text):
#     return text

# def talkWithBot(prompt):

#     client = OpenAI(
#         base_url=endpoint,
#         api_key=token,
#     )

#     completion = client.chat.completions.create(
#         extra_body={},
#         model=model_name,
#         messages=[
#             {
#                 "role": "user",
#                 "content": prompt
#             }
#         ]
#     )
#     print(completion.choices[0].message.content)
#     return completion.choices[0].message.content

#actaul work

from openai import OpenAI

endpoint = "https://openrouter.ai/api/v1"
model_name = "deepseek/deepseek-r1:free"
token = "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"

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
    
    return talkWithBot("Provide a structured summary of this document with the following sections: Introduction, Key Findings, and Conclusion. Ensure the summary is easy to understand, using clear and simple language while preserving the core meaning of the document. : \n" + text)

if __name__ == "__main__":
    from file_handling import extract_text
    print(summarize_text(extract_text("uploads\\Assignment - II Isaac Kingsley D.pdf")))