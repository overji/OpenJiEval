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

### 3. eval_methods
一些用于评价大模型输出质量的工具  
|  
|- problem_solve_judge.py:评价题目  
|  
|- similarity_check.py:评价两段文字相似度  

### 4. secrets
用于存放大模型的名称、url、api_key  
|  
|- judge_secret.py:用于判题的大模型  
|  
|- secret.py:待评测的大模型  

编写标准:  
judge_secret.json:   
```json
{
    "model_name": "大模型名称",
    "model_secret": "大模型的apikey",
    "model_baseUrl": "大模型的url地址"
}
```
    
secret.json:
```json
[
  {
    "model_name": "大模型名称",
    "model_secret": "大模型的apikey",
    "model_baseUrl": "大模型的url地址",
    "is_multimodal": (0或1 -> 是否为多模态模型)
  },
]
```
每个大模型一条json对象，形成一个列表  
**⭐在使用前务必确保这两个文件都存在并且所有内容均被填写⭐**

### 5.tests
用于存放待评测的prompt  
|  
|- prompts.json: 待评测的prompts  

编写标准:  
promnpts.json:  
```json
[
  {
    "prompt_type": "prompt类型",
    "prompt": "prompt内容",
    "is_multimodal": (0或1 -> 是否用于多模态模型)
  }
]
```  
每个大模型一条json对象，形成一个列表  

### 6.logs
评测前请自行创建这个文件夹

