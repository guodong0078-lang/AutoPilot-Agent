# tests/test_agent.py
from autopilot_agent.agent import AutoPilotAgent
from plugins.example_plugin import example_tool

def test_agent_runs():
    agent = AutoPilotAgent()
    agent.register_tool(example_tool)
    out = agent.run_task("Find resources about python.")
    assert "results" in out
    assert isinstance(out["results"], list)
    assert len(out["results"]) >= 1
