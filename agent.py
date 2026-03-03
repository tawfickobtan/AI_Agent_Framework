from model import Model
from tool import Tool

class Agent:
    def __init__(self, name: str, description: str, model: Model, tools: list[Tool], system_prompt: str):
        self.name = name
        self.description = description
        self.model = model

        self.tools = tools
        self.tool_feed = []
        self.function_registry = {}
        for tool in self.tools:
            if tool.name in self.function_registry:
                print(tool.name + " tool found multiple times")
                continue
            self.function_registry[tool.name] = tool.func
            self.tool_feed.append(tool.get_schema())

        self.system_prompt = system_prompt or "You are a helpful assistant."

        self.messages = [{"role": "system", "content": self.system_prompt}]

    def add_message(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})

    def step(self) -> dict:
        response = self.model.complete(messages=self.messages, tools=self.tool_feed)
        return response