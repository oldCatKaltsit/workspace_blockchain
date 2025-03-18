# （进阶篇）第4章 MCP服务

## 4.1 什么是MCP服务

MCP（Model Context Protocol）是模型上下文协议的简称，它是一种允许Roo Code与本地运行的MCP服务器进行通信的协议。这些服务器提供额外的工具和资源，可以显著扩展Roo Code的功能。通过MCP服务，我们可以实现：

- **功能扩展**：添加Roo Code原生不支持的新功能
- **数据整合**：将外部数据源与Roo Code连接
- **自定义工具**：创建适合特定工作流程的专用工具

在第2章中，我们简单提到过MCP服务是Roo Code菜单栏的一部分，现在让我们深入了解它的工作原理和实际应用。

![MCP服务菜单](https://s2.loli.net/2025/03/03/xUBi5dqHsbjawWe.png)

## 4.2 MCP服务的工作原理

为方便阐述MCP服务的工作原理，这里引用一个场景，用户要通过外部程序向其他人打招呼：

1. **服务注册**：用户在本地启动MCP服务器，并在Roo Code中**注册向其他人打招呼的服务**,这个步骤其实是同时进行的
2. **功能暴露**：MCP服务器向Roo Code暴露一系列工具和功能
3. **用户请求**: 用户向**大语言模型**发送一个请求，例如“请向学习者打招呼”。
4. **模型判断**: **大语言模型**分析用户请求，判断它是否需要外部工具。 如果需要，例如需要向学习者打招呼，它会生成一个包含工具名称和参数的 JSON 对象。
5. **工具调用**: Roo Code 接收到这个 JSON 对象，并调用相应的工具。
6. **工具响应**: 工具执行操作，并将结果返回给 Roo Code。 例如，打招呼 API 返回确认执行的信息。
7. **模型响应**: Roo Code 利用工具返回的信息，生成最终的、用户友好的回复。 例如，“Hello 学习者!”

整个过程如下图所示：

![MCP服务工作流程](https://s2.loli.net/2025/03/03/okujADNHZPeS68G.png)

从技术角度看，MCP服务实际上是一个遵循特定协议的服务器，它与Roo Code进行通信，提供各种功能接口。

## 4.3 使用python创建一个MCP服务

### 4.3.1 准备工作

创建MCP服务需要一定的编程基础，通常我们会使用Node.js或Python来构建服务。在开始前，请确保：

- 已安装Node.js或Python
- 了解基本的HTTP服务器概念
- 有一定的JavaScript或Python编程经验

我们这里演示使用**python**创建一个简单的mcp服务，功能是用于打招呼。

### 4.3.2 使用Python创建简单的MCP服务

1. 首先创建一个新的项目文件夹，并安装mcp：

```bash
mkdir python-mcp-server
cd python-mcp-server
pip install mcp
```

2. 创建一个`main.py`文件，内容如下：

```python
# 导入必要的模块
import logging
from mcp.server.fastmcp import FastMCP

# 设置日志配置
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class HelloService:
    """一个简单的 MCP 问候服务

    这个服务提供一个基础的问候工具，可以根据提供的名字返回问候语。
    它展示了如何创建一个基本的 MCP 服务器并注册工具。
    """

    def __init__(self):
        # 创建一个 FastMCP 服务器实例
        # FastMCP 是 MCP 的高级抽象，它简化了服务器的创建和管理
        self.server = FastMCP("hello-service")

        # 使用装饰器注册工具
        # FastMCP 会自动从函数签名和文档字符串中提取工具的描述和参数信息
        @self.server.tool()
        async def greet(name: str = "World") -> str:
            """基础问候服务

            Args:
                name (str): 要问候的名字，默认为 "World"

            Returns:
                str: 问候语
            """
            logger.info(f"收到问候请求，name: {name}")
            result = f"Hello {name}!"
            logger.info(f"返回结果: {result}")
            return result

    def run(self):
        """运行服务器

        这个方法启动 MCP 服务器并处理来自客户端的请求。
        服务器会一直运行，直到发生错误或被手动停止。
        """
        try:
            logger.info("✅ MCP服务启动中...")
            logger.info("服务名称: hello-service")
            logger.info("等待连接...")
            # FastMCP 的 run 方法会自动处理:
            # - 服务器初始化
            # - 连接管理
            # - 请求处理
            # - 错误处理
            self.server.run()
        except Exception as e:
            logger.error(f"❌ 服务异常: {str(e)}")
            raise


if __name__ == "__main__":
    # 创建服务实例并运行
    service = HelloService()
    service.run()
```

3. 运行服务器：

```bash
python app.py
```

至此，这个Python版本的MCP服务提供了一个简单的打招呼工具，用于演示目的。

## 4.4 添加MCP服务

我们可以通过以下步骤添加现有的MCP服务：

1. 点击Roo Code菜单栏中的"**MCP Servers**"
2. 启用"**Enable MCP Servers**"和"**Enable MCP Server Creation**"
3. 点击"**Edit MCP Settings**"，会出现一个json文件
4. 编辑`cline_mcp_settings.json`文件，这里给出我的配置文件，并且解释每个配置项的含义(由于json中不允许出现注释，因此大家在实际编辑文件中，请去掉注释)：

```
{
  "mcpServers": {
    "hello": // 添加的mcp服务名称
    { 
      "command": "/Users/michaelbradley/Documents/Cline/MCP/print/.conda/bin/python", // 由于mcp服务调用python运行，这里添加python的绝对路径
      "args": [
        "/Users/michaelbradley/Documents/Cline/MCP/print/main.py"
      ], // mcp服务的main.py的绝对路径
      "cwd": "/Users/michaelbradley/Documents/Cline/MCP/print" // mcp服务项目的绝对路径
    }
  }
}
```

保存后`cline_mcp_settings.json`文件，Roo Code会**自动连接并启用**该服务。

![MCP服务添加成功](https://s2.loli.net/2025/03/03/iwBfMbvD7ApktuV.png)

这里红色信息代表**MCP服务添加并链接成功，不是报错**，无视即可。

## 4.5 在Roo Code调用MCP服务

回到Roo Code主界面，确保**Auto-approve**选项里“**Use MCP Servers**”选项开启.可以输入一下提示词进行测试：

```
向学习者打招呼
```

可以看到，Roo Code会要求你调用已经链接的MCP服务器，并且成功输出response：

![Roo Code调用服务](https://s2.loli.net/2025/03/03/QHnO6GB2Rdictv8.png)


## 4.6 MCP服务的未来发展

目前MCP服务潜力尚未完全开发，随着MCP协议的不断发展，我们可以期待：

- **更丰富的协议特性**：支持更复杂的交互模式和数据类型
- **社区驱动的服务生态**：更多开源MCP服务的出现
- **专业领域服务**：针对特定行业和领域的专业MCP服务
- **服务集成平台**：简化MCP服务的发现、部署和管理的平台

## 4.7 总结

MCP服务为Roo Code提供了强大的扩展能力，使其能够连接到外部数据源和工具。通过创建自定义MCP服务，我们可以根据自己的需求和工作流程定制Roo Code的能力，从而更高效地完成各种任务。

无论是简单的工具扩展，还是复杂的数据整合和分析，MCP服务都为AI辅助编程提供了无限可能。随着你对MCP服务的熟悉和深入理解，你将能够创建越来越强大的工具来增强你的AI编程体验。

## 4.8 参考学习资源

[MCP官方项目](https://github.com/modelcontextprotocol/servers)

[MCP文档](https://modelcontextprotocol.io/introduction)

[精选MCP服务器](https://github.com/punkpeye/awesome-mcp-servers)