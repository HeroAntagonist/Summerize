from langchain.document_loaders import WebBaseLoader
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains.summarize import load_summarize_chain
from dotenv import load_dotenv
import time
import random 

load_dotenv()

def type_out(message):
    for char in message:
        rand_Num = random.uniform(.005,.05)
        time.sleep(rand_Num)
        yield char

def summerize_web(url):
    loader = WebBaseLoader(url)
    docs = loader.load()
    #Remember to set env var for openai token #OPENAI_API_KEY=""
    llm = ChatOpenAI(temperature=0, model='gpt-3.5-turbo-16k') 
    chain = load_summarize_chain(llm, chain_type="stuff", verbose=False)
    return (chain.run(docs))

def summerize_page():
    try:
        [print(x,end="", flush=True) for x in type_out("Please enter a url... ")]
        for i in type_out(summerize_web(input())):
            print(i, end="", flush=True)
        print(' ')
        print(' ')
    except:
        print('The URL you entered does not appear to be valid')

while True:
    summerize_page()
    user_input = input("Do you want to summerize another webpage (yes/no):")
    if user_input.lower() not in ('yes', 'y'):
        print("Exiting the script...")
        break 





