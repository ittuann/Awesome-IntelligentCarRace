# 提交指南

!!! note "提交前请注意"

    在提交 [Pull Request](https://github.com/ittuann/Awesome-IntelligentCarRace/pulls){:target="\_blank"} 前，请仔细阅读本提交引导文档。

    请确保您的提交不会引入任何错误，并且已经经过了测试。

    如果您不熟悉下面 Git 等操作，请查看[帮助通道](https://ittuann.github.io/Awesome-IntelligentCarRace/contribution/#_5)。

提交信息只需两个步骤：1.[向表格中增加信息](https://ittuann.github.io/Awesome-IntelligentCarRace/contribution/#_2) -> 2.[测试添加后的效果](https://ittuann.github.io/Awesome-IntelligentCarRace/contribution/#_3)

如果您已添加了信息但没有在本地测试添加后的效果，请在 Pull Request 内明确注明。您也可以考虑直接使用[帮助通道](https://ittuann.github.io/Awesome-IntelligentCarRace/contribution/#_5)内提交 issue 的方式进行信息的补充。

## 向表格中增加信息

首先，请登录您的 Github 账号。打开本项目的仓库链接: <https://github.com/ittuann/Awesome-IntelligentCarRace>{:target="\_blank"} ，然后在页面的右上角点击 `Fork` 按钮，以便将本仓库分支到您的个人账号。

确保您已经克隆了最新版本的仓库，并且在正确的 [main](https://github.com/ittuann/Awesome-IntelligentCarRace/tree/main){:target="\_blank"} 分支上进行操作。

想要在表格中添加新的内容，仅需要直接修改项目**根目录**的 [table.csv](https://github.com/ittuann/Awesome-IntelligentCarRace/blob/main/table.csv){:target="\_blank"}。

在 [table.csv](https://github.com/ittuann/Awesome-IntelligentCarRace/blob/main/table.csv){:target="\_blank"} 表格的最后一行后追加新的一行条目，即可完成信息的添加。请确保您提交的数据格式正确，并与表单内现有条目保持一致。

## 测试添加后的效果

测试添加信息后的网页效果，则首先需要安装 Python 环境和依赖。在项目的根目录中，运行以下命令来安装必要的依赖：

```python
pip install -r requirements.txt
```

然后运行脚本，生成筛选后的各个分表：

```python
python ./scripts/split.py
```

执行以下命令来在本地运行和测试项目：

```shell
mkdocs serve
```

如果在运行项目过程中没有出现任何报错，那就代表您成功地完成了增加信息后的测试。您也可以在本地浏览打开`http://127.0.0.1:8000/Awesome-IntelligentCarRace/`查看效果。

## 提交更改

在确认所有更改都正常工作后，您可以将更改提交到您的分支，并创建一个 [Pull Request](https://github.com/ittuann/Awesome-IntelligentCarRace/pulls){:target="\_blank"}

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
