# 代码生成时间: 2025-08-30 18:59:30
import pandas as pd
from flask import Flask, request, jsonify

# 初始化Flask应用
app = Flask(__name__)

# 示例数据集
data = {
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35]
}

# 将示例数据转换成Pandas DataFrame
df = pd.DataFrame(data)

# API接口 - 获取所有用户数据
@app.route("/users", methods=["GET"])
def get_users():
    # 将DataFrame转换为JSON格式返回
    return jsonify(df.to_dict(orient="records"))

# API接口 - 创建新用户
@app.route("/users", methods=["POST"])
def create_user():
    try:
        # 获取请求体中的JSON数据
        user_data = request.get_json()
        # 将新用户添加到DataFrame中
        new_row = pd.DataFrame([user_data], columns=df.columns)
        df = pd.concat([df, new_row], ignore_index=True)
        return jsonify(new_row.to_dict(orient="records").values()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# API接口 - 更新用户信息
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    try:
        user_data = request.get_json()
        # 检查用户ID是否存在
        if user_id not in df["id"].values:
            return jsonify({"error": "User not found"}), 404
        # 更新用户信息
        df.loc[df["id"] == user_id] = user_data
        return jsonify(df.loc[df["id"] == user_id].to_dict(orient="records")), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# API接口 - 删除用户
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        # 检查用户ID是否存在
        if user_id not in df["id"].values:
            return jsonify({"error": "User not found"}), 404
        # 删除用户
        df = df[df["id"] != user_id]
        return jsonify({"message": "User deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
