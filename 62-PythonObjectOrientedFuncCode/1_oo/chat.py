from typing import Callable

from openai import OpenAI

# Models
GPT3_TURBO = "gpt-3.5-turbo"
GPT4 = "gpt-4o"

type ChatFn = Callable[[str], str] # A function that takes a string and returns a string

# factory function that uses closures to create a configured chat function
def chatter(api_key: str, model: str = GPT4) -> ChatFn:
    ai_client = OpenAI(api_key=api_key) # Creates OpenAI client once - stored in the closure's scope

    def send_chat_request(query: str) -> str: # Inner function that will be returned. It "remembers" ai_client and model via closure.
        response = ai_client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": query},
            ],
        )
        chat_result = response.choices[0].message.content
        if not chat_result:
            raise ValueError("No response from the chat model.")
        return chat_result

    return send_chat_request
