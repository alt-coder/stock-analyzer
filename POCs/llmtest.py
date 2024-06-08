from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)
from langchain.schema import HumanMessage, SystemMessage
from keys import openAIkey

llm = ChatOpenAI(model= "mistralai/mistral-7b-instruct", openai_api_key = openAIkey, openai_api_base= 'https://openrouter.ai/api/v1'  )
      
# use llm to chat
# define a list of messages in the chat chain
messages = [
    SystemMessage(
        content="You are a helpful assistant who is very good at Go-lang programming language"
    ),
    HumanMessage(
        content='''Hi! How are you?'''
    ),
]

# use the llm object to generate a response to the user's message
ct = llm(messages)
print(ct.content)

