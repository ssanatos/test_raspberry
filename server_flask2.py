from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloworld():
    str = "Hello World!"
    return str

# host가 ip. 다른데서도 막 접속하게 0.0.0.0 
# 저 플라스크를 서버인양 동작하기
app.run(host = '0.0.0.0', port = '8000')
# 실행하면 터미널에 나오는 IP 클릭해서 들어가기.
# ----