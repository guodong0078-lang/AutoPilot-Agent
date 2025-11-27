# plugins/example_plugin.py
from autopilot_agent.tools import Tool

def can_handle(step: str) -> bool:
    """如果包含关键字 search 或 find 则可处理"""
    lower = step.lower()
    return "search" in lower or "find" in lower or "look up" in lower

def run(step: str) -> str:
    """示例工具的运行逻辑：模拟返回的结果（可替换为真实逻辑）"""
    # 这里我们只是返回一个模拟结果字符串
    return f"Simulated search results for: '{step}'"

example_tool = Tool(name="example_search", can_handle=can_handle, run=run)
