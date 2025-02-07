import json
import os

from eval_methods.similarity_check import similarity_check
from llm_use.load_llms import load_llms
from llm_use.llm import OpenJi_LLM
from eval_methods.problem_solve_judge import problem_solve_judge
from src.utils import get_all_json_files

class testLLM:
    def __init__(self):
        self.llms = load_llms()
        try:
            self.judge_llm = self.build_judge_llm()
        except Exception as e:
            print(e)
            self.judge_llm = None

    def build_judge_llm(self):
        secretDir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "secrets","judge_secret.json")
        with open(secretDir, "r") as f:
            diction = json.load(f)
        if diction != []:
            model_name = diction['model_name']
            model_secret = diction['model_secret']
            model_baseUrl = diction['model_baseUrl']
            i_judge_llm = OpenJi_LLM(model_name=model_name, model_base_url=model_baseUrl, model_api_key=model_secret)
            return i_judge_llm
        else:
            raise Exception("Fail to load judge llm")

    def test_problem(self,
                     llm_output:str,
                     standard_answer:str,
                     choices=None):
        if choices is None:
            choices = []
        return problem_solve_judge(judge_llm=self.judge_llm,
                                llm_answer=llm_output,
                                standard_answer=standard_answer,
                                choices=choices)

    def load_problem_test(self):
        #这个，不需要了
        testsDir = os.path.join(os.path.dirname(os.path.dirname(__file__)),"tests")
        all_test_jsons = get_all_json_files(testsDir)
        to_be_tested_jsons = []
        answer = []
        for j in all_test_jsons:
            with open(os.path.join(testsDir, j), 'r', encoding='utf-8') as f:
                dic = json.load(f)
                if(dic["judge_method"] == "problem_solve"):
                    for js in get_all_json_files(os.path.join(testsDir,dic["files_dir"])):
                        to_be_tested_jsons.append(os.path.join(testsDir,dic["files_dir"],js))
        for test_json in to_be_tested_jsons:
            with open(test_json, 'r', encoding='utf-8') as f:
                f_json = json.load(f)
                question = f_json["question"]
                standard_answer = f_json["standard_answer"]
                llm_answer = f_json["llm_answer"]
                print(f"正在评价{test_json}")
                answer.append(problem_solve_judge(self.judge_llm,question,standard_answer,llm_answer))
        return answer

