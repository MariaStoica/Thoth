# Thoth. A reading list generator.
import sys
import xml.etree.ElementTree
import random

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def anyBooksLeft():
	for categ in e.findall("Category"):
		queue = dict[categ.get("name")]
		if not queue.isEmpty():
			return True
	return False


if len(sys.argv) == 1:
	sys.exit("ERROR: Missing starting category. Set it by writing its name")

inputFilePath = './MyBooks.xml'
destinationFilePath = './ReadingList.txt'
dict = {}
startingCategory = sys.argv[1]

# read and parse the xml
e = xml.etree.ElementTree.parse(inputFilePath).getroot()

# add categories in their own queue - array of queues with category name as key
for categ in e.findall("Category"):
	categName = categ.get("name")

	books = Queue()
	for book in categ.findall("Book"):
		books.enqueue(book.get("title"))

	dict[categName] = books

# mix n mingle books according to the rules
readingList = dict[startingCategory].dequeue() + "\n"

index = 1
while anyBooksLeft():
	if index % 3 == 0 and not dict["fiction"].isEmpty():
		readingList += dict["fiction"].dequeue() + "\n"
	elif index % 4 == 0 and not dict["technical"].isEmpty():
		readingList += dict["technical"].dequeue() + "\n"
	elif random.randint(0,1) == 1 and not dict["interesting"].isEmpty():
		readingList += dict["interesting"].dequeue() + "\n"
	elif not dict["selfdev"].isEmpty():
		readingList += dict["selfdev"].dequeue() + "\n"
	index = index + 1

# write the results in the destination file
destinationFile = open(destinationFilePath, 'w')
destinationFile.write(readingList)
destinationFile.close()
print(readingList)
