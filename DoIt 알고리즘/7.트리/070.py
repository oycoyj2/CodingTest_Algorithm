import sys
sys.stdin = open("input.txt", 'rt')

def preorder(n):
    if n == '.':
        return
    print(n, end="")
    preorder(left[n])
    preorder(right[n])

def inorder(n):
    if n == '.':
        return
    inorder(left[n])
    print(n, end="")
    inorder(right[n])

def postorder(n):
    if n == '.':
        return
    postorder(left[n])
    postorder(right[n])
    print(n, end="")

N = int(input())
tree = {}
left = {}
right = {}
for i in range(N):
    parent, l_child, r_child = input().split()
    tree[parent] = True
    left[parent] = l_child
    right[parent] = r_child
    if l_child != '.':
        tree[l_child] = False
    if r_child != '.':
        tree[r_child] = False

root = ''
for node, has_parent in tree.items():
    if has_parent:
        root = node
        break

preorder(root)
print()
inorder(root)
print()
postorder(root)