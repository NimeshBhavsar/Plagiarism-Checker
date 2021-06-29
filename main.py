import os
import matplotlib.pyplot as plt
from queue import PriorityQueue
import PreProcess as pp
import Calculate_Similarity as cs
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

l = {}
def ppcorpus():
    """Preprocess the corpus taking all .txt files in directory
        and calls the preprocessing class for each of them"""
    files = [doc for doc in os.listdir() if (doc.endswith('.txt') and (doc!='store.txt' and doc!='temp.txt'))]
    for doc in files:
        l[doc] = pp.Preprocess(doc).trig
def storeCorpus():
    """ Stores the preprocesed corpus in a text file
        to avoid the computational load of preprocessing
        every time"""
    target = open('store.txt', "w")
    target.write(str(l))
    target.close()
def loadCorpus():
    """Loads the preprocessed data"""
    ter = open('store.txt','r')
    s = ter.read()
    ter.close()
    l = eval(s)
    print('a',l)

master = Tk()
master.title("Plagiarism Checker") #title of the window
Label(master, text="File Name").grid(row=0)
Label(master, text="Input Text").grid(row=1)
master.geometry("800x650")
e1 = Entry(master) #text field to input file name 
#e1.get() to access the input value

e1.grid(row=0, column=1)

t = Text(master, width=75, height=35) #text field to input text to be checked
t.grid(row=1,column=1)
def Prepro():
    """ Calls the preprocessing functions"""
    ppcorpus()
    storeCorpus()
def helloCallBack(): #function that runs when we click the check button
    """ Gets the data from input boxes and preprocesses it
        adds the file to the corpus and finally graphs the
        plagiarism percentage in form of bar graph"""
    s = t.get("1.0",END)
    r = e1.get()
    r = r+'.txt'
    f=open(r,"w")
    f.write(s)
    f.close()
    inp = pp.Preprocess(r).trig
    X = []
    Y = []
    doc_rank = cs.CalcSim(l,inp).doc_rank
    for i in range(len(l)):
        item = doc_rank.get()
        Y.append(item[0])
        X.append(item[1])
    #graph the similarity
    fig = plt.subplots(figsize=(10, 5))
    plt.bar(X,Y, color='maroon',width = 0.9,align='center')
    plt.xlabel("Document Name") 
    plt.ylabel("Percentage Similarity") 
    plt.title("Similarity Plot")
    plt.xticks(rotation = 90)
    plt.tight_layout()
    plt.show()
    #master.destroy()
    '''Output Frame'''

check = ttk.Button(master, text='Check', command=helloCallBack) #check button
check.grid(row=2,column=1)

prep = ttk.Button(master, text='PreProcess', command=Prepro) #check button
prep.grid(row=3,column=1)

master.mainloop( )
