from typing import List
from src.get_training_set import get_training_data
from llm_use.llm import OpenJi_LLM
from llm_use.load_llms import load_llms
from src.test_llms import testLLM
from src.load_prompts import get_prompts_list
import src.logger as logger
import pandas as pd



def test_llm_main(df: pd.DataFrame, llm: OpenJi_LLM, testLLM: testLLM, final_count: list,prompts:List[dict]):
    final_scores = []
    if llm.is_multimodal:
        for prompt_json in prompts:
            prompt_score = 0
            if prompt_json["is_multimodal"]:
                logger.info(f"本次测试的大模型为{llm.model_name},多模态:{bool(llm.is_multimodal)},prompt:\"{prompt_json["prompt"]}\",prompt类型:{prompt_json["prompt_type"]}")

                for index, row in df.iterrows():
                    try:
                        logger.info(f"本次题目{row['id']},图片路径:{row['image']},目标答案:{row['answer']},题目选项:{row['options']}")
                        message = llm.send_message(prompt_json["prompt"],
                                                   f"http://112.124.43.86/problems/images/{row['image']}",
                                                   "你是一个数学高手")
                        logger.info(f"大模型答案:{message}")
                        score = testLLM.test_problem(message, row['answer'], row['options'])
                        prompt_score += (score / 100)
                        logger.info(f"本次得分:{score},现在总得分{prompt_score}")

                    except Exception as e:
                        logger.error(e.__str__())
                        continue
                final_scores.append({prompt_json["prompt_type"]:prompt_score})
    return final_scores

if __name__ == '__main__':
    llms: List[OpenJi_LLM] = load_llms()
    tester = testLLM()
    logger.info(f"大模型加载完成")
    final_count = []
    df = get_training_data()
    logger.info(f"训练数据加载完成")
    prompts = get_prompts_list()
    logger.info(f"prompts加载完成")
    for llm in llms:
        final_score = test_llm_main(df, llm, tester, final_count,prompts)
        final_count.append({llm.model_name:final_score})
    logger.info(f"最终评价{final_count}")