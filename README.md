# proyuketang-slidesCrawler_inclass

在荷塘雨课堂上课时下载当前课件，以 pdf 格式保存到本地。

## 使用说明

### 1. 配置 `config.json` 文件

进入上课界面，按 `F12` 打开开发者工具，切换到 “网络” 标签页并刷新页面。

找到 `fetch?presentation_id=...` 请求，查看请求标头。先将 `:path` 字段中 `presentation_id=` 之后的内容复制到 `config.json` 文件的对应位置，再将 `authorization` 字段的全部内容复制到 `config.json` 文件的对应位置，最后将 `cookie` 字段中从 `sessionid=` 到最近的分号前的内容复制到 `config.json` 文件的 `sessionid` 项中。

![config](img.jpg)

### 2. 运行程序

确保安装所有依赖后运行该程序。

```
python slides_crawler.py
```

该程序会将当前课件以 pdf 格式保存到当前目录，命名为 `slides.pdf` 。

### 3. 注意事项

注意该程序仅用于获取当前课件，若课堂中放映了多个课件需要分别获取。

## LISENCE

本仓库的内容采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) 许可协议。您可以自由使用、修改、分发和创作衍生作品，但只能用于非商业目的，署名原作者，并以相同的授权协议共享衍生作品。

如果您认为文档的部分内容侵犯了您的合法权益，请联系项目维护者，我们会尽快删除相关内容。
