from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3")

template = """
You are an expoert in answering questions about a pizza restaurant.

Here are some relevant reviews: {reviews}

Here is the question to answer: {question}

"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n\n--------------------------------\n\n\n")
    question = input("Enter a question (q to quit): ")
    print("\n\n\n--------------------------------\n\n\n")
    if question.lower() == "q":
        break   
    result = chain.invoke({
        "reviews": [],
        "question": question
    })
    print(result)