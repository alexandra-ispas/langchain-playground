from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser, JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
model = ChatOpenAI(
    model="gpt-3.5-turbo-1106", temperature=0.7
)


def call_string_output_parser():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Tell me a joke about the following subject"),
        ("human", "{input}")
    ])

    parser = StrOutputParser()

    chain = prompt | model | parser

    return chain.invoke({
        "input": "dog"
    })


def call_list_output_parser():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Generate a list of 10 synonyms for the following subject. Return the list as comma separated "
                   "values."),
        ("human", "{input}")
    ])

    parser = CommaSeparatedListOutputParser()

    chain = prompt | model | parser

    return chain.invoke({"input": "happy"})


def call_json_output_parser():
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Generate a JSON representation of the following subject.\nFormatting instructions: {"
                   "format_instructions}"),
        ("human", "{phrase}")
    ])

    class Person(BaseModel):
        name: str = Field(description="The name of the person.")
        age: int = Field(description="The age of the person.")

    parser = JsonOutputParser(pydantic_object=Person)

    chain = prompt | model | parser

    return chain.invoke({"phrase": "Max is 30 years old.", "format_instructions": parser.get_format_instructions()})


print(call_string_output_parser()) # the response is now ot type String
