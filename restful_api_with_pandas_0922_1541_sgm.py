# 代码生成时间: 2025-09-22 15:41:17
import pandas as pd
from flask import Flask, request, jsonify

# 创建 Flask 应用
app = Flask(__name__)

# 定义一个简单的数据集
data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [25, 30, 35, 40, 45]
}

# 将数据集转换为 DataFrame
df = pd.DataFrame(data)

# 定义 API 接口，返回所有数据
@app.route("/api/data", methods=["GET"])
def get_all_data():
    try:
        # 返回 DataFrame 转换为 JSON
        return jsonify(df.to_dict(orient="records"))
    except Exception as e:
        # 错误处理
        return jsonify({"error": str(e)}), 500

# 定义 API 接口，根据 ID 获取数据
@app.route("/api/data/<int:data_id>", methods=["GET"])
def get_data_by_id(data_id):
    try:
        # 根据 ID 查找数据
        result = df[df['id'] == data_id]
        # 如果找到数据，返回数据
        if not result.empty:
            return jsonify(result.to_dict(orient="records"))
        else:
            # 如果没有找到数据，返回 404 错误
            return jsonify({"error": "Data not found"}), 404
    except Exception as e:
        # 错误处理
        return jsonify({"error": str(e)}), 500

# 定义 API 接口，添加新数据
@app.route("/api/data", methods=["POST"])
def add_data():
    try:
        # 获取 JSON 数据
        data = request.get_json()
        # 将数据添加到 DataFrame
        df = df.append(data, ignore_index=True)
        return jsonify(df.to_dict(orient="records")), 201
    except Exception as e:
        # 错误处理
        return jsonify({"error": str(e)}), 500

# 定义 API 接口，更新数据
@app.route("/api/data/<int:data_id>", methods=["PUT"])
def update_data(data_id):
    try:
        # 获取 JSON 数据
        data = request.get_json()
        # 根据 ID 查找数据
        result = df[df['id'] == data_id]
        # 如果找到数据，更新数据
        if not result.empty:
            df.loc[df['id'] == data_id] = data
            return jsonify(df.to_dict(orient="records"))
        else:
            # 如果没有找到数据，返回 404 错误
            return jsonify({"error": "Data not found"}), 404
    except Exception as e:
        # 错误处理
        return jsonify({"error": str(e)}), 500

# 定义 API 接口，删除数据
@app.route("/api/data/<int:data_id>", methods=["DELETE"])
def delete_data(data_id):
    try:
        # 根据 ID 查找数据
        result = df[df['id'] == data_id]
        # 如果找到数据，删除数据
        if not result.empty:
            df = df[df['id'] != data_id]
            return jsonify(df.to_dict(orient="records"))
        else:
            # 如果没有找到数据，返回 404 错误
            return jsonify({"error": "Data not found"}), 404
    except Exception as e:
        # 错误处理
        return jsonify({"error": str(e)}), 500

# 运行 Flask 应用
if __name__ == "__main__":
    app.run(debug=True)