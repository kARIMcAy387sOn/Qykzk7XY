# 代码生成时间: 2025-09-29 20:42:49
import pandas as pd
from typing import List

# 定义区块链节点类
class BlockchainNode:
    """
    区块链节点管理类。
    """
    def __init__(self, node_id: int, node_name: str, node_address: str):
        """
        初始化节点信息。
        :param node_id: 节点唯一标识符
        :param node_name: 节点名称
        :param node_address: 节点地址
        """
        self.node_id = node_id
        self.node_name = node_name
        self.node_address = node_address

    def __str__(self):
        """
        返回节点的详细信息。
        """
        return f"Node ID: {self.node_id}, Name: {self.node_name}, Address: {self.node_address}"

# 定义区块链节点管理器
class BlockchainNodeManager:
    """
    区块链节点管理器，负责管理所有节点。
    """
    def __init__(self):
        """
        初始化节点管理器。
        """
        self.nodes = []

    def add_node(self, node: BlockchainNode):
        """
        添加一个新的节点。
        :param node: 新节点对象
        """
        if node in self.nodes:
            raise ValueError("Node already exists")
        self.nodes.append(node)

    def remove_node(self, node_id: int):
        """
        移除一个节点。
        :param node_id: 需要移除的节点ID
        """
        for node in self.nodes:
            if node.node_id == node_id:
                self.nodes.remove(node)
                return
        raise ValueError("Node not found")

    def get_node(self, node_id: int):
        """
        根据节点ID获取节点信息。
        :param node_id: 节点ID
        """
        for node in self.nodes:
            if node.node_id == node_id:
                return node
        raise ValueError("Node not found")

    def list_nodes(self):
        """
        列出所有节点。
        """
        for node in self.nodes:
            print(node)

# 示例用法
if __name__ == "__main__":
    manager = BlockchainNodeManager()

    try:
        # 添加节点
        node1 = BlockchainNode(1, "Node 1", "192.168.1.1")
        manager.add_node(node1)
        node2 = BlockchainNode(2, "Node 2", "192.168.1.2")
        manager.add_node(node2)

        # 列出所有节点
        manager.list_nodes()

        # 获取单个节点信息
        node = manager.get_node(1)
        print(f"Selected Node: {node}")

        # 移除节点
        manager.remove_node(1)
        manager.list_nodes()

    except ValueError as e:
        print(f"Error: {e}")