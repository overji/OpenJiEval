import json
import os
from typing import List
from llm_use.llm import OpenJi_LLM

def load_llms() -> List[OpenJi_LLM]:
    diction = []
    llms: List[OpenJi_LLM] = []
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)),"secrets","secret.json"), "r") as f:
        diction = json.load(f)
    if diction != []:
        for llm_use in diction:
            model_name = llm_use['model_name']
            model_secret = llm_use['model_secret']
            model_baseUrl = llm_use['model_baseUrl']
            is_multimodal = llm_use['is_multimodal']
            llm = OpenJi_LLM(model_name=model_name,
                             model_base_url=model_baseUrl,
                             model_api_key=model_secret,
                             is_multimodal=is_multimodal)
            llms.append(llm)
    return llms