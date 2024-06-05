from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(
    model = "gpt-3.5-turbo",
    temperature = 0,   # answer qs factually
    max_tokens = 100,
    verbose = True,
)

# response = llm.invoke("hello! how are you?")


# response = llm.batch(["hello! how are you?", "write a poem about AI"])
# batch questions are running in parallel


response = llm.stream("hello! how are you?")
for chunk in response:
    print(chunk.content, end="", flush=True)


# print(response)
