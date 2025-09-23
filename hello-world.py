from agents import Agent, Runner
import os
import openai

# For using OpenAI to generate query embedding
from dotenv import load_dotenv
load_dotenv()
open_api_key = os.getenv("OPENAI_API_KEY")
openai_client = openai.OpenAI(api_key=open_api_key)


agent = Agent(name="assistant", instructions="You are a helpful assistant.")

result = Runner.run_sync(agent, "What is the capital of France?")

print(result.final_output)