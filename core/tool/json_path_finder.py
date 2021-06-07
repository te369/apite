import json
from typing import List


class JsonPathFinder:
    """
    https://github.com/kingname/JsonPathFinder
    find_one方法返回从外层到目标字段的第一条路径。
    而find_all方法返回从外层到目标字段的所有路径。
    iter_node方法。在把 JSON 字符串转成 Python 的字典或者列表以后，
    这个方法使用深度优先遍历整个数据，
    记录它走过的每一个字段，如果遇到列表就把列表的索引作为 Key。直到遍历到目标字段，或者某个字段的值不是列表也不是字典时结束本条路径，继续遍历下个节点。
    """
    def __init__(self, json_str, mode='key'):
        self.data = json.loads(json_str)
        self.mode = mode

    def iter_node(self, rows, road_step, target):
        if isinstance(rows, dict):
            key_value_iter = (x for x in rows.items())
        elif isinstance(rows, list):
            key_value_iter = (x for x in enumerate(rows))
        else:
            return
        for key, value in key_value_iter:
            current_path = road_step.copy()
            current_path.append(key)
            if self.mode == 'key':
                check = key
            else:
                check = value
            if check == target:
                yield current_path
            if isinstance(value, (dict, list)):
                yield from self.iter_node(value, current_path, target)

    def find_one(self, target: str) -> list:
        path_iter = self.iter_node(self.data, [], target)
        for path in path_iter:
            return path
        return []

    def find_all(self, target) -> List[list]:
        path_iter = self.iter_node(self.data, [], target)
        return list(path_iter)

"""
if __name__ == '__main__':
    with open('te.json', ) as f:
        json_data = f.read()

    print('开始测试按 Key 搜索...')
    finder = JsonPathFinder(json_data)
    path_list = finder.find_all('headers')
    data = finder.data
    for path in path_list:
        print(path)

    print('开始测试按 Value 搜索：...')
"""