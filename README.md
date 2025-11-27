# AutoPilot-Agent

AutoPilot-Agent — 一个面向新手友好的本地自动化 Agent 框架模板。
目标：快速搭建可扩展的本地 Agent，支持插件化工具（Tool）。

## 功能（v0.1）
- 插件式工具系统（Tool / ToolRegistry）
- 最简任务分解与执行（按句拆分）
- 示例插件（`plugins/example_plugin.py`）
- 本地运行示例 `run_example.py`

## 快速开始（Windows / macOS / Linux）
```bash
# 1 克隆仓库（如果你无法 git clone，可直接在 GitHub 页面上传文件）
git clone https://github.com/你的用户名/AutoPilot-Agent.git
cd AutoPilot-Agent

# 2 创建并激活虚拟环境（推荐）
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate

# 3 安装依赖
pip install -r requirements.txt

# 4 运行示例
python run_example.py
