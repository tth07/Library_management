from tkinter import *
from tkinter import ttk
import addbook
import sqlite3

con=sqlite3.connect('Library.db')
cur=con.cursor

class Main(object):
    def __init__(self, master):
        self.master = master
        mainFrame = Frame(self.master)
        mainFrame.pack()
        topFrame =Frame(mainFrame,width=1350,height=70,bg='#f8f8f8',padx=20,relief=SUNKEN,borderwidth=2)
        topFrame.pack(side=TOP,fill=X)
        centerFrame = Frame(mainFrame,width=1350,bg='#e0f0f0',height=680,relief=RIDGE)
        centerFrame.pack(side=TOP)
        centerLeftFrame = Frame(centerFrame,width=900,height=700,bg='#e0f0f0',borderwidth=2,relief='sunken')
        centerLeftFrame.pack(side=LEFT)
        centerRightFrame = Frame(centerFrame,width=450,height=700,bg='#e0f0f0',borderwidth=2,relief='sunken')
        centerRightFrame.pack()
        #search bar
        search_bar = LabelFrame(centerRightFrame,width=440,height=75,text="Search box",bg='#9bc9ff')
        search_bar.pack(fill=BOTH)
        self.lbl_search=Label(search_bar,text="Search: ",font='arial 12 bold',bg='#9bc9ff',fg='white')
        self.lbl_search.grid(row=0,column=0,padx=20,pady=10)
        self.end_search=Entry(search_bar,width=30,bd=10)
        self.end_search.grid(row=0,column=1,columnspan=3,padx=10,pady=10)
        self.btn_search=Button(search_bar,text="Search",font="arial 12 bold",bg='#fcc324',fg='white')
        self.btn_search.grid(row=0,column=4,padx=20,pady=10)
        #list book
        list_bar = LabelFrame(centerRightFrame,width=440,height=175,text="List box",bg='#fcc324')
        list_bar.pack(fill=BOTH)
        lbl_list = Label(list_bar,text="Short by",font="times 16 bold",fg='#2488ff',bg='#fcc324')
        lbl_list.grid(row=0,column=2)
        self.listChoice = IntVar()
        rb1 = Radiobutton(list_bar,text="Book List",var=self.listChoice,value=1,bg='#fcc324')
        rb2 = Radiobutton(list_bar,text="Available",var=self.listChoice,value=2,bg='#fcc324')
        rb3 = Radiobutton(list_bar,text="Issued",var=self.listChoice,value=3,bg='#fcc324')
        rb1.grid(row=1,column=0)
        rb2.grid(row=1,column=1)
        rb3.grid(row=1,column=2)
        btn_list=Button(list_bar,text="List Books",bg='#2488ff',fg='white',font='arial 12 bold')
        btn_list.grid(row=1,column=3,padx=40,pady=10)
        #title
        title_bar=Frame(centerRightFrame,width=440,height=40)
        title_bar.pack(fill=BOTH)
        self.title_right=Label(title_bar,text="Welcome to our Library",font="arial 16 bold")
        self.title_right.grid(row=0)




###################################################################################################################
        #add book
        self.btnbook= Button(topFrame,text="Add Book",font="arial 12 bold",compound=LEFT, command=self.addBook)
        self.btnbook.pack(side=LEFT,padx=10)

        #add member
        self.btnmember = Button(topFrame,text="Add Member",font="arial 12 bold",padx=10)
        self.btnmember.configure()
        self.btnmember.pack(side=LEFT)
        #give book
        self.btngive = Button(topFrame,text="Give Book",font="arial 12 bold",padx=10,)
        self.btngive.pack(side=LEFT)

########################################################################################################################
                    #tab1
        self.tabs= ttk.Notebook(centerLeftFrame,width=900,height=600)
        self.tabs.pack()
        self.tab1= ttk.Frame(self.tabs)
        self.tab2= ttk.Frame(self.tabs)
        self.tabs.add(self.tab1,text="Libary Management")
        self.tabs.add(self.tab2,text="Statistics")

        #list books
        self.list_books= Listbox(self.tab1,width=40,height=30,bd=5,font="time 12 bold")
        self.sb=Scrollbar(self.tab1,orient=VERTICAL)
        self.list_books.grid(row=0,column=0,padx=(10,0),pady=10,sticky=N)
        self.sb.config(command=self.list_books.yview)
        self.list_books.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0,column=0,sticky=N+S+E)
        #detail
        self.list_details=Listbox(self.tab1,width=80,height=30,bd=5,font='time 12 bold')
        self.list_details.grid(row=0,column=1,padx=(10,0),pady=10,sticky=N)

        #tab2

        self.lbl_book_count=Label(self.tab2,text="",pady=20,font="verdana 14 bold")
        self.lbl_book_count.grid(row=0)
        self.lbl_member_count=Label(self.tab2,text="",pady=20,font="verdana 14 bold")
        self.lbl_member_count.grid(row=1, sticky=W)
        self.lbl_taken_count=Label(self.tab2,text="",pady=20,font="verdana 14 bold")
        self.lbl_taken_count.grid(row=2, sticky=W)

    def addBook(self):
        add=addbook.AddBook()

def main():
    root = Tk()
    app = Main(root)
    root.title("Final Project: Library Management") 
    root.geometry("1350x750+350+200")
    root.mainloop()

if __name__ == "__main__":
    main()