from scriptflow import Agent

agent = Agent()

agent.observe("screen.png")
agent.plan("open browser")
agent.execute()
