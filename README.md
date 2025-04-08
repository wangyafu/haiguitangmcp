## 介绍

本项目旨在让大语言模型扮演海龟汤游戏主持人，使你独自一人也能享受海龟汤游戏的快乐。

## 快速开始

在使用本项目前，你需要确保你的电脑上已经安装了Python和uv。


你首先需要克隆整个项目，然后运行uv sync安装依赖。

```bash
git clone https://github.com/wangyafu/haiguitangmcp/
cd haiguitangmcp
uv sync
```

其次，你需要修改配置文件（假设你将项目安装在了E盘）

### 在vscode中配置

```json
"mcp":{
    "servers":{
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
    }
}


```

### 在cherry studio中进行配置

```json
"mcpServers": {
    
    "haiguitang": {
      "isActive": true,
      "name": "海龟汤MCP服务器",
      "description": "和用户玩海龟汤",
      "registryUrl": "",
      "command": "uv",
      "args": [
        "--directory",
        "E:/haiguitangmcp/haiguitang_mcp",
        "run",
        "server.py"
      ]
    },
   
}

```

上述的"E:/haiguitangmcp/haiguitang_mcp"表示server.py所在的路径。

在其他mcp client中的配置方法类似。

## mcp相关内容

本项目提供了三个工具:

- `get_prompt`: 获取海龟汤游戏的完整玩法说明
- `get_puzzle`: 获取一个特定谜题的完整内容，需要提供谜题标题作为参数
- `list_puzzles_tool`: 列出所有可用的谜题列表

同时，本项目还提供了以下资源:

- `puzzles://{puzzle_title}`: 获取特定谜题的信息

以及一个提示模板:

- `game_rules`: 提供海龟汤游戏规则的提示模板

## 游戏规则

在本游戏中：

- 海龟汤是一种情景推理游戏，谜题本身并没有很强的逻辑性，注重能否发现关键线索重现情景
- 出题人提出一个看似不合常理的问题和情景（谜面），猜题者通过提问缩小范围并最终揭示完整故事情节（谜底）
- 猜题者可以提出任何问题，出题人主要用"是"、"不是"、"是也不是"或"没有关系"来回答
- 当问题中既有对的地方也有不对的地方时，出题人会回答"是也不是"
- 当问题与谜题核心情节无关时，出题人会回答"没有关系"
- 猜题者可以通过在消息开头加上"汤底"来尝试描述完整情景
- 当猜题者掌握了关键线索时，出题人会提醒猜题者归纳线索，形成对谜底的完整描述
- 猜题者可以请求引导和提示，出题人会给予尚未掌握的线索
- 当猜题者的描述大致包含了谜题的关键情景时，出题人会确认"完全正确"


### 小技巧

- 从基本问题开始，如谜题涉及人数、死者的死因等。
- 注意谜面中的每一个细节，它们可能是关键线索
- 当你感到困惑时，尝试从不同角度思考问题
- 记录已经确认的线索，以便归纳整理

## 关于谜题

目前本项目已经提供了35个谜题。
本人曾开发[海龟汤模拟器](https://www.hgtang.com)，该网站有评分功能。目前的35个谜题来自于我和一些热心用户为该网站搜集的谜题。依据该网站上各谜题的评分，推荐游玩的谜题如下：

- 忠诚的狗
- 100元钱
- 爱犬
- 治病
- 祭日
- 电梯里的人
- 延迟死亡
- 生意
- 裤子破了
- 要好的朋友

欢迎你为本项目贡献更多的谜题。你可以在haiguitang_mcp/puzzles文件夹中加入新的谜题文件然后发起Pull Request。

注意：

- 如果你希望用户游玩之前有所预警，你可以在标题，也就是谜题文件的名称中注明。
- 请注意海龟汤的版权问题。
- 你可以在海龟汤文件中添加作者和提交者信息。

