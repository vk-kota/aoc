

lines = []
with open('2022/day7/input.txt', 'r') as f:
    for line in f.readlines():
        lines.append(line.strip('\n'))


class Tree(object):
    """Generic tree node"""
    def __init__(self, index, name='/', size= None, parent=None):
        self.index = index
        self.name = name
        self.children = []
        self.size = size
        self.contents = {}
        if size is None:
            self.dir = True
        else:
            self.dir = False
        self.parent = None
        if parent is not None:
            if isinstance(parent, Tree):
                self.parent = parent
            else:
                raise TypeError

    def add_child(self, node: Tree):
        if isinstance(node, Tree):
            self.children.append(node)
        else:
            raise TypeError


    def __repr__(self):
        if self.size is None:
            info = '(dir) \n'
        else:
            info = f'(file, size={self.size})'

        return f' - {self.name} {info}'

def calc_dir_size(node: Tree):
    size = 0
    if len(node.children) == 0:
        size += node.size
    else:
        for n in node.children:
            size += calc_dir_size(n)

    total_size = size
    return total_size

cur_node = Tree(0, '/')
node_dict = {0: cur_node}
index = 1

for i, line in enumerate(lines):
    if line.startswith('$'):
        if line.startswith('$ cd'):
            cd_arg = line.split(' ')[2]
            if cd_arg == '..':
                cd_arg = cur_node.parent.name
                cur_node = cur_node.parent

            elif cd_arg == '/':
                cur_node = node_dict[0]
            else:
                cur_node = cur_node.contents[cd_arg]

    else:
        if line.startswith('dir'):
            cd_arg = line.split(' ')[1]
            node_dict[index] = Tree(index, cd_arg, size=None, parent=cur_node)
            cur_node.contents[cd_arg] = node_dict[index]
            index += 1

        elif line[0].isdigit():
            size, fname = line.split(' ')
            size = int(size)
            node_dict[index] = Tree(index, fname, size=size, parent=cur_node)
            cur_node.contents[fname] = node_dict[index]
            index += 1

for node_name, node in node_dict.items():
    if node.parent is not None:
        node.parent.add_child(node_dict[node_name])

ans_dict = {}
for node in node_dict.values():
    if node.dir:
        dir_size = calc_dir_size(node)
        if dir_size <= 100000:
            ans_dict[node.index] = dir_size

ans = sum(ans_dict.values())

# Answer 2
total_space = 70000000
req_space = 30000000
used_space = calc_dir_size(node_dict[0])
free_up = req_space - (total_space - used_space)


ans2_dict = {}
for node in node_dict.values():
    if node.dir:
        ans2_dict[node.index] = calc_dir_size(node)

ans2_dict_sorted = sorted(ans2_dict.items(), key=lambda item: item[1])

ans2 = min(v for _, v in ans2_dict_sorted if v >= free_up)
