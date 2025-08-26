# 代码生成时间: 2025-08-26 13:21:29
import pandas as pd

"""
程序：响应式布局设计
使用Pandas框架处理数据
"""

# 定义一个函数，用于创建响应式布局的数据框架
def create_responsive_layout(data, column_widths):
    """
    创建一个响应式布局的数据框架
    
    参数：
    data (list of dict): 数据列表，每个元素是一个包含列名和值的字典
    column_widths (dict): 列宽度字典，键为列名，值为列宽度
    
    返回：
    pd.DataFrame: 响应式布局的数据框架
    
    异常：
    ValueError: 如果数据或列宽度无效
    """
    if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
        raise ValueError("数据必须是字典列表")
    if not isinstance(column_widths, dict):
        raise ValueError("列宽度必须是字典")
    
    # 创建数据框架
    df = pd.DataFrame(data)
    
    # 确保所有列都存在于数据框架中
    for column in column_widths:
        if column not in df.columns:
            raise ValueError(f"列'{column}'不存在于数据框架中")
    
    # 设置列宽度
    df.style.set_table_styles([
        {'selector': f'th[colindex={i}]', 'props': [('width', column_widths[col])}} for i, col in enumerate(df.columns)
    ])
    
    return df

# 示例用法
if __name__ == '__main__':
    # 定义数据
    data = [
        {'姓名': '张三', '年龄': 25, '职业': '工程师'},
        {'姓名': '李四', '年龄': 30, '职业': '设计师'}
    ]
    
    # 定义列宽度
    column_widths = {
        '姓名': '100px',
        '年龄': '80px',
        '职业': '120px'
    }
    
    try:
        # 创建响应式布局的数据框架
        df = create_responsive_layout(data, column_widths)
        
        # 显示数据框架
        print(df)
    except ValueError as e:
        print(f"错误：{e}")