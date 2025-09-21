from agents import Agent, Runner

agent = Agent(name="assistant", instructions="You are a helpful assistant.")

result = Runner.run_sync(agent, "What is the capital of France?")

print(result.final_output)