from openai import OpenAI


class GPT:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)

    def get_response(self, model="gpt-4o-mini", worker="You are a helpful assistant.", prompt="Tell me a joke."):
        completion = self.client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": worker
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        #print(completion)
        return completion.choices[0].message.content

