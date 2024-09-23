# 이순신 장군 챗봇

이 프로젝트는 **FastAPI**를 사용해 이순신 장군의 말투로 대화하는 챗봇을 구현합니다. GPT-4 모델을 활용하여 사용자가 입력한 대화에 대해 이순신 장군의 어투로 답변합니다.

## 설치 및 실행

### 1. 리포지토리 클론
프로젝트를 클론하여 로컬 환경에 복사합니다.

git clone https://github.com/username/lee-soon-shin-chatbot.git
cd lee-soon-shin-chatbot

### 2. 가상 환경 설정 (선택 사항)
가상 환경을 설정하여 필요한 패키지를 격리된 환경에서 설치할 수 있습니다.

python -m venv env
source env/bin/activate  # Windows에서는 env\Scripts\activate

### 3. 필수 패키지 설치
필요한 라이브러리와 패키지를 requirements.txt 파일을 통해 설치합니다.

pip install -r requirements.txt

### 4. OpenAI API 키 설정
프로젝트를 실행하기 전에 OpenAI API 키를 설정해야 합니다. os.environ['OPENAI_API_KEY'] 부분에 실제 API 키를 입력합니다.

os.environ['OPENAI_API_KEY'] = 'Your_OpenAI_API_Key'

### 5. FastAPI 서버 실행
다음 명령어를 통해 FastAPI 서버를 실행합니다. 서버는 127.0.0.1:7001에서 실행됩니다.

uvicorn main:app --reload --host 127.0.0.1 --port 7001
사용 방법
서버가 실행되면, 클라이언트는 /hero 경로로 POST 요청을 보내 챗봇과 대화할 수 있습니다.

요청 예시:

curl -X POST "http://127.0.0.1:7001/hero" -d "chat=장군님, 전투에서 승리하려면 어떻게 해야 할까요?"
응답 예시:

json

{
  "result": "후손이여, 전투에서 승리하려면 용맹과 지혜가 필요하니라. 항상 준비를 철저히 하고, 적을 방심하지 말라."
}

## 코드 설명

FastAPI 서버 생성: FastAPI를 사용하여 서버를 설정하고, 클라이언트 요청을 처리할 경로 /hero를 설정합니다.
GPT-4 모델 사용: langchain을 통해 GPT-4 모델을 불러오고, 이순신 장군의 말투로 응답하는 대화 체인을 생성합니다.
POST 요청 처리: 클라이언트가 보낸 chat 데이터를 바탕으로 대화 응답을 생성하여 반환합니다.

## 라이선스
이 프로젝트는 MIT 라이선스를 따릅니다.

## 사용 방법

curl -X POST "http://127.0.0.1:7001/hero" -d "chat=안녕하세요, 장군님!"

## 라이선스
MIT
"# Admiral-chat" 
