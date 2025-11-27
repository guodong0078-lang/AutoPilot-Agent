# autopilot_agent/utils.py
from rich import print

def pretty(msg: str):
    """终端友好输出"""
    print(f"[bold cyan][AutoPilot][/bold cyan] {msg}")
