from binary_tree import  *
def in_order(node):
    
    if node.left:
        in_order(node.left)
    print(node)
    if node.right:
        in_order(node.right)

if __name__ == "__main__":
    root = create_tree()
    in_order(root)