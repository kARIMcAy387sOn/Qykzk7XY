# 代码生成时间: 2025-10-06 02:12:28
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import numpy as np

"""
商品推荐引擎
使用Pandas和Sklearn实现基于物品相似度的推荐系统
"""

class ProductRecommendationEngine:
    def __init__(self, data):
        """
        初始化商品推荐引擎
        :param data: 数据集，包含用户-商品评分信息
        """
        self.data = pd.DataFrame(data)
        self.item_similarity_matrix = None
        self.user_item_matrix = None

    def calculate_item_similarity(self):
        """
        计算商品相似度矩阵
        """
        # 将评分矩阵转换为标准化向量，以便计算余弦相似度
        self.user_item_matrix = StandardScaler().fit_transform(self.data.pivot_table(index='user_id', columns='product_id', values='rating').values)
        # 计算余弦相似度矩阵
        self.item_similarity_matrix = cosine_similarity(self.user_item_matrix)

    def recommend_products(self, user_id, top_n=5):
        """
        为指定用户推荐前N个最相似的商品
        :param user_id: 用户ID
        :param top_n: 推荐商品数量
        :return: 推荐商品列表
        """
        if self.item_similarity_matrix is None:
            raise ValueError("请先计算商品相似度矩阵")
        if user_id not in self.data['user_id'].values:
            raise ValueError("用户ID不存在")

        # 获取指定用户的评分向量
        user_vector = self.user_item_matrix[self.data['user_id'].values.tolist().index(user_id)]
        # 计算商品相似度
        similar_scores = np.dot(self.item_similarity_matrix, user_vector)
        # 获取最相似的商品ID
        sorted_item_indices = np.argsort(-similar_scores)
        # 推荐商品
        recommended_items = self.data['product_id'].iloc[sorted_item_indices[1:top_n+1]].tolist()
        return recommended_items

    def evaluate(self, test_data):
        """
        评估推荐系统的准确性
        :param test_data: 测试数据集
        """
        if self.item_similarity_matrix is None:
            raise ValueError("请先计算商品相似度矩阵")
        
        self.data = pd.concat([self.data, test_data])
        self.calculate_item_similarity()
        
        self.data = self.data[self.data['user_id'].isin(test_data['user_id'].values)]
        self.test_data = test_data
        
        predicted_ratings = []
        actual_ratings = []
        
        for index, row in self.test_data.iterrows():
            user_id = row['user_id']
            product_id = row['product_id']
            
            # 获取预测评分
            user_vector = self.user_item_matrix[self.data['user_id'].values.tolist().index(user_id)]
            product_index = self.data['product_id'].values.tolist().index(product_id)
            predicted_rating = np.dot(user_vector, self.user_item_matrix[product_index])
            predicted_ratings.append(predicted_rating)
            
            # 获取实际评分
            actual_ratings.append(row['rating'])
        
        return predicted_ratings, actual_ratings

# 示例用法
if __name__ == '__main__':
    data = {
        'user_id': [1, 1, 1, 2, 2, 3, 3, 3],
        'product_id': [101, 102, 103, 101, 103, 101, 102, 103],
        'rating': [4, 3, 5, 2, 3, 4, 3, 5]
    }
    recommendation_engine = ProductRecommendationEngine(data)
    recommendation_engine.calculate_item_similarity()
    recommended_items = recommendation_engine.recommend_products(1)
    print("推荐商品: ", recommended_items)
