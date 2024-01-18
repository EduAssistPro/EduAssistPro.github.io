---
title: 【算法与数据结构】FIT2004 Assignment
date: 2024-01-03
categories: 算法与数据结构
tags: [算法与数据结构,Python]
img_path: /assets/img/
---


时间
====

**2023年10月20日**

关键词
======

**算法与数据结构，Python，FIT2004，网络流，字典树**

课程信息
========

**莫纳什大学-数据结构与算法-FIT2004**

客户需求
========

两道算法题目，第一题是关于字典树的，第二题是关于网络流的。

1.  需要给出python代码实现，不能使用map、set等数据结构，只能使用list。

2.  需要编写测试用例来保证代码的鲁棒性。老师提供了少量测试用例，需要设计额外的测试用例来保证算法在各个情况下都能work。

3.  需要写详细文档介绍代码设计和分析复杂度

4.  作业根据**测试用例通过率**+**文档详细程度**
    算分**，**客户希望尽量拿到90分以上（满分100）。

![descript](【算法与数据结构】FIT2004 Assignment_media/media/image1.png)

![descript](【算法与数据结构】FIT2004 Assignment_media/media/image2.png)

![descript](【算法与数据结构】FIT2004 Assignment_media/media/image3.png)

辅导过程
========

代码实现+网络流建模
-------------------

第一题相对简单，用python实现字典树已经很熟练了。

第二题就想对困难许多。这并不是一个常见的网络流题目，需要通过建模将题目条件转换为网络流模型。这个建模花费了较长时间。

为了让同学理解建模过程，专门做了PPT给同学讲解。把原始问题一步步拆解转换为网络流的Max-flow问题求解。

![descript](【算法与数据结构】FIT2004 Assignment_media/media/image4.png)

![descript](【算法与数据结构】FIT2004 Assignment_media/media/image5.png)

下面是我们做的讲解PPT

![descript](【算法与数据结构】FIT2004 Assignment_media/media/image6.png)

测试用例构造
------------

为了保证能拿90分，编写了大量的测试用例进行测试，把各种边边角角的条件都覆盖了

大概第一题 约20个测试用例，第二题约50个测试用例。

文档编写
--------

由于最后打分还需要根据文档详细程度打分，为了能拿高分，文档也是尽可能的多写一点

![descript](【算法与数据结构】FIT2004 Assignment_media/media/image7.png)

客户评价与满意度
================

最后拿到满分

![descript](【算法与数据结构】FIT2004 Assignment_media/media/image8.png)
