

lines = []
with open('2022/day7/input.txt', 'r') as f:
    for line in f.readlines():
        lines.append(line.strip('\n'))


class Tree(object):
    """Generic tree node"""
    def __init__(self, name='/', size= None, parent=None):
        self.name = name
        self.children = []
        self.size = size
        self.total_size = None
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

    def calc_dir_size(self):
        size = 0
        if self.dir:
            for n in self.children:
                if n.dir:
                    size += calc_dir_size(n)
                else:
                    size += n.size
        self.total_size = size
        return self.total_size

    def __repr__(self):
        if self.size is None:
            info = '(dir) \n'
        else:
            info = f'(file, size={self.size})'

        return f' - {self.name} {info}'


cur_node = Tree('/')
node_dict = {'/': cur_node}

for i, line in enumerate(lines[:206]):
    if line.startswith('$'):
        if line.startswith('$ cd'):
            cd_arg = line.split(' ')[2]
            if cd_arg == '..':
                cd_arg = cur_node.parent.name
            elif cd_arg == '/':
                pass
            else:
                if cd_arg not in node_dict:
                    node_dict[cd_arg] = Tree(cd_arg, size=None, parent=cur_node)

            cur_node = node_dict[cd_arg]

    else:
        if line.startswith('dir'):
            cd_arg = line.split(' ')[1]
            if cd_arg not in node_dict:
                node_dict[cd_arg] = Tree(cd_arg, size=None, parent=cur_node)

        elif line[0].isdigit():
            size, fname = line.split(' ')
            size = int(size)
            if fname not in node_dict:
                node_dict[fname] = Tree(fname, size=size, parent=cur_node)

for node_name, node in node_dict.items():
    if node.parent is not None:
        node.parent.add_child(node_dict[node_name])

ans_dict = {}
for node in node_dict.values():
    if node.dir:
        dir_size = node.calc_dir_size()
        if dir_size <= 100000:
            ans_dict[node.name] = dir_size

ans = sum(ans_dict.values())




