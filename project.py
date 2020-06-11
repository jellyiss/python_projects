# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:20:00 2020

@author: JellyIss
"""

from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random

root = Tk()
root.title('Grammar exercise!')
root.iconbitmap('images/sunny.ico')
root.geometry("800x800")

def snoopy():
    global da_snoopy
    da_snoopy = ImageTk.PhotoImage(Image.open("images/snoopy.png"))
    show_snoopy.config(image=da_snoopy, bg = '#F0C4D8')

def welcome():
    hide_frames()
    main_frame.pack(fill='both', expand=1)
    hello_label = Label(main_frame, text="Welcome to Grammar Exercise!",font=("Alef", 15), bg='#F0C4D8').pack()
    app_label = Label(main_frame, text="This application enables you to practise your grammar skills!", font=("Alef", 12), bg='#F0C4D8').pack()
    instr_label = Label(main_frame, text="Choose from the menu what do you want to practise!", font=("Alef", 12), bg = '#F0C4D8').pack()
    global show_snoopy
    show_snoopy = Label(main_frame)
    show_snoopy.pack(pady=5)
    author_button = Button(main_frame, text = "About author", command = author, font=("Alef", 12), bg= '#F0C4D8').pack()
    snoopy()

def ma_pic():
    global da_my
    da_my = ImageTk.PhotoImage(Image.open("images/my_pic.jpg"))
    show_me.config(image = da_my, bg = '#F0C4D8')

def author():
    hide_frames()
    author_frame.pack(fill='both', expand=1)
    global show_me
    show_me = Label(author_frame)
    show_me.pack(pady=5)
    name_label = Label(author_frame, text="Izabella Kasprolewicz",font=("Alef", 12), bg='#F0C4D8').pack()
    what_label = Label(author_frame, text="English Linguistics: Theories, Interfaces, Technologies", font=("Alef", 12), bg='#F0C4D8').pack()
    course_label = Label(author_frame, text ="IT skills for linguists", font=("Alef", 12), bg='#F0C4D8').pack()
    lecturer_label = Label(author_frame, text = "Lecturer: Grzegorz Aperliński", font=("Alef", 12), bg='#F0C4D8').pack()
    back_button = Button(author_frame, text = "Go back to Welcome screen", command = welcome, font=("Alef", 12), bg='#F0C4D8').pack(pady=15)
    ma_pic()                       
    
def articles_answer():
    if article_radio.get() == my_pictures_articles[answer]:
        response = "Correct! Go to the next one!"
        pass_button = Button(articles_frame, text="Next", command=articles, font=("Alef", 12), bg='#F0C4D8').pack()
    else:
        response = "Incorecct! Try again!"
    
    answer_article_label.config(text=response)
    
    

#Create articles function

def articles():
    hide_frames()
    articles_frame.pack(fill="both", expand=1)
    my_label = Label(articles_frame, text = "Choose the correct article: a, an, the or -(no article)", font=("Alef", 15), bg='#F0C4D8').pack()
    
    
    global show_picture
    show_picture = Label(articles_frame)
    show_picture.pack(pady=5)

    global my_pictures
    my_pictures = ['engineer', 'historybooks', 'love', 'nicegirl', 'party', 'restaurant', 'sickman', 'tvset', 'uglydress', 'video']
    
    
    
    global my_pictures_articles
    my_pictures_articles = {
    'engineer':'an',
    'historybooks':'-',
    'love':'-',
    'nicegirl':'a',
    'party':'the',
    'restaurant':'the',
    'sickman':'the',
    'tvset':'a',
    'uglydress':'an',
    'video':'the'
    }

    answer_list = []
    count = 1
    global answer

    rando = randint(0, len(my_pictures)-1)
    while count == 1:
            answer = my_pictures[rando]
            global my_pictures_image
            picture = "images/" + my_pictures[rando] + ".png"
            my_pictures_image = ImageTk.PhotoImage(Image.open(picture))
            show_picture.config(image=my_pictures_image)
            
            answer_list.append(my_pictures[rando])
            my_pictures.remove(my_pictures[rando])
            random.shuffle(my_pictures)
            count += 1
            
    global answer_article_label 
    answer_article_label = Label(articles_frame, text="", font=("Alef", 15), bg='#F0C4D8')
    answer_article_label.pack(pady=5)
    
    global article_radio
    article_radio = StringVar()
    article_radio.set("a")
    article_radio_button1=Radiobutton(articles_frame, text="a", variable=article_radio, value="a", font=("Alef", 12), bg='#F0C4D8').pack()
    article_radio_button2=Radiobutton(articles_frame, text="an", variable=article_radio, value="an", font=("Alef", 12), bg='#F0C4D8').pack()
    article_radio_button3=Radiobutton(articles_frame, text="the", variable=article_radio, value="the", font=("Alef", 12), bg='#F0C4D8').pack()
    article_radio_button4=Radiobutton(articles_frame, text="-", variable=article_radio, value="-", font=("Alef", 12), bg='#F0C4D8').pack()
    #button to answer
    article_answer_button = Button(articles_frame, text="Answer", command= articles_answer, font=("Alef", 12), bg='#F0C4D8').pack(pady=5)
    

    
def random_wordbuilding():
    
    global my_pictures_word
    my_pictures_word = ['responsibility', 'announcement', 'death', 'laughter', 'loss', 'behaviour', 'complaint', 'arrival', 'disappearance', 'astonishment']
    
    #generate a random number
    global randobuild
    randobuild = randint(0, len(my_pictures_word)-1)
    wordbuild = "images/" + my_pictures_word[randobuild] + ".png"
    #Create Images
    global wordbuild_img
    wordbuild_img = ImageTk.PhotoImage(Image.open(wordbuild))
    show_img1.config(image=wordbuild_img)

def wordbuild_answer():
    answer1 = answer_input1.get()
    
    if answer1.lower() == my_pictures_word[randobuild]:
        response = "Correct! Go to the next one!"
        rando_button1 = Button(wordbuilding_frame, text="Next",font=("Alef", 12),bg = '#F0C4D8', command =wordbuilding).pack()
    else:
        response = "Incorrect!"
        
    answer_label1.config(text=response)
    
    answer_input1.delete(0,'end')


    
#create word building function
def wordbuilding():
    hide_frames()
    wordbuilding_frame.pack(fill="both", expand=1)
    my_label1 = Label(wordbuilding_frame, text = "Use the words in brackets to form a new word that fits into each blank", font=("Alef", 15), bg='#F0C4D8').pack()
    
    global show_img1
    show_img1 = Label(wordbuilding_frame)
    show_img1.pack(pady=5)
    random_wordbuilding()
    
    #Label for comment about answer
    global answer_label1
    answer_label1 = Label(wordbuilding_frame, text="",font=("Alef", 12), bg='#F0C4D8')
    answer_label1.pack(pady=5)
    
    #Entry 
    global answer_input1
    answer_input1 = Entry(wordbuilding_frame, font=("Alef", 12),bd=2)
    answer_input1.pack(pady=5)
    
    
    #create Button for answer
    answer_button1 = Button(wordbuilding_frame, text="Check Answer",font=("Alef", 12), command=wordbuild_answer, bg='#F0C4D8')
    answer_button1.pack(pady=5)
    
#hide previous frames
def hide_frames():
    #loop for previous frames
    for widget in articles_frame.winfo_children():
        widget.destroy()
        
    for widget in wordbuilding_frame.winfo_children():
        widget.destroy()
        
    for widget in main_frame.winfo_children():
        widget.destroy()
    
    for widget in author_frame.winfo_children():
        widget.destroy()
        
    articles_frame.pack_forget()
    wordbuilding_frame.pack_forget()
    main_frame.pack_forget()
    author_frame.pack_forget()

#Create menu

my_menu = Menu(root)
root.config(menu=my_menu)

#Create menu items
main_menu = Menu(my_menu)
my_menu.add_cascade(label="Practise", menu=main_menu)
main_menu.add_command(label = "Welcome!", command=welcome)
main_menu.add_command(label = "Articles", command=articles)
main_menu.add_command(label = "Word bulding", command=wordbuilding)
main_menu.add_separator()
main_menu.add_command(label="Exit", command=root.quit)


#create frames
main_frame = Frame(root, width=800, height=800, bg='#C4F0DC')
author_frame = Frame(root, width=800, height=800, bg ='#C4F0DC')
articles_frame = Frame(root, width=800, height=800, bg='#C4F0DC')
wordbuilding_frame = Frame(root, width=800, height=800, bg='#C4F0DC')

welcome()
root.mainloop()