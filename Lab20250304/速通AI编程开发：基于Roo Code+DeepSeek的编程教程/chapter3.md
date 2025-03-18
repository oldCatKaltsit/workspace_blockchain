# （进阶篇）第3章 提示词（Prompts）配置项

## 3.1 Roo Code提示词配置了什么

众所周知，**提示词（Prompt）是用户向大语言模型输入的一段文本，用于指导大语言模型生成符合用户要求的输出**。在ai编程领域更是如此，提示词的好坏直接决定了大语言模型的输出结果。那么，Roo Code的提示词配置了什么？

Roo Code的提示词由以下三部分配置项组成：

1. **大语言模型回答的语言以及自定义规则**

2. **不同模式下大语言模型的提示词**

3. **支持性提示词**

## 3.2 大语言模型回答的语言以及自定义规则

![语言及规则配置项](https://s2.loli.net/2025/02/24/T1SGZM6xgRzatAl.png)

**Preferred Language**这个配置项用于配置大语言模型回答的语言，默认是中文，也可以根据自己需求选择其他语言。

**Custom Instructions for All Modes**这个配置项用于配置大语言模型在各个模式下（**第二章提到的Code、Architect、Ask、Debug模式**）要遵循的规则。这些指令**适用于所有模式**。它们提供了一套基础行为，可以通过下面的模式特定指令来进行增强。这个功能**笔者认为没必要使用**，因为下方一行小字：

> Instructions can also be loaded from **.clinerules** in your workspace.

也就是说，我们可以通过在项目里**新建.clinerules文件**，将项目要求、技术栈等写入这个文件，让大语言模型**依据特定的项目需求、技术栈等**，生成符合要求的代码。

以先前开发的"**番茄时钟**"为例，我们可以在.clinerules文件中写入这样的关键词，这里给了一个网页开发框架，如果用户在自己的电脑中**安装了这个框架**，可以尝试使用这个文件进行开发：

```
# 项目要求
- 使用Vite构建工具，搭建初始化环境
- 使用react框架进行开发
- 使用Tailwind CSS进行样式管理
- 使用TypeScript进行类型管理
......
```

大语言模型就可以根据这些关键词，基于文件中提到的网页开发框架，生成符合要求的代码。

## 3.3 不同模式下的提示词

在第二章的内容中，我们提到过，Roo Code支持四种模式：**Code、Architect、Ask、Debug**。在这里，我们可以深入研究不同模式下的提示词配置，甚至可以自定义模式。

![默认的四种模式的提示词配置](https://s2.loli.net/2025/02/24/jnU3BregoZ9DCpl.png)

每一个模式下都有四个配置项：

- **角色定义（Role Definition）**：用于规定大语言模型在不同模式下扮演的角色

- **API配置（API Configuration）**：用于配置大语言模型在不同模式下使用的API，这里默认均为default，也就是进入系统时默认配置的api

- **可用工具（Available Tools）**：用于配置大语言模型在不同模式下可用的工具，这里的工具就是Roo Code中**Auto-approve提供的部分工具**，包括**读取文件和目录，编辑文件，执行命令，调用浏览器，使用MCP服务器**。

默认的四个模式不允许修改可用工具，这四个模式可以使用的工具如下表所示：

| 模式 | 可用工具 |
| --- | --- |
| Code | 读取文件和目录，编辑文件，执行命令，调用浏览器，使用MCP服务器 |
| Architect | 读取文件和目录，编辑文件（**仅支持编辑markdown文件**），调用浏览器，使用MCP服务器 |
| Ask | 读取文件和目录，调用浏览器，使用MCP服务器 |
| Debug | 读取文件和目录，编辑文件，执行命令，调用浏览器，使用MCP服务器 |


- **模式特定自定义指令（Mode-specific Custom Instructions）**：可选项，Code模式下默认为空，可用于指定该模式下的特定行为。

我们以**Architect模式**为例，来看一下模式特定自定义指令的提示词：

```
原文：
Depending on the user's request, you may need to do some information gathering (for example using read_file or search_files) to get more context about the task. You may also ask the user clarifying questions to get a better understanding of the task. Once you've gained more context about the user's request, you should create a detailed plan for how to accomplish the task. (You can write the plan to a markdown file if it seems appropriate.)

翻译：
根据用户的请求，你可能需要进行一些信息收集（例如使用read_file或search_files）以获取有关任务的更多上下文。你也可以向用户提出澄清性问题，以更好地理解任务。一旦你对用户的请求有了更多了解，你就应该创建一个详细的任务执行计划。（如果觉得合适的话，你可以将计划写入markdown文件中。）
```

同样的，提示词下方有一行小字：

> Custom instructions specific to Architect mode can also be loaded from .clinerules-architect in your workspace.

也就是说，我们也可以在项目中新建.clinerules-architect文件，将模式特定自定义指令写入这个文件，让大语言模型**依据特定的项目需求**，生成符合要求的代码。

如果大家想将整个提示词迁移到其他编程工具中使用，可以点击下方“**Preview System Prompt**”按钮，将提示词复制到剪贴板中，这种模式下的提示词经过了高度抽象，因此长度会非常长。

![Code模式下的系统提示词](https://s2.loli.net/2025/02/26/IJA9vX6NwoZzFxB.png)

## 3.4 支持性提示词

![支持性提示词配置项](https://s2.loli.net/2025/02/26/Oea6Fhx4nLi2Uv7.png)

如图所示，这一部分的提示词用于增强Roo Code的功能，包括：

- **增强用户所写的提示词（Enhance Prompt）**
- **代码解释（Explain Code）**
- **修复代码错误（Fix Issues）**
- **提升代码可读性、可维护性（Improve Code）**
- **向对话补充内容（Add to Context）**
- **将终端内容补充进入对话（Add Terminal Content to Context）**
- **修复终端命令报错（Fix Terminal Command）**
- **解释终端命令（Explain Terminal Command）**

其中，**Enhance Prompt**在第二章就已经使用过，通过点击✨按钮，可以增强用户所写的提示词。**Explain Code**、**Fix Issues**、**Improve Code**、**Add to Context**这四部分提示词用于针对**代码片段**进行操作，**Add Terminal Content to Context**、**Fix Terminal Command**、**Explain Terminal Command**这三部分提示词用于针对**终端命令**进行操作。

## 3.5 用户如何自定义具有特定功能的提示词

这部分在Modes部分进行配置，点击右上角的“+”按钮，即可添加新的模式。

![添加新的模式](https://s2.loli.net/2025/02/26/65upBolyUMTz7dL.png)

这里举一个我学习rust编程语言的例子，我的需求是让Roo Code扮演一个**rust编程语言专家**，但是它能够逐步引导“**不怎么了解计算机底层逻辑，但是了解一些编程语言的基础知识**”的我，并且**不会直接给出**代码实现逻辑，而是让我自己思考，并且给出思考方向，让我自己实现。

**Name**：模式名称，这里我命名为“RustProfessor”

**Slug**：模式的标识符号，用于URL和文件名，只能使用小写字母、数字和连字符，这里我命名为“rust-professor”

**Save Location**：保存位置，Global表示**该模式全局生效**，Project-specific会通过新建一个.roomodes文件，**该模式只在当前项目生效**，这个模式的优先级高于Global。这里我选择Global

**Role Definition**：角色定义，这里我是这样写的：

```
你是roo，同时也是一个rust编程导师，你能够用苏格拉底式提问法引导用户自主推导 Rust 的核心思想，像拼乐高一样帮用户从已知编程知识迁移到 Rust 的独特世界观，而非直接传授答案
```

**Available Tools**：可用工具，这里我只**保留了Read Files权限**，因为我想让大语言模型**只读取文件**，而不是**编辑文件**

**Custom Instructions (optional)**：模式特定自定义说明（可选），这里我是这样写的：

```
你要遵循以下行为准则：
1. 拆解脚手架原则
当收到问题时会先反问：
💡 "你觉得这个问题的核心矛盾可能和 Rust 的哪个特性相关？（比如所有权/借用检查/模式匹配）"
💡 "如果用你熟悉的XX语言类比，这里会遇到什么问题？Rust 会如何用不同方式解决？"

2. 隐喻大师模式
用生活化比喻解释底层概念：
🌰 "所有权就像图书馆借书，同一时间只能有一个读者做笔记"
🌰 生命周期标注是 "给编译器画地图，防止数据在旅途中迷路"

3. 最小提示策略
当代码卡住时给出：
⚠️ "注意这个错误提示中的`move`关键字，回忆变量所有权传递的规则"
⚠️ "是否需要在这个结构体里实现`Drop`或`Clone`特性？为什么？"

4. 错题本引导法
对常见误区（如过度克隆、生命周期恐惧症）：
📌 "很多新手会在这里用.clone()，你觉得这是最优解吗？代价是什么？"
📌 "如果不用引用计数指针，能否用更Rust的方式重构这段关系？"

你和用户的对话流程设计方式如下：
1. 概念锚点
先定位你已有知识："你说了解过Python的装饰器，Rust的trait类似但更强调..."

2. 矛盾具象化
制造认知冲突："如果用Java的思路直接写这段代码，编译器会报什么错？为什么？"

3. 阶梯式挑战
从简单案例开始："先尝试用不可变引用实现X功能，成功后再挑战可变引用的版本"

4. 编译器视角
引导扮演编译器："如果现在你是borrow checker，会如何分析这段代码的数据流？"

你不允许进行以下行为：
❌ 直接写出完整代码
❌ 使用"只要记住..."式说教
❌ 讨论超出当前引导路径的底层细节

启动示例
用户：想用Rust读取文件但总是编译不过😣
Roo：
1️⃣ (锚点) "在其他语言里你是如何操作文件的？会显式关闭资源吗？"
2️⃣ (矛盾) "猜猜Rust的`?`操作符在这里承担了哪些隐式责任？"
3️⃣ (提示) "注意`read_to_string`的返回值类型，需要处理哪些潜在错误？"
```

点击下方“Create Mode”按钮，即可创建新的模式。

我们新建一个空的rust项目，在项目下新建一个main.rs文件，输入以下**错误内容**：

```rust
print("hello world")
```

切换到“RustProfessor”模式，输入以下引导查看效果：

```
我是从其他编程语言转过来的，头一次接触rust这门语言，编写了一个hello world程序，但是总是报错，你能帮我解决这个问题吗？
```

![扮演的老师发现了报错](https://s2.loli.net/2025/02/27/plNmbgwZva9XjhW.png)

可以看出，扮演的老师发现了报错，并且给出了**错误提示**，我按照错误提示修改后的，改成了这样：

```rust
println!("hello world");
```

当然，这段代码依然是无法运行的，扮演的老师继续引导我，让我思考问题出在哪里。最后发现，没有使用main函数。

![扮演的老师引导我思考问题出在哪里](https://s2.loli.net/2025/02/27/lqFakjmvODPd1hB.png)

最后，我按照老师的引导，修改了代码，得到了正确的代码，至此，扮演的老师成功引导我自主推导出了Rust的核心思想，像拼乐高一样帮用户从已知编程知识迁移到 Rust 的独特世界观，而非直接传授答案。

```rust
fn main() {
    println!("hello world");
}
```

到这里，Roo Code的提示词配置就已经全部介绍完毕了。接下来带领大家讲解MCP服务，并且介绍如何搭建并使用mcp服务。