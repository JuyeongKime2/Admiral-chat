from fastapi import FastAPI, Form
import uvicorn
#from langchain.llms import OpenAI  #랭체인 버전 실행 
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate,SystemMessagePromptTemplate
from langchain.chains import LLMChain
import os

#과제

"""
fastapi 서버생성 127.0.0.1:7001

주소 : /hero

컨셉: 이순신장군 

{'result': 채팅내용}

클라이언트에게 form을 사용하여 chat이라는 키값에 대화를 전송하도록 요청
"""

app = FastAPI()
    

os.environ['OPENAI_API_KEY']='Your_API_KEY'


#1.chatmodel 생성
chat_model = ChatOpenAI(model_name='gpt-4o-mini',temperature=0.1) 

#2. 프롬프트 생성
chat_prompt = ChatPromptTemplate.from_messages(
    
    [
        SystemMessagePromptTemplate.from_template('당신은 이순신 장군입니다. 근엄하고 위엄있는 말투로 후손들에게 알기쉽게 설명해주세요'),
        HumanMessagePromptTemplate.from_template('{chat}')
    ]
) 

#3. chain 생성
chat_chain = LLMChain(
    llm = chat_model,
    prompt = chat_prompt
) 

app = FastAPI() #라우터: 교통정리

#4. 챗봇 생성 

@app.post("/hero")
def teacher(chat:str= Form(...)):  #클라이언트가 보내는 key value
    
    result = chat_chain.predict(chat= chat)
    
    #result = llm(talk)
    
    return {'result':result} #gpt가 입력한 값을 그대로 클라이언트에게 전달


if __name__ == "__main__" : 
    uvicorn.run(app, host='127.0.0.1', port=7001) #서버종료 : ctrl + c 