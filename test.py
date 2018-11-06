#coding-utf-8

class Bag():
    def __init__(self, maxsize=10): # 指定背包的默认最大长度
        self.maxsize = maxsize
        self._items = list() # 实例化容器对象，这里使用list

    def __len__(self): # 求背包现有物品长度
        return len(self._items)
    
    def add(self, item):
        if len(self) >= self.maxsize: # add之前判断背包是否物品已满
            raise Exception('Bag is full')
        self._items.append(item)

    def remove(self, item):
        self._items.remove(item)

    def __iter__(self):
        for i in self._items: # yield惰性输出
            yield i

    def clear(self): # 清除
        self._items.clear()

# 测试ADT
bag = Bag()

for i in range(5):
    bag.add(i)

assert len(bag) == 5

bag.remove(2)

assert len(bag) == 4

bag.clear()

assert len(bag) == 0

for i in range(10):
    bag.add(i)

assert len(bag) == 10

try: # 异常捕获
    bag.add(0)
except Exception as e:
    print('Bag is full ! ')

print('用例执行完成')
