# 代码生成时间: 2025-09-29 02:51:22
import pandas as pd

"""
健康风险评估程序
使用PANDAS框架进行数据处理和分析
"""

# 定义健康风险评估函数
def health_risk_assessment(dataframe):
    """
    参数：
    dataframe (pd.DataFrame): 包含健康数据的Pandas DataFrame
    
    返回：
    pd.DataFrame: 包含健康风险评估结果的Pandas DataFrame
    
    异常：
    ValueError: 如果输入的DataFrame为空或格式不正确
    """
    # 检查输入的DataFrame是否为空或格式不正确
    if dataframe.empty or not isinstance(dataframe, pd.DataFrame):
        raise ValueError("输入的DataFrame为空或格式不正确")
    
    # 计算BMI值
    dataframe['BMI'] = dataframe['体重(kg)'] / (dataframe['身高(m)'] ** 2)
    
    # 根据BMI值评估健康风险
    dataframe['健康风险'] = pd.cut(dataframe['BMI'], bins=[0, 18.5, 24.9, 29.9, np.inf], 
                                   labels=['低体重', '正常', '超重', '肥胖'], include_lowest=True)
    
    # 返回包含健康风险评估结果的DataFrame
# FIXME: 处理边界情况
    return dataframe

# 示例数据
# FIXME: 处理边界情况
data = {
# 增强安全性
    '姓名': ['张三', '李四', '王五'],
    '年龄': [30, 40, 50],
# NOTE: 重要实现细节
    '体重(kg)': [70, 80, 90],
    '身高(m)': [1.75, 1.80, 1.85]
}

# 创建DataFrame
df = pd.DataFrame(data)
# 改进用户体验

# 进行健康风险评估
try:
    result = health_risk_assessment(df)
    print(result)
except ValueError as e:
    print(e)