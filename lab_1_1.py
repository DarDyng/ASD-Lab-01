class Tree:
    """
    Attributes:
    root заміняє self для кращого читання коду
    """
    def __init__(root, data):  # конструктор  __init__ використовуватиметься для вставки елементів в дерево
        root.right = None
        root.left = None
        root.value = data
        
    def search_node(root, data):  # пошук елементу
        if data < root.value:
            if root.left is None:
                print(data, f" Елементу {data} не знайдено в дереві")
            print(root.left.search_node(data))
        elif data > root.value:
            if root.right is None:
               print(data, f" Елементу {data} не знайдено в дереві")
            print(root.right.search_node(data))
        else:
            print(root.value, f" Елемент {data} знайдено в дереві")
        
    def insert(root, data):  # метод для вставки елементів
        if root.value:
            if root.value > data:
                if root.left is None:
                    root.left = Tree(data)
                else:
                    root.left.insert(data)
            elif root.value < data:
                if root.right is None:
                    root.right = Tree(data)
                else:
                    root.right.insert(data)
        else:
            root.value = data
        
    def create_root_bst(root, data):  # функція котра створює першу вершину
        root.right = None
        root.left = None
        root.parent = None
        root.value = data


def inorder(root):  # центрований (inorder) обхід дерева
    """
    How it work?

    Спочатку відвідайте всі вузли у лівому піддереві
    Потім кореневий вузол
    Відвідайте всі вузли у правому піддереві

    :param root:
    :return:
    """
    if root:
        inorder(root.left)
        print(str(root.value), " -> ", end='')
        inorder(root.right)


def postorder(root):  # зворотний (postorder). обхід дерева
    """
    How it work?

    Відвідати всі вузли в лівому піддереві
    Відвідати кореневий вузол
    Відвідати всі вузли у правому піддереві

    :param root:
    :return:
    """
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.value), " -> ", end='')


def preorder(root):  # прямий (preorder) обхід дерева
    """
    How it work?

    Відвідайте кореневий вузол
    Завітайте до всіх вузлів у лівому піддереві
    Відвідайте всі вузли у правому піддереві

    :param root:
    :return:
    """
    if root:
        print(str(root.value), " -> ", end='')
        postorder(root.left)
        postorder(root.right)


root = Tree(10)  # створення екземпляру класу
root.insert(15)  # вставка елемента в бінарне дерево
root.insert(121)  # вставка елемента в бінарне дерево
root.insert(22)  # вставка елемента в бінарне дерево
root.insert(12)  # вставка елемента в бінарне дерево
root.insert(143)  # вставка елемента в бінарне дерево
root.insert(1)  # вставка елемента в бінарне дерево
root.insert(51)  # вставка елемента в бінарне дерево
print("inorder :\n")
inorder(root)  # центрований (inorder) обхід дерева
print("\n\npostorder :\n")
postorder(root)  # зворотний (postorder). обхід дерева
print("\n\npreorder :\n")
preorder(root)  # прямий (preorder) обхід дерева
print(f"\n")
print(f"\n", root.search_node(10))
print(f"\n", root.search_node(13))
