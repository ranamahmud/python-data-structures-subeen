from binary_tree import  *
def post_order(node):
    
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    print(node)

if __name__ == "__main__":
    root = create_tree()
    post_order(root)