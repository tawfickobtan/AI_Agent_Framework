from tool import Tool
from agent import Agent
from model import Model
from dotenv import load_dotenv
import os

load_dotenv()

@Tool.toolthis(
    name="add_numbers",
    description="Adds two numbers together.",
    input_schema={
        "type": "object",
        "properties": {
            "a": {"type": "integer", "description": "The first number."},
            "b": {"type": "integer", "description": "The second number."}
        },
        "required": ["a", "b"]
    }
)
def add_numbers(a: int, b: int) -> int:
    return a + b

tools = [add_numbers]
print(add_numbers.get_schema())

#------------------------------------

model = Model(model_name="openai/gpt-oss-20b", base_url="https://api.groq.com/openai/v1", api_key=os.getenv("GROQ_API_KEY"))
print(model.complete([{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What is 5 + 7?"}]))

#------------------------------------

agent = Agent(name = "adding agent", 
              description = "adds", 
              model=model, 
              tools=tools,
              system_prompt="You are a helpful assistant that can add numbers. When asked to add dont add yourself, use the add_numbers tool."
              )
agent.add_message(role = "user", content = "What is 5 + 7?")
print(agent.step())