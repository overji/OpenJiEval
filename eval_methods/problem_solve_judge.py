import json

from llm_use.llm import OpenJi_LLM
import re

def standard_output():
    return "{\"gain_score_point\": 得分点,\"final_score\": 最终得分}"

def problem_solve_judge(judge_llm:OpenJi_LLM,
                        standard_answer:str,
                        llm_answer:str,
                        origin_problem:str="",
                        choices=None):
    if choices is None:
        choices = []
    print("正在判题")
    choices_prompt_section = ""
    if len(choices) != 0:
        choices_prompt_section = (f"下面是这个选择题的选项，用户的答案必须是这四个选项中的一个，"
                                  f"和四个选项中的一个选项表达的意思相同就可以认为选择了这个选项，"
                                  f"如果和四个选项意思均不同就直接给出零分:{choices}\n\n")
    prompt = (f"下面我会给出一道题目的标准答案和用户给出的答案，你需要根据这个标准答案，分析用户给出的这个答案是否正确"
              f"首先是标准答案:{standard_answer}\n\n"
              f"随后是我给出的答案:{llm_answer}\n\n"
              f"{choices_prompt_section}"
              f"请逐一给出给分点，最终给出最终得分，最终得分必须在0-100之间，0表示题目解答错误，"
              f"如果解答正确，那么得分应当在60-100分之间，60分表示只有答案，80分表示解答与标准解答在方法、过程上完全不同，100分表示解答与标准解答在方法、过程上完全相同，注意给分有理有据\n\n"
              f"如果标准解答只给出了解答结果，那么只要其他大模型的解答正确，就给出100分\n\n"
              f"注意只需要对我给出的答案进行评分，不需要对标准答案进行评分，除了要求格式之外不要有多余的解释\n\n"
              f"请按照以下格式给出你的评分:{standard_output()},在这个格式中，gain_score_point表示得分点，final_score表示最终得分。最终得分只要一个数字")
    judge_response = judge_llm.send_message(prompt)
    final_score = 0
    print(judge_response)
    # 正则表达式提取分数
    pattern = r'"final_score":\s*(\d+)'

    match = re.search(pattern, judge_response)
    if match:
        final_score = int(match.group(1))
        print(f"final_score: {final_score}\n")
    else:
        print("No match found")
    return final_score