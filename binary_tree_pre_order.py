from binary_tree import  *
def pre_order(node):
    print(node)
    
    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)
if __name__ == "__main__":
    root = create_tree()
    pre_order(root)