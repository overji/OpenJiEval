import json
import os

from llm_use.load_llms import load_llms
from llm_use.llm import OpenJi_LLM
from eval_methods.problem_solve_judge import problem_solve_judge
import src.logger as logger

class testLLM:
    def __init__(self):
        self.llms = load_llms()
        try:
            self.judge_llm = self.build_judge_llm()
        except Exception as e:
            logger.error(e.__str__())
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

