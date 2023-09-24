# 提交指南

!!! note "提交前请注意"

    在提交 [Pull Request](https://github.com/ittuann/Awesome-IntelligentCarRace/pulls){:target="\_blank"} 前，请仔细阅读本提交引导文档。

    请确保您的提交不会引入任何错误，并且已经经过了测试。

## 向表格中增加信息

确保您已经克隆了最新版本的仓库，并且在正确的 [main](https://github.com/ittuann/Awesome-IntelligentCarRace/tree/main) 分支上进行操作。

想要在表格中添加内容，请直接修改项目根目录的 [table.csv](https://github.com/ittuann/Awesome-IntelligentCarRace/blob/main/table.csv) 。请确保您的数据格式正确并与其他数据条目保持一致。

## 测试添加后的效果

首先需要安装依赖。在项目的根目录中，运行以下命令来安装必要的环境：

```python
pip install -r requirements.txt
```

然后运行脚本，生成筛选后的各个分表

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

## 寻求帮助

这是一个很好的建议，因为这样可以鼓励那些不熟悉 Git 的用户也能够为项目做出贡献。以下是完善后的文本：

---

## 寻求帮助

如果您不熟悉 Git 的操作，但依然希望为项目补充或修改信息，不用担心，我们为您提供了另外一个途径。

1. 提交 Issue:

   - 打开项目的 [Github Issues 页面](https://github.com/ittuann/Awesome-IntelligentCarRace/issues){:target="\_blank"}。
   - 点击 "New Issue" 按钮。
   - 在标题中简短描述您想要补充或修改的内容。
   - 在详情描述中，详细列出您想要添加或修改的信息，并且请附上信息来源或参考链接。
   - 提交 Issue。

2. 等待反馈:
   一旦您提交了 Issue，我或其他社区成员会在看到后开始处理。我们会不定期检查并将您提供的信息添加到项目中。同时，您也可以在 issue 中追踪到我们对您请求的处理情况。

每一个人都可以为项目做出贡献，不论您是否熟悉技术操作。我们感谢您的参与和支持！
