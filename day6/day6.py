from typing import MutableMapping


class Node:
    def __init__(self, name):
        self.name = name
        self.children = set()
        self.distance_to_root = -1

    def add_child(self, child):
        self.children.add(child)

    def __hash__(self):
        return self.name.__hash__()

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Node):
            return self.name == other.name
        return False


nodes: MutableMapping[str, Node] = dict()

for line in open('input', 'r'):
    line = line.replace('\n', '')
    line = line.split(')')
    parent_name = line[0]
    child_name = line[1]

    if parent_name not in nodes:
        nodes[parent_name] = Node(parent_name)

    if child_name not in nodes:
        nodes[child_name] = Node(child_name)

    nodes[parent_name].add_child(nodes[child_name])

print(len(nodes))

root = nodes['COM']

def dfs(node, distance):
    node.distance_to_root = distance

    if len(node.children) == 0:
        return
    else:
        for child in node.children:
            dfs(child, distance + 1)


dfs(root, 0)

print(sum([n.distance_to_root for n in nodes.values()]))

# part 2: for each node, find the distance to san and the distance to you. The minimum of the sum of this pair -2 is the
# answer. (Assuming the graph contains no cycles)
results = []
for i in nodes.values():

    # init to -1
    for n in nodes.values():
        n.distance_to_root = -1

    dfs(i, 0)

    if nodes['SAN'].distance_to_root > -1 and nodes['YOU'].distance_to_root > -1:
        results.append((nodes['SAN'].distance_to_root, nodes['YOU'].distance_to_root))

print(min([t[0] + t[1] for t in results]) - 2)