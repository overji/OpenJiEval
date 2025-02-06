import json

from llm_use.llm import OpenJi_LLM
import re

def standard_output_format():
    return "{\"similarity\": 你的评价值}"

def similarity_check(judge_llm:OpenJi_LLM,
                     standard_output:str,
                     llm_output:str):
    """
    This function is used for check similarity between two sentence(or paragraph) using LLM
    :param judge_llm: A instance of OpenJi_LLM, used for judge similarity
    :param standard_output: the standard output
    :param llm_output: the output from LLM
    :return: A int between 0 and 100, representing the similarity between two sentence(or paragraph)
    """

    print("正在进行相似度检测")
    prompt = (f"下面会给出两个句子A和B，第一个句子A是标准输出，第二个句子B是模型输出\n\n{standard_output}\n\n{llm_output}\n\n"
              f"请判断句子B与句子A的相似度，相似度范围为0-100，0为完全不相似，100为完全一致\n"
              f"输出格式为{standard_output_format()}")
    response = judge_llm.send_message(prompt)
    print(response[2]['content'])
    matchJson = re.search(r'"similarity": (\d+)', response[2]['content'])
    if matchJson:
        print(f"相似度为{matchJson.group(1)}")
        return int(matchJson.group(1))