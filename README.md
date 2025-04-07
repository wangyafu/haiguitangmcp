## 快速开始

你首先需要克隆整个项目，然后运行uv sync安装依赖。

其次，你需要在配置文件中加入（假设你将项目安装在了E盘）

```json
"haiguitang-mcp": {
                "type": "stdio",
                "command": "uv",
                "args": [
                    "--directory",
                    "E:\\haiguitangmcp\\haiguitang_mcp",
                    "run",
                    "server.py"
                ]
            }

```

具体的形式和位置可能会因mcp client的不同而有所不同。以上是基于vscode的配置。