import os
import glob
from mcp.server.fastmcp import FastMCP, Context
from pydantic import BaseModel
from mcp.server.fastmcp.prompts import base
# 创建 MCP 服务器

prompt="""我们在玩海龟汤游戏。
现在请你来扮演海龟汤游戏的出题人，而我是猜题者。
接下来你需要帮助我享受解谜的乐趣。

## 背景
海龟汤是一种情景推理游戏。游戏中的谜题本身并没有很强的逻辑性，注重能否发现关键线索重现情景。
其玩法是由出题者提出一个看似不合常理的问题和情景（也就是谜面），参与猜题者可以提出任何问题以试图缩小范围并最终揭示出完整的故事情节（也就是谜底）。

## 任务
- 回答问题。
- 当猜题者通过提问掌握了谜题中关键线索时，提醒猜题者归纳线索，形成对谜底的完整描述。
- 判断猜题者的描述是否完全正确。
- 在猜题者请求引导和提示时，给与线索。
- 在猜题者请求归纳线索时，整理猜题者目前已经获得的线索，但不要给出猜题者还未掌握的线索。

### 回答问题
- 出题人主要用“是”“不是”回答问题。
- 如果猜题者的问题中既有对的地方也有不对的地方，出题人还可以回答“是也不是”。
- 问题与谜题的核心情节无关时，出题人还可以回答“没有关系”。
- 出题人不会使用其他的话来回答问题，以免泄露谜底。
### 判断描述

- 当猜题者的描述大致上包含了谜题的关键情景时，回答{完全正确}。
- 如果猜题者的描述有明显的错误或严重的疏漏，指出猜题者在哪些地方有错误，或还需要在哪些地方进行推理。

### 引导
- 在用户请求引导时，给予猜题者尚未掌握的线索。
- 当猜题者输入“111”、“cnm”这样意义不明的文字，或直接表露出了挫败情绪时，你可以主动询问猜题者是否愿意接受引导。
## 注意事项
- 出题者不能泄露谜底中的线索，否则猜题人将失去解谜的乐趣。
- 出题人依据谜面和谜底中所述的情景进行回答。出题人还可以参考关于谜题的注意事项。
- 当猜题者的话以“汤底”开始时，意味着他在尝试对谜题中的情景进行描述，而非向你提问。
- 当猜题者的话没有以“汤底”开始时，可能猜题者仍然在对情景进行描述，只是忘记了加上“汤底”

"""
# 定义谜题结构
class Puzzle(BaseModel):
    title: str
    content: str

def main():
    mcp = FastMCP("海龟汤")
    # 存储所有谜题
    puzzles = {}
    current_puzzle = None
    # 加载谜题文件
    def load_puzzles():
        # 获取当前脚本所在目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.dirname(current_dir)  # 获取上一级目录

        # 查找多个可能的路径
        puzzle_paths = [
            os.path.join(current_dir, "puzzles", "*.md"),  # app/puzzles/*.md
            os.path.join(base_dir, "haiguitang-mcp", "puzzles", "*.md"),  # 项目根目录/app/puzzles/*.md
            os.path.join(base_dir, "puzzles", "*.md"),  # 项目根目录/puzzles/*.md
            os.path.join(base_dir, "*.md"),  # 项目根目录/*.md
        ]

        for path_pattern in puzzle_paths:
            print(f"正在搜索路径: {path_pattern}")
            puzzle_files = glob.glob(path_pattern)
            for file_path in puzzle_files:
                puzzle_title = os.path.basename(file_path).replace(".md", "")
                if "README" in puzzle_title:
                    continue
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()


                    # 创建谜题对象
                    puzzle = Puzzle(
                        title=puzzle_title,
                        content=content
                    )
                    puzzles[puzzle_title] = puzzle
                    print(f"已加载谜题: {puzzle_title}")
                except Exception as e:
                    print(f"加载谜题 {puzzle_title} 失败: {str(e)}")

        if not puzzles:
            print("警告：未找到任何谜题文件")

    # 初始化时加载谜题
    load_puzzles()


    # 提供单个谜题资源
    @mcp.resource("puzzles://{puzzle_title}")
    def get_puzzle(puzzle_title: str) -> str:
        """获取特定谜题的信息"""
        try:
            puzzle = puzzles[puzzle_title]
            return str(puzzle)
        except KeyError:
            return "找不到该谜题"
    # 提供游戏规则的提示模板
    @mcp.prompt()
    def game_rules() -> list[base.Message]:
        """海龟汤游戏规则"""

        return [base.UserMessage(prompt)]
    @mcp.tool()
    def get_prompt()->str:
        '''获取海龟汤游戏的玩法'''
        return prompt
    # 工具：选择谜题
    @mcp.tool()
    def get_puzzle(puzzle_title: str) -> str:
        """获取一个谜题的完整内容

        Args:
            puzzle_title: 海龟汤的标题

        Returns:
            选择结果信息
        """
        try:
            puzzle=puzzles[puzzle_title]
            return str(puzzle)
        except KeyError:
            return "找不到该谜题"

    # 工具：列出所有谜题
    @mcp.tool()
    def list_puzzles_tool() -> str:
        """列出所有可用的谜题

        Returns:
            谜题列表
        """
        puzzle_list = []
        for puzzle_id, puzzle in puzzles.items():
            puzzle_list.append(f"- {puzzle_id}")
        return "可用谜题列表:\n" + "\n".join(puzzle_list)
    mcp.run(transport="stdio")
if __name__=="__main__":
    main()

