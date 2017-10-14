# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 22:46:23 2017

@author: ATUL
"""

from tkinter import *

root = Tk()

text1 = Text(root, height=20, width=30)
photo=PhotoImage(file='pic3.png')
text1.insert(END,'\n')
text1.image_create(END, image=photo)

text1.pack(side=LEFT)

text2 = Text(root, height=20, width=50)
scroll = Scrollbar(root, command=text2.yview)
text2.configure(yscrollcommand=scroll.set)
text2.tag_configure('bold_italics', font=('Arial', 11, 'bold', 'italic'))
text2.tag_configure('big', font=('Verdana', 18, 'bold'))
text2.tag_configure('color', foreground='#476042', 
						font=('Tempus Sans ITC', 12, 'bold'))

text2.insert(END,'\nMovies Reviews and Analysis\n', 'big')
quote = """\n
-the movie review is a popular way for critics to access a movie’s overall quality and determine whether or not they think movie is worth recommending.
"""
text2.insert(END, quote, 'color')

text2.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)
def analys():
    with open('simple analysis.py') as source:
        exec(source.read())

b=Button(root,text="Analysis",command= analys,padx=30,pady=15)
b.pack()
def genre():
    with open('genreanalysis.py') as source:
        exec(source.read())

a=Button(root,text="GENRE ANALYSIS",command= genre, justify=LEFT,padx=5,pady=15)
a.pack()
def pred():
    with open('IMDB rating prediction.py') as source:
        exec(source.read())

c=Button(root,text="IMDB Rating \nPrediction",command= pred,padx=16,pady=15)
c.pack()
def dire():
    with open('direc-actor.py') as source:
        exec(source.read())

d=Button(root,text="Directors & \n Actors\nAnalysis",command= dire,padx=18,pady=15)
d.pack()

root.title("Movies Reviews")
root.mainloop()