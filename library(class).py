class Library:
    def __init__(self):
        self.library=[]
    def add_book(self, title, auther, copies):
        book= {"Title":title, "Auther":auther, "Copies":copies}
        self.library.append(book)
    def display_books(self):
        for i in self.library:
            print(i)
    def search_book(self, title):
        for i in self.library:
            if(i["Title"] == title):
                print(i["Auther"])
lb1= Library()
lb1.add_book("Python", "aaa", 4)
lb1.add_book("java", "bbb", 5)
lb1.display_books()
lb1.search_book("Python")
