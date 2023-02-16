import json
class Book:
  def __init__(self, title, author, year):
    self.title = title
    self.author = author
    self.year = year

  def to_json(self):
    return self.__dict__

class BookCollection:
  def __init__(self):
    self.books = []

  def add(self, book):
    self.books.append(book)

  def to_json(self):
    books = [book.to_json() for book in self.books]
    return json.dumps(books, indent=4)

collection = BookCollection()
collection.add(Book('A Song of Ice and Fire', 'George R. R. Martin', 1996))
collection.add(Book('The 48 Laws of Power', 'Robert Greene', 1998))
collection.add(Book('Think and Grow Rich', 'Napoleon Hill', 1937))

books = collection.to_json()
print(books)