# Zhihao Zhu 个人主页维护说明

这个仓库发布到：

```text
https://zzh9568.github.io/
```

当前版本是一个很小的静态个人主页仓库，只公开一般个人主页需要的信息。

## 当前公开内容

仓库主要包含：

| 内容 | 文件 |
| --- | --- |
| 首页 | `index.html` |
| Research 页面 | `research/index.html` |
| CV PDF | `documents/CV.pdf` |
| CV 生成脚本 | `scripts/make_cv.py` |
| GitHub Pages 部署 workflow | `.github/workflows/pages.yml` |

已经删除模板示例文章、talks、teaching、portfolio、示例 PDF、模板 CV、模板头像、本地预览页、大 PDF 等无关内容。

## 首页怎么改

首页直接改：

```text
index.html
```

常见修改位置：

- 顶部个人简介：搜索 `I study trustworthy AI`
- 侧边栏简介：搜索 `Postdoctoral Fellow at HKUST`
- Research Focus：搜索 `Research Focus`
- 首页缩略论文：搜索 `Selected Publications`
- About 简介：搜索 `<h2>About</h2>`

`AI for Finance` 目前没有显示。如果以后要加回这块内容，可以在 `Research Focus` 区域新增一张卡片。

## Research 页面怎么改

完整研究页面直接改：

```text
research/index.html
```

常见修改位置：

- 研究方向：搜索 `Research Interests`
- 已发表/录用论文：搜索 `Selected Publications`
- Working papers：搜索 `Working Papers`
- Awards：搜索 `Awards`

## CV 怎么换

当前 CV 链接指向：

```text
documents/CV.pdf
```

最简单的更新方式：

1. 用新的 PDF 覆盖 `documents/CV.pdf`
2. 文件名保持 `CV.pdf`

如果想重新生成当前格式的 CV，可以修改：

```text
scripts/make_cv.py
```

然后运行：

```powershell
python scripts\make_cv.py
```

如果系统里的 `python` 不可用，可以使用 Codex runtime 或任意安装了 `reportlab` 的 Python。

## 头像照片

当前页面使用 `ZZ` 文字头像，没有公开真实照片。

如果以后要添加头像：

1. 把照片放到 `images/`，例如 `images/profile.jpg`
2. 在 `index.html` 和 `research/index.html` 里搜索：

```html
<div class="avatar">ZZ</div>
```

3. 替换成：

```html
<img class="avatar" src="/images/profile.jpg" alt="Zhihao Zhu">
```

可能还需要在 CSS 里给 `.avatar` 保持圆形样式。

## 邮箱、Scholar、ORCID、GitHub 怎么改

需要同时检查这两个文件：

```text
index.html
research/index.html
```

搜索以下关键词即可定位：

- `zhihaozhu@ust.hk`
- `Google Scholar`
- `ORCID`
- `github.com/zzh9568`

## 部署方式

仓库使用 GitHub Actions 发布静态文件。Workflow 是：

```text
.github/workflows/pages.yml
```

它会把以下内容复制到 GitHub Pages artifact：

- `index.html`
- `research/index.html`
- `documents/CV.pdf`

所以公开网页只包含这几个页面/文件。

## 上传前检查

上传前建议确认：

1. `index.html`
2. `research/index.html`
3. `documents/CV.pdf`
4. `scripts/make_cv.py`
5. `.github/workflows/pages.yml`

不要提交私人文件、草稿、审稿材料、模板作者文件、临时 Office 文件或本地截图。
