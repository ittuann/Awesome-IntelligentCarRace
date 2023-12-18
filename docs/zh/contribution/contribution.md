# 提交指南

参与本项目的协作**需要**一个 GitHub 账号（可以前往 [GitHub 账号注册页面](https://github.com/signup) 页面注册），**并不需要**高超的 GitHub 技巧。

如果您想要向这份表格中提交新的内容，请参考本提交指南的内容。

!!! note "提交前请注意"

    在提交 [Pull Request](https://github.com/ittuann/Awesome-IntelligentCarRace/pulls){:target="\_blank"} 前，请仔细阅读本提交引导文档。

    如果您不熟悉下面 Git 操作等，请查看[帮助通道](https://ittuann.github.io/Awesome-IntelligentCarRace/contribution/#_5)。

提交信息最多只需两个步骤：1.[向表格中增加信息](https://ittuann.github.io/Awesome-IntelligentCarRace/contribution/#_2) -> 2.[测试添加后的效果](https://ittuann.github.io/Awesome-IntelligentCarRace/contribution/#_3)(非必须但推荐)

您也可以考虑直接使用[帮助通道](https://ittuann.github.io/Awesome-IntelligentCarRace/contribution/#_5)内提交 issue 的方式进行信息的补充。

## 向表格中增加信息

首先，请登录您的 Github 账号。打开本项目的仓库链接: <https://github.com/ittuann/Awesome-IntelligentCarRace>{:target="\_blank"} ，然后在页面的右上角点击 `Fork` 按钮，以便将本仓库分支到您的个人账号。

确保您已经克隆了最新版本的仓库，并且在正确的 [`main`](https://github.com/ittuann/Awesome-IntelligentCarRace/tree/main){:target="\_blank"} 分支上进行操作。

想要在表格中添加新的内容，仅需要直接修改项目**根目录**的 [`table.csv`](https://github.com/ittuann/Awesome-IntelligentCarRace/blob/main/table.csv){:target="\_blank"}。

在 [`table.csv`](https://github.com/ittuann/Awesome-IntelligentCarRace/blob/main/table.csv){:target="\_blank"} 表格的最后一行后，追加您想要添加的一行新条目。请确保您提交的数据格式正确，并与表单内现有条目保持一致。信息的添加即可完成。

如果您已增加了信息但没有执行下一步在本地测试添加后的效果，请在 Pull Request 内**明确注明**。

## 测试添加后的效果

为了保提交不会引入任何错误，在本地测试添加信息后的网页效果时，首先需要安装 Python 环境和依赖。在项目的根目录中，运行以下命令来安装必要的依赖：

```python
pip install -r requirements.txt
```

然后运行脚本，生成筛选后的各个分表：

```python
python scripts/split.py
```

执行以下命令来在本地查看修改后的运行效果：

```shell
mkdocs serve -f docs/mkdocs.yml
```

如果在运行项目过程中没有出现任何报错，那就代表您成功地完成了增加信息后的测试。您也可以在本地浏览打开`http://127.0.0.1:8000/Awesome-IntelligentCarRace/`查看效果。

## 提交更改

在确认所有更改都正常工作后，您可以将更改提交到您的分支，并创建一个 [Pull Request](https://github.com/ittuann/Awesome-IntelligentCarRace/pulls){:target="\_blank"}，即可完成信息的补充。

## 项目代码文档

项目采用 CI/CD 流程自动完成构建和部署。如果您想了解完整的工作流，可以查看本仓库的 [Github Action](https://github.com/ittuann/Awesome-IntelligentCarRace/actions){:target="\_blank"}。这里包含了整个自动化流程详细的步骤和运行记录。

项目代码覆盖率测试可在此查看: [Codecov](https://app.codecov.io/gh/ittuann/Awesome-IntelligentCarRace){:target="\_blank"} [![Codecov Coverage](https://codecov.io/gh/ittuann/Awesome-IntelligentCarRace/graph/badge.svg?token=UZT4S22K06)](https://codecov.io/gh/ittuann/Awesome-IntelligentCarRace){:target="\_blank"} ; 项目代码质量分析请访问: [Codacy](https://app.codacy.com/gh/ittuann/Awesome-IntelligentCarRace/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/35d02f5299284eefadd465b0d01a8fce)](https://app.codacy.com/gh/ittuann/Awesome-IntelligentCarRace/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade){:target="\_blank"} ; 仓库许可证合规性扫描请查看: [FOSSA](https://app.fossa.com/projects/git%2Bgithub.com%2Fittuann%2FAwesome-IntelligentCarRace){:target="\_blank"} [![FOSSA License Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fittuann%2FAwesome-IntelligentCarRace.svg?type=small)](https://app.fossa.com/projects/git%2Bgithub.com%2Fittuann%2FAwesome-IntelligentCarRace?ref=badge_small){:target="\_blank"}

同时项目提供了详尽的项目代码文档，您可以通过以下链接查看：<https://ittuann.github.io/Awesome-IntelligentCarRace/contribution/scripts>{:target="\_blank"} 该文档由源代码内的信息自动生成，确保了随代码的更新同步保持最新状态。

## 帮助通道

如果您不熟悉上述 Git 等操作，但依然希望为项目补充或修改信息，不用担心，我们为您提供了另外一个途径。

a. 提交 Issue:

- 打开项目的 [Github 仓库页面](https://github.com/ittuann/Awesome-IntelligentCarRace){:target="\_blank"} 。
- 点击 [Issues](https://github.com/ittuann/Awesome-IntelligentCarRace/issues){:target="\_blank"} 页面下的 [New issue](https://github.com/ittuann/Awesome-IntelligentCarRace/issues/new/choose){:target="\_blank"} 按钮。
- 在显示的几个 Issues 模板中，选择 `✨ 提交信息` 。
- 根据模板的提示完成信息的录入。
- 提交 Issue 。

b. 等待反馈:

- 一旦您提交了 Issue，我或其他社区成员会在看到后开始处理。我们会不定期检查并将您提供的信息添加到项目中。
- 同时，您也可以在 Issue 中追踪到我们对您请求的处理情况。

每一个人都可以为项目做出贡献，不论您是否熟悉技术操作。感谢您的参与和支持！
