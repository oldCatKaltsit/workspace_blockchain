# （基础篇）第1章 环境下载、安装与配置

## 1.1 vscode下载与安装

由于Roo Cline（现已更名为Roo Code）依赖编程IDE环境才可以运行，因此我们需要下载vscode，点击这个链接，根据你自己的操作系统进行下载：https://code.visualstudio.com/Download

![vscode下载界面](https://s2.loli.net/2025/02/20/eBGk6sLa9DJA4mW.png)

### 针对Windows系统用户的注意事项：

**Windows系统**用户下载好vscode之后，双击exe文件，选择“我同意此协议”
![我同意此协议](https://s2.loli.net/2025/02/20/tNHu9jOyZSqgC6Y.png)

点击下一步选择软件安装目录，点击下一步选择是否创建开始菜单文件夹，点击下一步选择附加任务（这里建议勾选“**添加桌面快捷方式**”以及“**添加到PATH（重启后生效）**”）

![这里会显示出所有软件接下来会执行的操作](https://s2.loli.net/2025/02/20/KogicTb85Fqz12O.png)

点击“安装”，之后点击“完成”按钮即可完成安装。

![点击“完成”按钮即可完成安装](https://s2.loli.net/2025/02/20/pvYazVoE9R5GfPT.png)

### 针对macOS系统用户的注意事项：

macOS系统用户下载好vscode之后，解压缩会得到一个“Visual Studio Code”的应用程序，打开“**访达**”，将其**拖动到左侧“应用程序”目录**即可完成安装。

![选中“Visual Studio Code”应用程序，拖动到“应用程序”目录即可完成安装](https://s2.loli.net/2025/02/20/vfdHkUzFrR1KV9M.png)

## 1.2 Roo Cline（现已更名Roo Code）下载与安装

打开界面左侧的扩展按钮，在搜索框中搜索“Roo Code”，找到对应扩展，点击“Install”按钮进行安装：

![Roo Code安装](https://s2.loli.net/2025/02/20/4XRzSA7yCcgZN2h.png)


![点击Install按钮](https://s2.loli.net/2025/02/20/1g835qMzbYHnJrT.png)

![选择信任并安装](https://s2.loli.net/2025/02/20/3MhHk4VidesK96o.png)

安装成功后的初始化界面如下图所示：

![Roo Code主界面](https://s2.loli.net/2025/02/20/OuLDWwIbSq5cFJk.png)

## 1.3 （可选）vscode的汉化

点击“**扩展**”按钮，在搜索框中搜索“Chinese”，找到**微软官方**的扩展（一般情况是第一个），同样点击“Install”按钮安装，然后**重启vscode**即可完成汉化：

![vscode汉化](https://s2.loli.net/2025/02/20/YiaufLgTG7U4Wmv.png)

## 1.4 Roo Cline（现已更名Roo Code）配置deepseek

由于目前支持deepseek的服务商较多，这里分为**官方渠道**和**非官方渠道**讲解如何配置模型：

### 1.4.1 deepseek官方api

需要注意的是，截至写稿前，官方接口的计费体系尚未完全开放，因此本部分的配置示例基于您**已注册deepseek开放平台**并拥有**有效API-key及可用额度的前提**，这是调用接口的必要技术条件。

打开Roo Code的初始化界面，点击“API Provider”下拉列表，选择“**DeepSeek**”，在下方“DeepSeek API Key”输入开放平台中的API-key，点击下方“Let's go!”即可完成配置。

![官方渠道配置](https://s2.loli.net/2025/02/20/jtXYmxJQrZGqOzN.png)

### 1.4.2 兼容openai格式的第三方api

目前绝大多数deepseek非官方渠道均兼容openai的api格式，这里以[**硅基流动**](https://cloud.siliconflow.cn)为例进行演示，其他非官方渠道同理。

点击链接注册账号之后，点击“**实名认证**“完成实名，然后点击左侧的**API密钥——新建API密钥**，输入描述信息之后，点击“**新建密钥**”，即可完成密钥创建。

![硅基流动创建API-key](https://s2.loli.net/2025/02/20/mvp9EFz1kISfrxN.png)

点击密钥进行复制，打开Roo Code的初始化界面，点击“API Provider”下拉列表，选择“**OpenAI Compatible**”，在下方“Base URL”输入`https://api.siliconflow.cn/v1`,“API Key”输入硅基流动平台复制的密钥，"Model"页面搜索“**deepseek-ai/DeepSeek-R1**”，选中即可添加成功。

![非官方渠道配置](https://s2.loli.net/2025/02/20/zGeL19ERhOKvNF2.png)

这里补充硅基流动中deepseek-ai/DeepSeek-R1与Pro/eepseek-ai/DeepSeek-R1的区别：

|区别|deepseek-ai/DeepSeek-R1|Pro/deepseek-ai/DeepSeek-R1|
|---|---|---|
|是否可用赠费|既可使用赠费，也可使用充值余额|只能使用充值余额|
|是否需要实名使用|未实名用户每日最多请求此模型 100 次|无需实名|

至此，环境下载、安装和配置全部结束。欢迎大家补充其他渠道deepseek的接入方法。