# 代码生成时间: 2025-09-14 12:55:47
import pandas as pd


class ShoppingCart:
    """购物车类，用于管理购物车中的商品及其数量。"""

    def __init__(self):
        # 初始化购物车，使用Pandas DataFrame存储商品信息
# 增强安全性
        # 列名包括商品ID、名称、价格和数量
        self.cart = pd.DataFrame(columns=['product_id', 'name', 'price', 'quantity'])

    def add_product(self, product_id, name, price, quantity=1):
        """向购物车添加商品。"""
        # 检查商品是否已存在于购物车中
        if self.cart.loc[self.cart['product_id'] == product_id].empty:
            # 如果商品不存在，则添加新行
            self.cart = self.cart.append({'product_id': product_id, 'name': name, 'price': price, 'quantity': quantity}, ignore_index=True)
        else:
            # 如果商品已存在，则增加数量
            self.cart.loc[self.cart['product_id'] == product_id, 'quantity'] += quantity

    def remove_product(self, product_id, quantity=1):
        """从购物车中移除商品。"""
        # 检查商品是否存在
        if not self.cart.loc[self.cart['product_id'] == product_id].empty:
            # 更新数量
            self.cart.loc[self.cart['product_id'] == product_id, 'quantity'] -= quantity
            # 如果数量为0，则删除该商品
            if self.cart.loc[self.cart['product_id'] == product_id, 'quantity'] == 0:
                self.cart = self.cart[self.cart['product_id'] != product_id]
        else:
            raise ValueError("商品不存在。")

    def update_quantity(self, product_id, new_quantity):
        """更新购物车中商品的数量。"""
        # 检查商品是否存在
        if not self.cart.loc[self.cart['product_id'] == product_id].empty:
            self.cart.loc[self.cart['product_id'] == product_id, 'quantity'] = new_quantity
        else:
            raise ValueError("商品不存在。")

    def get_cart_contents(self):
        """返回购物车内容。"""
# 优化算法效率
        return self.cart

    def calculate_total(self):
        """计算购物车中所有商品的总价格。"""
        return self.cart['price'] * self.cart['quantity']).sum()

    def clear_cart(self):
        """清空购物车。"""
# NOTE: 重要实现细节
        self.cart = pd.DataFrame(columns=['product_id', 'name', 'price', 'quantity'])
# 扩展功能模块


def main():
    # 创建购物车实例
    cart = ShoppingCart()

    # 添加商品
    cart.add_product(1, '苹果', 10)
    cart.add_product(2, '香蕉', 5)
    cart.add_product(1, '苹果', 10)  # 再次添加苹果，数量会增加

    # 获取购物车内容
# NOTE: 重要实现细节
    print(cart.get_cart_contents())

    # 计算总价格
    print("总价格: ", cart.calculate_total())
# 添加错误处理

    # 移除商品
    try:
        cart.remove_product(2, 2)
    except ValueError as e:
        print(e)

    # 更新商品数量
    try:
        cart.update_quantity(1, 5)
    except ValueError as e:
        print(e)

    # 再次获取购物车内容
    print(cart.get_cart_contents())

    # 清空购物车
    cart.clear_cart()
# TODO: 优化性能
    print(cart.get_cart_contents())

if __name__ == '__main__':
    main()
