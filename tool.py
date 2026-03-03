from typing import Callable

class Tool:
    def __init__(self, name: str, description: str, input_schema: dict, func: Callable):
        self.name = name
        self.description = description
        self.input_schema = input_schema
        self.func = func
        
    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
    
    def get_schema(self):
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.input_schema
            }
        }
    
    def toolthis(name: str, description: str, input_schema: dict):
        def decorator(func: Callable):
            return Tool(name, description, input_schema, func)
        return decorator
    
    def __repr__(self):
        return f"Tool:\nname={self.name}\ndescription={self.description}"