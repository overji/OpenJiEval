# OpenJiEval——一个大模型自动评测工具
## 思路介绍
首先由大模型根据prompt，生成对题目的答案，然后交由评测大模型进行评分。
***
## 各模块介绍
### 1.llm_use
用于大模型的调用，大模型相关内容在secrets文件夹中
|
|-llm.py:大模型实例对象
|
|-load_llms.py:批量加载所有大模型

### 2.src
|
|-get_training_set.py:获取训练集
|
|-test_llms:获取用于评测的大模型实例
|
|-utils.py: 一些有用的函数

