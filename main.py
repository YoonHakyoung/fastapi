from typing import Union

from fastapi import FastAPI

app = FastAPI()


# 테스트 생성

# 테스트 삭제

# 테스트 케이스 목록 가져오기
@app.get("/testcase/{testcase_id}")
def read_list():
    # 테스트 케이스 가져오는 SQL
    return 

# runner 실행

# 테스트 결과값 반환
@app.get("/testcase/{testcase_id}/stats")
def stats():
    # 테스트 결과 가져오는 SQL
    return