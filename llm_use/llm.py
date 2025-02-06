import json

from openai import OpenAI

class OpenJi_LLM:
    def __init__(self,
                 model_name:str,
                 model_base_url:str,
                 model_api_key:str,
                 is_multimodal:bool = False):
        self.model_name = model_name
        self.llm = OpenAI(api_key=model_api_key,base_url=model_base_url)
        self.is_multimodal = is_multimodal

    def send_message(self,
                                  user_prompt: str,
                                  image_url: str = "",
                                  system_message: str = "",
                                  temperature: int = 0.1,
                                  ):
        """
        标准的大模型调用接口
        :param user_prompt: 用户的prompt
        :param image_url: 图片链接，可以不写
        :param system_message: 系统信息
        :param temperature: 大模型的temperature
        :return: 返回大模型输出的内容，注意不是流式输出
        """
        if (not self.is_multimodal) or image_url == "":
            #如果模型不是多模态，就返回非多模态情况下的结果
            return self.send_message_no_picture(user_message=user_prompt,
                                                system_message=system_message,
                                                temperature=temperature)
        response = self.llm.chat.completions.create(
            model=self.model_name,
            messages=[{
                'role':
                    'user',
                'content': [{
                    'type': 'text',
                    'text': user_prompt,
                }, {
                    'type': 'image_url',
                    'image_url': {
                        'url':image_url
                    },
                }],
            }],
            stream=False
        )
        return (response.choices[0].message.content)

    def send_message_no_picture(self,
                     user_message:str,
                     system_message:str = "",
                     temperature:int=0.1):
        #返回值是本次对话的json
        my_message = [
            {
                "role": "system",
                "content": system_message
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
        response = self.llm.chat.completions.create(
            model = self.model_name,
            messages=my_message,
            stream=False,
            temperature=temperature
        )
        returned_message = response.choices[0].message.content
        my_message.append({
            "role":"assistant",
            "content":returned_message
        })
        return my_message




