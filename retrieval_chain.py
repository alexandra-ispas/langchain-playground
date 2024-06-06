from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.documents import Document
from langchain.chains.combine_documents import create_stuff_documents_chain

docA = Document(
    page_content="lalallalallallalalallalalla"
)

model = ChatOpenAI(
    model="gpt-3.5-1106",
    temperature=0.4,  # lower because we want ot answer questions from a datasource
)

prompt = ChatPromptTemplate.from_template("""
Answer the user's question:
Context: {context}
Question: {input}
""")

# chain = prompt | model

chain = create_stuff_documents_chain( # this should be used for retrieval
    llm=model,
    prompt=prompt
)

response = chain.invoke({
    "input": "What is LCEL?",
    "context": [docA]
})

print(response)
