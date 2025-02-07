import logging
from typing import List
from src.get_training_set import get_training_data
from llm_use.llm import OpenJi_LLM
from llm_use.load_llms import load_llms
from src.test_llms import testLLM
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("output.log", encoding='utf-8'),
                        logging.StreamHandler()
                    ])

def test_llm_main(df: pd.DataFrame, llm: OpenJi_LLM, testLLM: testLLM, final_count: list):
    final_score = 0
    if llm.is_multimodal:
        for index, row in df.iterrows():
            try:
                if index < 45:
                    continue
                logging.info(f"本次题目{row['id']},图片路径:{row['image']},目标答案:{row['answer']},题目选项:{row['options']}")
                message = llm.send_message("帮我解答一下这个题目，尽可能地简洁，并且只需要返回答案，不要有多余的过程",
                                           f"http://112.124.43.86/problems/images/{row['image']}",
                                           "你是一个数学高手")
                logging.info(message)
                score = testLLM.test_problem(message, row['answer'], row['options'])
                final_score += (score / 100)
                logging.info(f"本次得分:{score},现在总得分{final_score}")

            except Exception as e:
                logging.error(e)
                continue
    return final_score

if __name__ == '__main__':
    llms: List[OpenJi_LLM] = load_llms()
    tester = testLLM()
    logging.info(f"大模型加载完成")
    final_count = []
    df = get_training_data()
    logging.info(f"训练数据加载完成")
    for llm in llms:
        final_score = test_llm_main(df, llm, tester, final_count)
        final_count.append((llm.model_name, final_score))
    logging.info(f"最终评价{final_count}")