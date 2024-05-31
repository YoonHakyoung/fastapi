import logging
import subprocess

# 로그 설정
logging.basicConfig(level=logging.DEBUG)

# 로그 출력 후 작업을 수행할 핸들러 생성
class MyHandler(logging.Handler):
    def emit(self, record):
        print("## log 내용 : " + self.format(record))

# 로거 생성
logger = logging.getLogger(__name__)

# 핸들러 추가
logger.addHandler(MyHandler())

# 예시 로그 출력
#logger.debug('DEBUG:urllib3.connectionpool:http://example.com:80 "GET / HTTP/1.1" 200 648')
#logger.debug('DEBUG:root:Request to http://example.com successful. Response time: 301.663 ms, Content length: 1256 bytes')

# 매개변수 설정
url = "http://example.com"
initial_user_count = 10
additional_user_count = 5
interval_time = 2
repeat_count = 3
test_id = 123

# 명령어 설정
command = [
    "python",
    "runner.py",
    "--url", url,
    "--initial_user_count", str(initial_user_count),
    "--additional_user_count", str(additional_user_count),
    "--interval_time", str(interval_time),
    "--repeat_count", str(repeat_count),
    "--test_id", str(test_id)
]

# 명령어 실행
subprocess.run(command)

# 변수에 저장된 로그 메시지 출력
# print(variable_handler.log_messages)
