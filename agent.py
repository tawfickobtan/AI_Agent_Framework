from model import Model
from tool import Tool
import json

class Agent:
    def __init__(self, name: str, description: str, model: Model, tools: list[Tool], system_prompt: str):
        self.name = name
        self.description = description
        self.model = model
        
        self.tools = tools
        self.tool_feed = []
        self.function_registry = {}
        self.id_map = {}
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
        self.messages.append(response)
        if response.tool_calls:
            for tool_call in response.tool_calls:
                tool_response = self.handle_tool_call(tool_call)
                self.messages.append(tool_response)
                return {"type": "tool_call", "tool_name": tool_call.function.name, "tool_arguments": tool_call.function.arguments, "tool_response": tool_response.content}
        else:
            return {"type": "message", "content": response.content}
        return response

    def handle_tool_call(self, tool_call) -> str:
        name = tool_call.function.name
        args = tool_call.function.arguments
        id = tool_call.id
        if id not in self.id_map:
            self.id_map[id] = name
        if isinstance(args, str):
                args = json.loads(args)
        result = ""
        try:
            result = str(self.function_registry[name](**args))
        except Exception as e:
            result = "Error occured while executing the tool: " + str(e)
        return {"role": "tool", "tool_call_id": id, "content": result}