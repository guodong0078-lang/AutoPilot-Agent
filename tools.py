# autopilot_agent/tools.py
from typing import Callable, List

class Tool:
    """
    Tool 表示一个可以被 Agent 使用的“工具”
    - name: 工具名称
    - can_handle: 接收 step 文本，返回是否能处理
    - run: 执行函数，返回处理结果（字符串）
    """
    def __init__(self, name: str, can_handle: Callable[[str], bool], run: Callable[[str], str]):
        self.name = name
        self.can_handle = can_handle
        self.run = run

class ToolRegistry:
    """工具注册与访问"""
    def __init__(self):
        self._tools: List[Tool] = []

    def register(self, tool: Tool):
        self._tools.append(tool)

    def get_all(self) -> List[Tool]:
        return list(self._tools)

    def find_handler(self, step: str):
        for tool in self._tools:
            try:
                if tool.can_handle(step):
                    return tool
            except Exception:
                continue
        return None
