from flask import Flask, jsonify, request

app = Flask(__name__)

# 模拟数据
data = [
    {"id": 1, "name": "测试案例1"},
    {"id": 2, "name": "测试案例2"}
]

@app.route('/')
def index():
    return "欢迎使用测试平台"

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def create_data():
    new_data = request.json
    data.append(new_data)
    return jsonify(new_data), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001,debug=True)
