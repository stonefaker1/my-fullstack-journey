fruits = ["苹果", "香蕉", "橘子"]

fruits.append("葡萄")  # 添加元素
fruits.insert(1, "梨")  # 在索引为1的位置插入元素
fruits.extend(["西瓜", "草莓"])  # 扩展列表，添加多个元素

fruits.remove("香蕉")  # 移除元素
fruits.pop()  # 移除最后一个元素
del fruits[0]  # 删除索引为0的元素

fruits[0] = "芒果"  # 修改索引为0的元素

print("西瓜" in fruits)  # 检查元素是否存在于列表中
print(fruits.index("西瓜"))  # 获取元素的索引
print(fruits.count("橘子"))  # 统计元素在列表中出现的次数