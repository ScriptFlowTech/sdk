from scriptflow import Agent


def test_agent_flow():
    agent = Agent()
    agent.observe("test")
    agent.plan("goal")
    assert agent.execute() is True
