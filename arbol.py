class Node:
    def __init__(self, name, amount=0.0, parent=None):
        self.name = name
        self.amount = amount
        self.parent = parent
        self.children = []

        if parent:
            self.parent.children.append(self)


root = Node('Total', amount=1000000.0)
node1 = Node('Bonos', amount=300000.0, parent=root)
node2 = Node('Acciones', amount=700000.0, parent=root)
node3 = Node('Bonos US', amount=100000.0, parent=node1)
node4 = Node('Bonos Chile', amount=200000.0, parent=node1)
node5 = Node('Acciones US', amount=500000.0, parent=node2)
node6 = Node('Acciones Chile', amount=200000.0, parent=node2)

"""
Implementa la función print_tree, que recibe como único argumento el nodo
raíz de un árbol e imprime los valores de name y amount de cada nodo
de forma ordenada.
Ejemplo:
>> print_tree(root)
Total: 1000000.0
  Bonos: 300000.0
    Bonos US: 100000.0
    Bonos Chile: 200000.0
  Acciones: 700000.0
    Acciones US: 500000.0
    Acciones Chile: 200000.0
>>
"""


def print_tree(root_node):
    value = "%s: %s" % (root_node.name, root_node.amount)
    result = "\t" * 0 + value + "\n"
    if root_node.children:
        for child in root_node.children:
            result += get_child(child, 1)

    print(result)


def get_child(children, nivel):
    children_value = "%s: %s" % (children.name, children.amount)
    return_value = "\t" * nivel + children_value + "\n"
    if children.children:
        for child in children.children:
            return_value += get_child(child, nivel + 1)
    return return_value


if __name__ == "__main__":
    print_tree(root)
