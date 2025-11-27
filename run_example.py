# run_example.py
"""
演示脚本：注册示例插件并运行一个演示任务
在本地运行： python run_example.py
"""
from autopilot_agent.agent import AutoPilotAgent
from plugins.example_plugin import example_tool
from autopilot_agent.utils import pretty
import json

def main():
    agent = AutoPilotAgent()
    agent.register_tool(example_tool)

    task = (
        "Find top 3 resources about vector databases. "
        "Summarize key points and provide links."
    )

    result = agent.run_task(task)
    pretty("Execution finished. Result:")
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
