import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class Model:
    def __init__(self, model_name, base_url, api_key):
        self.model_name = model_name
        self.base_url = base_url
        self.api_key = api_key
        self.client = OpenAI(
            base_url=self.base_url,
            api_key=self.api_key,
        )

    def complete(self, messages, tools = []):
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )
        return response.choices[0].message

