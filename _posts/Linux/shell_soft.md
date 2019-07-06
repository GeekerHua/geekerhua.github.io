---
title: 常用的shell下的工具
date:  2019/7/6  下午11:03:07
tags: [shell]
categories: [Linux满汉全席]
---

## pandoc-文件转换

### 从HTML格式转换为reStructuredText格式

```bash
pandoc -t rst myFile.html -o myFile.rst
```

## ffmpeg-音视频转换

[ffmpeg-官方链接](https://ffmpeg.org/ffmpeg.html)

### 使用FFmpeg把一个AVI格式的视频文件转换为一个Ogg格式的视频文件

```bash
ffmpeg -i myVideo.avi myvideo.ogg
```

## LibreOffice-工作文档转换

[Home | LibreOffice - Free Office Suite - Fun Project - Fantastic People](http://libreoffice.org/)

### 使用LibreOffice把一组幻灯片转换成PDF， 你可以使用如下命令行内容：

```bash
soffice --headless --convert-to pdf mySlides.odp
```

### 将某文件夹中所有的微软Word文档转换为LibreOffice Writer文件格式

```bash
soffice --headless --convert-to odt *.docx
```

