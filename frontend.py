from tkinter import *
from backend import Database

database = Database("bookstore.db")

class Window(object):

    ### Initialization function
    def __init__(self, window):

        self.window = window

        ### Title of the desktop app
        self.window.wm_title("BookStore")

        ### Labels
        lbl1 = Label(window, text="Title")
        lbl1.grid(row=0, column=0)

        lbl2 = Label(window, text="Author")
        lbl2.grid(row=0, column=2)

        lbl3 = Label(window, text="Year")
        lbl3.grid(row=1, column=0)

        lbl4 = Label(window, text="ISBN")
        lbl4.grid(row=1, column=2)

        ### Entry lines
        self.title_txt = StringVar()
        self.entry1 = Entry(window, textvariable=self.title_txt)
        self.entry1.grid(row=0, column=1)

        self.author_txt = StringVar()
        self.entry2 = Entry(window, textvariable=self.author_txt)
        self.entry2.grid(row=0, column=3)

        self.year_txt = StringVar()
        self.entry3 = Entry(window, textvariable=self.year_txt)
        self.entry3.grid(row=1, column=1)

        self.isbn_txt = StringVar()
        self.entry4 = Entry(window, textvariable=self.isbn_txt)
        self.entry4.grid(row=1, column=3)

        ### Search results
        self.lst = Listbox(window, height=6, width=35)
        self.lst.grid(row=2, column=0, rowspan=6, columnspan=2)

        self.lst.bind('<<ListboxSelect>>', self.get_selected_row)

        ### Scrollbar for search results
        scb = Scrollbar(window)
        scb.grid(row=2, column=2, rowspan=6)

        self.lst.configure(yscrollcommand=scb.set)
        scb.configure(command=self.lst.yview)

        ### Buttons
        bttn1 = Button(window, text="View all", width=12, command=self.view_all)
        bttn1.grid(row=2, column=3)

        bttn2 = Button(window, text="Search entry", width=12, command=self.search_entry)
        bttn2.grid(row=3, column=3)

        bttn3 = Button(window, text="Add entry", width=12, command=self.add_entry)
        bttn3.grid(row=4, column=3)

        bttn4 = Button(window, text="Update selected", width=12, command=self.update_selected)
        bttn4.grid(row=5, column=3)

        bttn5 = Button(window, text="Delete selected", width=12, command=self.delete_selected)
        bttn5.grid(row=6, column=3)

        bttn6 = Button(window, text="Close", width=12, command=window.destroy)
        bttn6.grid(row=7, column=3)

    ### Gets the selected row and inserts the infos into the entry fields
    def get_selected_row(self, event):
        try:
            index = self.lst.curselection()[0]
            self.selected_item = self.lst.get(index)
            self.entry1.delete(0, END)
            self.entry1.insert(END, self.selected_item[1])
            self.entry2.delete(0, END)
            self.entry2.insert(END, self.selected_item[2])
            self.entry3.delete(0, END)
            self.entry3.insert(END, self.selected_item[3])
            self.entry4.delete(0, END)
            self.entry4.insert(END, self.selected_item[4])
        except IndexError:
            pass

    ### Makes 'View all' button functional
    def view_all(self):
        self.lst.delete(0, END)
        for item in database.view():
            self.lst.insert(END, item)

    ### Makes 'Search entry' button functional
    def search_entry(self):
        self.lst.delete(0, END)
        for item in database.search(self.title_txt.get(), self.author_txt.get(), self.year_txt.get(), self.isbn_txt.get()):
            self.lst.insert(END, item)

    ### Makes 'Add entry' button functional
    def add_entry(self):
        database.insert(self.title_txt.get(), self.author_txt.get(), self.year_txt.get(), self.isbn_txt.get())
        self.lst.delete(0, END)
        self.lst.insert(END, (self.title_txt.get(), self.author_txt.get(), self.year_txt.get(), self.isbn_txt.get()))

    ### Makes 'Update selected' button functional
    def update_selected(self):
        database.update(self.selected_item[0], self.title_txt.get(), self.author_txt.get(), self.year_txt.get(), self.isbn_txt.get())

    ### Makes 'Delete selected' button functional
    def delete_selected(self):
        database.delete(self.selected_item[0])

### App window
window = Tk()
### Executes the desktop app
Window(window)
### Prevents the app from closing immediately after being executed
window.mainloop()