import xml.etree.cElementTree as ET
tree = ET.parse('book.xml')
root = tree.getroot()


def get_id():
    for child in root:
        child.findall('id')
        print(child.attrib)


def book_count():
    count = root.findall('book')
    print(len(count))


def sort_price():
    all_price = {}
    for books in root.iter('book'):
        title = books.find('title').text.split('.')
        price = books.find('price').text.split()
        doc1 = dict(zip(title, price))
        all_price.update(doc1)
    print(sorted(all_price.items(), key=lambda f: float(f[1])))


def sort_by_date():
    all_date = {}
    for date in root.iter('book'):
        title2 = date.find('title').text.split('.')
        dates = date.find('publish_date').text.split()
        doc2 = dict(zip(title2, dates))
        all_date.update(doc2)
    print(sorted(all_date.items(), key=lambda d: str(d[1])))


def book_year_2000(root_var):
    date_dict = {}
    for child in root_var:
        key = child[1].text
        value = child[4].text
        date_dict[key] = value

    date_dict2 = {}
    for key, value in date_dict.items():
        if '2000' in date_dict[key]:
            date_dict2[key] = value

    if date_dict2:
        print(date_dict2)
    else:
        print('Error')


def book_genre(root_var, genre=None):
    books_list = []
    if genre is None:
        genre = 'Computer'

    for child in root_var:
        if genre == child[2].text:
            books_list.append(child)

    if books_list:
        print(f'books in genre {genre} is: ')
        for element in books_list:
            print(element[0].text, element[4].text, element[5].text)
    else:
        print('Error')


if __name__ == '__main__':
    get_id()
    book_count()
    sort_price()
    sort_by_date()
    book_year_2000(root)


