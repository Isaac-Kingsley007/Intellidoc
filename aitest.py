from openai import OpenAI

API_KEY = "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"

client = OpenAI(api_key=API_KEY)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)