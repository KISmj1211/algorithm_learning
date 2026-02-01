def calculate_node(level):
    return 2 ** level

def calculate_all_node(level):
    return 2 ** (level+1) - 1

def calculate_edge(level):
    return 2 ** (level+1) - 2

def calculate_all_edge(level):
    return 2 ** (level+2) - 3

print(calculate_node(3))
print(calculate_all_node(3))

print(calculate_node(4))

##############
tree = [1, 2, 3, 4, 5, 6, 7]

# 새 노드를 추가하는 함수를 정의합니다.
def add_node(tree, new_node):
    tree.append(new_node)

# 노드 8을 추가합니다.
add_node(tree, 8)

# 트리의 새 상태를 출력합니다.
print(tree)

def insert_node(tree, index, new_node):
    tree.insert(index, new_node)

tree_breadth = [1, 2, 3, 4, 5, 6, 7]
# 1 2 3 4 5 6 7
# tree_breadth[0]  = 1
# tree_breadth[3]  = 4

def level_order(tree):
    for node in tree:
        print(node,end=" ")

level_order(tree_breadth)


tree_none = [None, 1, 2, 3, 4, 5, 6, 7]
def level_order_none(tree):
    for node in tree[1:]:
        if node is not None:
            print(node,end=" ")
        else:
            break
level_order_none(tree_none)


tree = [1,2,3,4,5,6,7]
def remove_node(tree, remove_node):
    tree.remove(remove_node)
    
def remove_node_index(tree, node_to_remove):
    tree[node_to_remove - 1] = tree[-1]
    tree.pop()
    
def remove_node2(tree, node_to_remove_index):
    tree[node_to_remove_index] = None

remove_node(tree, 5)
    
    
    
    

