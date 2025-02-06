import json

from llm_use.llm import OpenJi_LLM
import re

def standard_output():
    return "{\"gain_score_point\": 得分点,\"final_score\": 最终得分}"

def problem_solve_judge(judge_llm:OpenJi_LLM,
                        origin_problem:str,
                        standard_answer:str,
                        llm_answer:str):
    prompt = (f"下面我会给出一道题目，你需要根据这个标准答案，分析我给出的这个答案是否正确"
              f"首先是题目:{origin_problem}\n\n"
              f"其次是标准答案:{standard_answer}\n\n"
              f"最后是我给出的答案:{llm_answer}\n\n"
              f"请逐一给出给分点，最终给出最终得分，最终得分必须在0-100之间，0表示题目解答错误，"
              f"如果解答正确，那么得分应当在60-100分之间，60分表示只有答案，80分表示解答与标准解答在方法、过程上完全不同，100分表示解答与标准解答在方法、过程上完全相同，注意给分有理有据\n\n"
              f"注意只需要对我给出的答案进行评分，不需要对标准答案进行评分，除了要求格式之外不要有多余的解释\n\n"
              f"请按照以下格式给出你的评分:{standard_output()},在这个格式中，gain_score_point表示得分点，final_score表示最终得分。最终得分只要一个数字")
    judge_response_json = judge_llm.send_message(prompt)[2]["content"]
    final_score = 0
    print(judge_response_json)
    # 正则表达式提取分数
    pattern = r'"final_score":\s*(\d+)'

    match = re.search(pattern, judge_response_json)
    if match:
        final_score = int(match.group(1))
        print(f"final_score: {final_score}\n")
    else:
        print("No match found")
    return final_score