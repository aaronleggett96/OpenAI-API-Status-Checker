import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def ping_model(model, messages=None, prompt=None, temperature=None):
    try:
        if model in ["gpt-4", "gpt-3.5-turbo"]:
            if messages is None:
                messages = [{"role": "user", "content": "A"}]
            completion = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                max_tokens=1,
            )
        elif model == "text-davinci-003":
            if prompt is None:
                prompt = "A"
            completion = openai.Completion.create(
                model=model,
                prompt=prompt,
                max_tokens=1,
                temperature=temperature,
            )
        else:
            return False
        return True
    except Exception:
        return False
