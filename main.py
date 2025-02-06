from typing import List

from llm_use.llm import OpenJi_LLM
from llm_use.load_llms import load_llms

if __name__ == '__main__':
    llms:List[OpenJi_LLM] = load_llms()
    print(llms)