# autopilot_agent/agent.py
from typing import Dict, Any, List
from .tools import ToolRegistry, Tool
from .utils import pretty

class AutoPilotAgent:
    """
    最简本地 Agent 实现：
    - register_tool(tool)：注册 Tool 实例
    - run_task(task_str)：接收自然语言任务，按句子拆解为步骤并执行
    """
    def __init__(self):
        self.tools = ToolRegistry()

    def register_tool(self, tool: Tool):
        self.tools.register(tool)

    def run_task(self, task: str) -> Dict[str, Any]:
        pretty(f"Received task: {task}")
        # 基础规划：按句号/换行拆分（简单示例）
        raw_steps = [s.strip() for s in task.replace("\n", ".").split(".") if s.strip()]
        results: List[Dict[str, Any]] = []
        for i, step in enumerate(raw_steps, 1):
            pretty(f"Step {i}: {step}")
            handler = self.tools.find_handler(step)
            if handler:
                try:
                    res = handler.run(step)
                    results.append({"step": step, "tool": handler.name, "result": res})
                    pretty(f"Handled by: {handler.name}")
                except Exception as e:
                    results.append({"step": step, "tool": handler.name, "result": f"Error: {e}"})
            else:
                results.append({"step": step, "tool": None, "result": "No tool handled this step"})
        return {"task": task, "results": results}
