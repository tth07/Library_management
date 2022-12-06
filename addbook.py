from tkinter import *
from tkinter import messagebox
import sqlite3
con = sqlite3.connect('Library.db')
cur=con.cursor()

class AddBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+500+200")
        self.title("Add book")
        self.resizable(False,False)

        self.topFrame=Frame(self,height=150,bg="white")
        self.topFrame.pack(fill=X)

        self.bottomFrame=Frame(self,height=600,bg="#fcc324")
        self.bottomFrame.pack(fill=X)

        top_lbl_label=Label(self.topFrame,bg="white")
        top_lbl_label.place(x=120,y=10)
        heading=Label(self.topFrame, text="Add Book",font="arial 22 bold",fg='#003f8a',bg='white')
        heading.place(x=290,y=60)

        ############book name###########

        self.lbl_name=Label(self.bottomFrame,text="Name: ",font="arial 15 bold",fg='white',bg="#fcc324")
        self.lbl_name.place(x=40,y=40)
        self.ent_name=Entry(self.bottomFrame,width=30,bd=4)
        self.ent_name.insert(0,"Please enter Book Name: ")
        self.ent_name.place(x=150,y=45)

        ##############author name#############
        
        self.lbl_author=Label(self.bottomFrame,text="Author: ",font="arial 15 bold",fg='white',bg="#fcc324")
        self.lbl_author.place(x=40,y=80)
        self.ent_author=Entry(self.bottomFrame,width=30,bd=4)
        self.ent_author.insert(0,"Please enter Author Name: ")
        self.ent_author.place(x=150,y=85)

        #############book type################
        self.lbl_type=Label(self.bottomFrame,text="Type: ",font="arial 15 bold",fg='white',bg="#fcc324")
        self.lbl_type.place(x=40,y=120)
        self.ent_type=Entry(self.bottomFrame,width=30,bd=4)
        self.ent_type.insert(0,"Please enter Book Type: ")
        self.ent_type.place(x=150,y=125)

        ############book language########################
        self.lbl_language=Label(self.bottomFrame,text="Language: ",font="arial 15 bold",fg='white',bg="#fcc324")
        self.lbl_language.place(x=40,y=160)
        self.ent_language=Entry(self.bottomFrame,width=30,bd=4)
        self.ent_language.insert(0,"Please enter Book Language: ")
        self.ent_language.place(x=150,y=165)

        #########button####################
        button=Button(self.bottomFrame,text="Add Book",command=self.addBook)
        button.place(x=270,y=200)

    def addBook(self):
        name = self.ent_name.get()
        author = self.ent_author.get()
        type = self.ent_type.get()
        language = self.ent_language.get()

        if (name and author and type and language !=""):
            try:
                query="INSERT INTO 'books'(book_name,book_author,book_type,book_language) VALUES(?,?,?,?)"
                cur.execute(query,(name,author,type,language))
                con.commit()
                messagebox.showinfo("Success","Successful add to Library")
            except:
                messagebox.showinfo("Error","Cannot add to Library")
        else:
            messagebox.showinfo("Error","Fields Cannot be empty")












