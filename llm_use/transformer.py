from transformers import pipeline, Conversation

# 创建聊天机器人管道
chatbot = pipeline("conversational", model="OpenGVLab/InternVL2_5-78B", trust_remote_code=True)

# 创建对话对象
conversation = Conversation("你好！你是谁？")

# 生成回复
response = chatbot(conversation)

# 打印回复
print(response.generated_responses[-1])