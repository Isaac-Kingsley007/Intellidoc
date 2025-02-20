import openai

openai.api_key = "your-openai-api-key"

def summarize_text(text):
    """Sends text to OpenAI for summarization."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Summarize this: {text}"}],
        max_tokens=150
    )
    return response["choices"][0]["message"]["content"].strip()