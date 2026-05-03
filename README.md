# Zhihao Zhu 个人主页维护说明

这个仓库是我的学术个人主页源码，使用 Jekyll + Minimal Mistakes / academicpages 主题。

## 常用修改位置

以后大部分内容只需要改下面几个文件：

| 想修改的内容 | 修改文件 |
| --- | --- |
| 首页介绍、研究方向卡片、首页论文缩略列表、短个人简介 | `_pages/about.md` |
| Research 页面、完整论文列表、working papers、awards | `_pages/research.md` |
| 姓名、侧边栏简介、邮箱、GitHub、Google Scholar、ORCID、地点 | `_config.yml` |
| 顶部导航栏 | `_data/navigation.yml` |
| 页面样式、颜色、卡片、按钮、排版 | `assets/css/main.scss` |
| 页脚文字 | `_includes/footer.html` |
| 侧边栏头像显示逻辑 | `_includes/author-profile.html` |

## 首页怎么改

首页内容在：

```text
_pages/about.md
```

里面几个重要区域：

- `home-hero`：首页最上方的大标题、研究简介、按钮。
- `Research Focus`：首页的研究方向卡片。
- `Selected Publications`：首页显示的缩略论文列表。
- `About`：首页底部的短个人介绍。

目前 `AI for Finance` 这张研究方向卡片已经被注释掉了，因为现在还没有对应论文。以后如果想恢复：

1. 打开 `_pages/about.md`
2. 搜索 `AI for Finance`
3. 找到外面的 `<!--` 和 `-->`
4. 删除这两个注释标记即可恢复显示

如果你以后保留本地草稿预览文件，也可以在那里同步恢复；公开发布仓库里不保留预览页。

## Research 页面怎么改

完整 Research 页面在：

```text
_pages/research.md
```

这里适合放完整学术信息，包括：

- 研究简介
- 研究兴趣
- 完整已发表/录用论文列表
- Working papers
- Under review 状态
- Awards

首页只放缩略版，完整记录放 Research 页。

## 头像照片怎么换

现在主页使用的是 `ZZ` 文字头像，没有启用真实照片。

以后如果要加自己的照片：

1. 把照片放到 `images/` 文件夹，例如：

```text
images/profile.jpg
```

2. 打开 `_config.yml`
3. 找到 `author:` 下面的 `avatar`
4. 改成：

```yml
author:
  avatar: "profile.jpg"
```

注意：当前仓库里的 `images/profile.png` 看起来像原模板作者的照片，不建议直接使用，除非确认那是你自己的照片。

## CV 怎么换

当前 CV 链接指向：

```text
documents/CV.pdf
```

以后更新 CV 最简单的方法：

1. 用新的 PDF 覆盖 `documents/CV.pdf`
2. 文件名保持 `CV.pdf`

这样不需要改任何链接。

如果你想换成别的文件名，比如 `Zhihao_Zhu_CV.pdf`，需要同步修改：

- `_pages/about.md`
- `_data/navigation.yml`

## 邮箱、Scholar、ORCID、GitHub 怎么改

这些信息主要在：

```text
_config.yml
```

重点看这个区域：

```yml
author:
  name:
  bio:
  location:
  googlescholar:
  orcid:
  email:
  github:
```

本地 in-app browser 有时打不开 `mailto:` 邮件链接，这是浏览器/系统没有绑定邮件客户端导致的，不是网页问题。现在页面会直接显示邮箱地址，方便复制。

## 顶部导航栏怎么改

导航栏文件是：

```text
_data/navigation.yml
```

当前有：

- Home
- Research
- CV

以后新增页面后，再来这里加导航入口。

## 样式怎么改

主要样式文件是：

```text
assets/css/main.scss
```

我新增的自定义样式从这行开始：

```scss
/* Custom academic homepage refresh */
```

这里控制：

- 页面主色
- 首页按钮
- Research Focus 卡片
- 论文卡片
- 侧边栏文字头像
- 响应式布局

## 本地 Jekyll 预览

如果以后安装了 Ruby 和 Bundler，可以在项目目录运行：

```powershell
bundle install
bundle exec jekyll serve
```

然后打开：

```text
http://127.0.0.1:4000/
```

上传到 GitHub 后，GitHub Pages 会自动构建正式网页。

## 上传到 GitHub

你的仓库 SSH 地址是：

```text
git@github.com:zzh9568/zzh9568.github.io.git
```

如果当前目录还不是 Git 仓库，可以运行：

```powershell
cd "C:\Users\Lenovo\Desktop\个人主页\zzh9568.github.io-publish"

git init
git branch -M master
git remote add origin git@github.com:zzh9568/zzh9568.github.io.git

git add .
git commit -m "Refresh homepage design"

git pull --rebase origin master --allow-unrelated-histories
git push -u origin master
```

如果远程仓库默认分支是 `main`，把上面所有 `master` 改成 `main`。

## 上传前检查

上传前建议看一遍：

1. `_pages/about.md`
2. `_pages/research.md`
3. `_config.yml`
4. `documents/CV.pdf`
5. `README.md`

确认没问题后再 `git add .`、`git commit`、`git push`。
