from openai import OpenAI

endpoint = "https://models.inference.ai.azure.com"
model_name = "DeepSeek-R1"
token = "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"

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
      "content": "What is the meaning of life?"
    }
  ]
)
print(completion.choices[0].message.content)
completion.choices[0].message.content