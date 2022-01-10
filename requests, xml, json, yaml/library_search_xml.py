import xml.etree.cElementTree as ET
with open('library.xml') as f:
    root = ET.parse(f).getroot()


def book_finder(root_var, request=None):
    global key
    dict_books = {}
    if request is None:
        request = 'Learn Python 3 the Hard Way'

    for book in root_var.findall('book'):
        for child_elem in book:
            if request in child_elem.text:
                for key, value in book.attrib.items():
                    key = value
                dict_books.setdefault(key, book[1].text)

    if dict_books:
        print(f'Matches your "{request}" request')
        for key, value in dict_books.items():
            print(f'{key}: {value}')


book_finder(root)
print('^' * 50)
book_finder(root, 'Fantasy')
print('^' * 50)
book_finder(root, '2008')
print('^' * 50)
book_finder(root, '-09-10')
print('^' * 50)
