<p align="center">
  <img src="https://github.com/kunwu2023/kunwu/assets/31091395/956c21f3-f829-49b3-8358-d2e3ebced65b" width="120">
</p>
<h1 align="center"> KunWu </h1>
<p align="center">
<img alt="Static Badge" src="https://img.shields.io/badge/Build-v0.1.0-blue">
<img alt="Static Badge" src="https://img.shields.io/badge/License-MIT-green">

<p align="center"> 「<b>KunWu_Cli</b>」Python重构版本</p>
<p align="center"> 集 <b>模糊规则</b>/<b>污点分析模拟执行</b>/<b>机器学习</b> 三种高效检测策略，精准无误地发现 WebShell 风险</p>

# ✈️ 1# 工具概述

本项目为默安科技打造的新一代 WebShell 检测工具「KunWu_Cli」的Python重构版本

原项目地址：[https://github.com/kunwu2023/kunwu/](https://github.com/kunwu2023/kunwu/)

本项目结构主体结构如下：

| 名称        | 说明         |
|-----------|------------|
| main.py   | 程序入口点      |
| Scan.py   | 扫描模块核心代码   |
| config.py | 工具模块代码     |
| logo.py   | Kunwu logo |
| config.py | 程序配置文件     |

# 📝 2# TODO

* [x] 在基于原项目的基础上加入了异步检测的代码
* [x] 对代码进行了部分优化

# 🚨 3# 快速开始

### 3.1 安装依赖包

```
pip install -r requirements.txt
```

如果pip安装速度慢，可以采用国内源进行安装：

```
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

### 3.2 运行

```
python3 main.py --path /path/to/file
```

### 3.3 运行结果示例

![img/img.png](img/img.png)
![img/img_1.png](img/img_1.png)


# 🙏 4# 感谢各位师傅

## Stargazers

[![Stargazers repo roster for @Re1axCyber/PyKunwu_Cli](http://reporoster.com/stars/Re1axCyber/PyKunwu_Cli)](https://github.com/Re1axCyber/PyKunwu_Cli/stargazers)


## Forkers

[![Forkers repo roster for @Re1axCyber/PyKunwu_Cli](http://reporoster.com/forks/Re1axCyber/PyKunwu_Cli)](https://github.com/Re1axCyber/PyKunwu_Cli/network/members)


## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Re1axCyber/PyKunwu_Cli&type=Date)](https://star-history.com/#Re1axCyber/PyKunwu_Cli&Date)
