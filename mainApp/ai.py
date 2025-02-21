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

from openai import OpenAI

endpoint = "https://models.inference.ai.azure.com"
model_name = "DeepSeek-R1"
token = "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"

def summarize_text(text):
    return text

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