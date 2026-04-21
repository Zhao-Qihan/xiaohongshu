from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser

from prompt_template import xiaohongshu_template, user_template
from xiaohongshu_model import Xiaohongshu

def generate_xiaohongshu(subject, api_key):
    prompt = ChatPromptTemplate.from_messages([
        ("system", xiaohongshu_template),
        ("human", user_template)
    ])

    model = ChatOpenAI(model="qwen-plus",
                       openai_api_key=api_key,
                       openai_api_base="https://dashscope.aliyuncs.com/compatible-mode/v1")

    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)
    parser_instructions = output_parser.get_format_instructions()

    chain = prompt | model | output_parser
    result = chain.invoke({"parser_instructions": parser_instructions, "subject": subject})
    return result
