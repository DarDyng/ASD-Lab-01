
def tree_successor(root):   # Алгоритм пошуку термінального вузла Successor
	# Термінальний вузол завжди є листком або вузлом з одним нащадком і процедура їх видалення описана вище.
    if root.right != None:
        return minimum(root.right)
    y = root.parent
    while (y != None and x == y.right):
        x = y
        y = y.parent
    return y.keyА

# Програма Python для демонстрації операції видалення бінарному дереві пошуку

# Бінарне дерево Node


class Tree:

    # Конструктор для створення нового Node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None


# Допоміжна функція для обходу BST у порядку


def inorder(root): # центрований (inorder) обхід дерева
	"""
	 How it work?

	 Спочатку відвідайте всі вузли у лівому піддереві
	 Потім кореневий вузол
	 Відвідайте всі вузли у правому піддереві

	 :param root:
	 :return:
	 """
	if root is not None:
		inorder(root.left)
		print(root.key, " -> ", end=" ")
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
        print(str(root.key), " -> ", end='')


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
        print(str(root.key), " -> ", end='')
        postorder(root.left)
        postorder(root.right)


# Допоміжна функція для вставки в новий вузол із заданим ключем у BST
def insert(node, key):

	# Якщо дерево порожнє, поверніть новий вузол
	if node is None:
		return Tree(key)

	# Інакше повторюватися вниз по дереву
	if key < node.key:
		node.left = insert(node.left, key)
	else:
		node.right = insert(node.right, key)

	# повертає (незмінний) покажчик вузла
	return node

# Дано непорожній двійковий файл
# дерево пошуку, повертає вузол
# з мінімальним значенням ключа знайдене в цьому дереві
# Зверніть увагу, що все дерево не потрібно обшукувати


def minValueNode(node):
	current = node

	# петля вниз, щоб знайти крайній лівий лист
	while(current.left is not None):
		current = current.left

	return current

# За наявності бінарного дерева пошуку та ключа ця функція видаляє ключ і повертає новий корінь


def deleteNode(root, key):
	# Базовий випадок
	if root is None:
		return root

	# Якщо ключ, який потрібно видалити, менший за root.key, тоді він знаходиться в лівому піддереві

	if key < root.key:
		root.left = deleteNode(root.left, key)

	# Якщо kеу, який потрібно видалити, більший за кореневий ключ, тоді він лежить у правому піддереві

	elif(key > root.key):
		root.right = deleteNode(root.right, key)

	# Якщо ключ такий самий, як ключ root, то це вузол, який потрібно видалити
	else:

		# Вузол лише з одним дочірнім елементом або без нього
		if root.left is None:
			temp = root.right
			root = None
			return temp

		elif root.right is None:
			temp = root.left
			root = None
			return temp

		# Вузол з двома дочірніми елементами:
		# Отримати наступника в порядку (найменший у правому піддереві)
		temp = minValueNode(root.right)

		# Скопіюйте вміст наступника порядку до цього вузла
		root.key = temp.key

		# Видалити наступника по порядку
		root.right = deleteNode(root.right, temp.key)

	return root


def minimum(root):

	if root == None:
		return float('+inf')
	else:
		res = root.key
		lres = minimum(root.left)
		rres = minimum(root.right)
		if lres < res:
			res = lres
		if rres < res:
			res = rres
	return res


rooot = None

rooot = insert(rooot, 32)  # вставка елемента в бінарне дерево
rooot = insert(rooot, 3)   # вставка елемента в бінарне дерево
rooot = insert(rooot, 43)  # вставка елемента в бінарне дерево
rooot = insert(rooot, 15)  # вставка елемента в бінарне дерево
rooot = insert(rooot, 2)   # вставка елемента в бінарне дерево
rooot = insert(rooot, 54)  # вставка елемента в бінарне дерево
rooot = insert(rooot, 66)  # вставка елемента в бінарне дерево

print("\n-------------------------------------------")
inorder(rooot)
print("\n")
postorder(rooot)
print("\n")
preorder(rooot)
print("\n\n-------------------------------------------")

rooot = deleteNode(rooot, 3)
rooot = deleteNode(rooot, 54)

print("\n-------------------------------------------")
inorder(rooot)
print("\n")
postorder(rooot)
print("\n")
preorder(rooot)
print("\n-------------------------------------------")

print(f"Мінімальний елемент дерева - {minimum(rooot)}")

print("\n-------------------------------------------")
inorder(rooot)
print("\n")
postorder(rooot)
print("\n")
preorder(rooot)
print("\n\n-------------------------------------------")

print(tree_successor(rooot))
rooot = deleteNode(rooot, tree_successor(rooot))

print("\n-------------------------------------------")
inorder(rooot)
print("\n")
postorder(rooot)
print("\n")
preorder(rooot)
print("\n\n-------------------------------------------")
