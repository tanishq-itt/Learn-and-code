import pickle

class BookStorageService:
    def save(self, book):
        filename = f"/documents/{book.title} - {book.author}"
        with open(filename, "wb") as file:
            pickle.dump(book, file)
