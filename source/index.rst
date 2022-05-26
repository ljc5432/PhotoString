.. PhotoString documentation master file, created by
   sphinx-quickstart on Thu May 26 13:44:44 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Lab2:Using Blueprints to Architect A Photo Album Web Application
======================================
小组成员：
'''''''''
201931990526   楼吉诚
^^^^^^^^^^^^^
201931990524   李远帆
^^^^^^^^^^^^^
201931990523   李森特
^^^^^^^^^^^^^
201931990521   康净焮
^^^^^^^^^^^^^
201931990528   潘林鑫
^^^^^^^^^^^^^

Abstract
--------

重构 PhotoString 项目的代码，使用Flask中的Blueprint进行模块化管理

Introduction
------------

A former student developed a web photo album called Photo String for storing photos. He used the Flask
micro web framework. Photo String allows the user to upload a picture and add a description for that
picture. For simplicity, he omitted the user authentication part.
In this lab, you are going to use blueprints to refactor Photo String and add a few small features. Never
heared of blueprints? Read this online tutorial.
Your task in this lab is described as follows.

1.Download the source code of Photo String and run it.
2.Make the following blueprints: upload bp, show bp, search bp, and api bp.
3.Register the above blueprints to the web application.
4.The upload bp blueprint allows uploading a new photo. The associated route is /upload.
5.The show bp blueprint allows displaying all photos and their descriptions in chronological order. The
associated route is /show.
6.The search bp blueprint allows filtering photos according to their descriptions. The associated route
is /search/query-string. Only the photos whose descriptions match query-string will be returned
as the search result.
7.The api bp blueprint allows getting all photo information in JSON format from command-line. HTTPie
is a useful API testing tool. The associated route is /api/json. The returned json string must contain
photo ID, date of upload, photo size (in KB) and photo description for each photo

Methods and materials
---------------------

①HttPie：是一个命令行 HTTP 客户端，拥有直观的界面，支持 JSON、语法高亮、下载功能（类似 wget）、插件支持等特性。

Results
-------


视频链接：

参考文章链接表：
蓝图(Blueprint)详解： https://www.cnblogs.com/wf-skylark/p/9306789.html
Flask 的路由Route详情：https://www.jb51.net/article/230282.htm
flask-url参数：https://blog.csdn.net/weixin_38170137/article/details/101363553
flask学习记录03-json数据类型的接收、转换和返回：https://zhuanlan.zhihu.com/p/425971516

End
~~~
