"""
@Author:shkstart
@Desc: 
"""
# 1、模型的初始化
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
from rich import print as rprint

# 从.env文件中加载环境变量
load_dotenv(override=True)

CLOSEAI_API_KEY = os.getenv("CLOSEAI_API_KEY")
CLOSEAI_BASE_URL = os.getenv("CLOSEAI_BASE_URL")

model = init_chat_model(
    model="gpt-5.4-mini",
    model_provider="openai",
    api_key=CLOSEAI_API_KEY,
    base_url=CLOSEAI_BASE_URL
)

# 2、声明一个函数（工具）
def get_weather(city : str):
    return f"{city}天气晴朗~~"

# 3、将函数绑定在模型上
model_with_tools = model.bind_tools([get_weather])

# 4、调用模型
response = model_with_tools.invoke("北京的天气怎么样")
rprint(response)