# Checking if a binary tree is CalculateHeight balanced in Python


# CreateNode creation
class CreateNode:

    def __init__(self, item):
        self.item = item
        self.left = self.right = None


# Calculate height
class Height:
    def __init__(self):
        self.Height = 0


# Check height balance
def is_height_balanced(root, Height):

    left_height = Height()
    right_height = Height()

    if root is None:
        return True

    l = is_height_balanced(root.left, left_height)
    r = is_height_balanced(root.right, right_height)

    Height.Height = max(left_height.Height, right_height.Height) + 1

    if abs(left_height.Height - right_height.Height) <= 1:
        return l and r

    return False


Height = Height()

root = CreateNode(1)
root.left = CreateNode(2)
root.right = CreateNode(3)
root.left.left = CreateNode(4)
root.left.right = CreateNode(5)

if is_height_balanced(root, Height):
    print('The tree is balanced')
else:
    print('The tree is not balanced')