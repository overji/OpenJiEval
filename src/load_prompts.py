import json
import os.path
from typing import List


def prompts_dir()->str:
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"tests","prompts.json")
    return path

def get_prompts_list()->List[dict]:
    path:str = prompts_dir()
    with open(path,encoding='utf-8') as f:
        return json.load(f)
