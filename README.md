# URL 단축 서비스

### ☝️ 요구사항

<details>
<summary>
  <img src="https://img.shields.io/badge/AWS-orange">
</summary>
  &emsp;• DynamoDB 관련 권한이 있는 AWS 계정<br>
  &emsp;• DynamoDB 리소스를 다루기 위해 AWS 계정의 ACCESS KEY ID와 SECRET ACCESS KEY가 필요 (.env 파일에 입력)<br>
  <br>
  <img src="https://github.com/user-attachments/assets/3fa3e36e-6e87-4775-9295-885d05f950f2">

</details>

<details>
<summary>
  <img src="https://img.shields.io/badge/python-3.11_|_3.12-blue">
</summary>
  &emsp;• python 3.11 버전 이상
</details>

<details>
<summary>
  <img src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json">
</summary>
  &emsp;• python 패키지 관리용 poetry
</details>

***

### 👩‍💻 설치 및 시작
#### 1. poetry로 패키지 내려받기
```
poetry install
```
#### 2. poetry 가상환경 시작
```
poetry shell
```
#### 3. 서비스 시작
```
uvicorn app.main:app --reload
```
⚠️ 최초 시작 시 dynamodb 테이블을 생성하도록 되어있어 시간이 걸릴 수 있음

***

### 📝 API 문서
서비스 시작 후..
- [반응형 문서 (Swagger UI)](http://127.0.0.1:8000/docs)
- [대안 자동 문서](http://127.0.0.1:8000/redoc)

#### ✅ API 테스트
- `POST /shorten` : 단축 URL 생성
  - 위 Swagger UI에서 테스트 가능
- `GET /stats/{short_key}` : 단축 URL 통계 조회
  - 위 Swagger UI에서 테스트 가능
- `GET /{short_key}` : 원본 URL 리다이렉션
  - 브라우저 주소창에 `http://127.0.0.1:8000/{short_key}` 입력하여 리다이렉션 확인 가능
  - ⚠️ 한번 단축 URL로 접속하면 브라우저 캐시에 저장되어 다시 단축 URL로 접속하여도 통계가 업데이트되지 않음
    - 브라우저 캐시를 비우거나 시크릿탭으로 재시도해야 통계 업데이트 확인할 수 있음

***

### 🗃️ 데이터베이스
AWS DynamoDB를 사용

#### ⚙️ 설정
- 서비스 시작 시 테이블이 없으면 자동 생성
- "expire_at" 속성에 대해 TTL(Time To Live) 설정

#### ❓ 선정 이유
- 완전 관리형 서비스로 운영이 편함
- 확장성이 좋음
- 읽기가 많을 것으로 예상됨
  * key-value 데이터베이스로 읽기가 빠름
  * 추후 [DAX](https://aws.amazon.com/ko/dynamodbaccelerator/) 도입 가능 (아직은 서울 리전에 없음. 현재는 elasticache를 이용하는 방법이 있음)
- 테이블 설계가 어렵지만 서비스가 간단하여 단점이 부각되지 않는다고 판단

***

### ⚡ 보너스 기능
##### &emsp;&emsp;✔️ URL 키 만료 기능 (DynamoDB TTL 이용)
##### &emsp;&emsp;✔️ 통계 기능
##### &emsp;&emsp;❌ 테스트 코드

