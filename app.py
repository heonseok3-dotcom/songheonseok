from flask import Flask, render_template, jsonify, request
from datetime import datetime

app = Flask(__name__)

# 신분증 데이터베이스 (해시 테이블)
# QR 데이터(학번/식별번호)를 키로 사용하여 개인정보를 저장
id_database = {
    "2024001": {"name": "홍길동", "birth": "2005-05-10", "photo": "2024001.jpg", "dept": "컴퓨터공학과"},
    "2024002": {"name": "김철수", "birth": "2004-11-22", "photo": "2024002.jpg", "dept": "전자공학과"},
    "2024003": {"name": "이영희", "birth": "2005-01-30", "photo": "2024003.jpg", "dept": "정보통신과"},
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    qr_id = data.get('qr_id', '').strip()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 1. 존재 여부 확인 (본인 인증 로직)
    if qr_id in id_database:
        user_info = id_database[qr_id]
        return jsonify({
            "status": "success",
            "message": "본인 인증 완료",
            "user": user_info,
            "time": now
        })
    else:
        return jsonify({
            "status": "fail",
            "message": "등록되지 않은 신분증 정보입니다.",
            "time": now
        })

if __name__ == '__main__':
    app.run(debug=True, port=5000)