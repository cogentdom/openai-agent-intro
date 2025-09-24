#!/usr/bin/env python3.9
# Note: This code requires Python 3.9+ and the openai-agents package
# Install with: python3.9 -m pip install openai-agents python-dotenv eval_type_backport

from agents import Agent, Runner
import os
import openai

# For using OpenAI to generate query embedding
from dotenv import load_dotenv
load_dotenv()
# open_api_key = os.getenv("OPENAI_API_KEY")
# openai_client = openai.OpenAI(api_key=open_api_key)


agent = Agent(name="assistant", instructions="You are a helpful assistant.")

result = Runner.run_sync(agent, "What is the capital of France?")

print(result.final_output)