'''
DAILY MOTIVATION ~by  https://github.com/nuras1999
This tool shows you a random motivational quote whenever the program is executed.
It is highly recommended to convert this python file into exe file.
Save the exe file in startup folder in windows so that whenever PC is turned on we see a motivational quote.
Add your favourite motivational quotes to the images folder.
IMAGES ARE RANDOMLY TAKEN FROM VARIOUS INSTAGRAM ACCOUNT.

'''
from tkinter.ttk import *                                   #For creating GUI windows and elements
from tkinter import *
from PIL import Image, ImageTk                              #For image
from os import listdir,path,rename                          #For path traversal
import os               
import random                                               #For random number generation

def renamingImages(dirName):
    allFiles = list()
    listOfFile = listdir(dirName)
    for entry in listOfFile:
    
        fullPath = path.join(dirName, entry)                #combining foldername and filename to create full path
        allFiles.append(fullPath)                           #all file names added to list
    for imageNames in allFiles:                             #randomizing all filenames
        posOfSlash=imageNames.rfind("\\")                   #last occurance of backslash(filename starts after this)
        posOfDot=imageNames.rfind(".")                      #last occurance of dot(filename ends before this)
        randomNumber=random.randint(0,999999)               #creating a random number
        newImageName=imageNames[:posOfSlash]+"\\"+str(randomNumber)+imageNames[posOfDot:]               #creating new filename in same path
        try:                
            os.rename(imageNames,newImageName)              #renaming to new name
        except:                                             #if that random filename aldready exists try other random number
            randomNumber=random.randint(0,999999)
            newImageName=imageNames[:posOfSlash]+"\\"+str(randomNumber)+imageNames[posOfDot:]
            os.rename(imageNames,newImageName)

def fetchRandomImage(dirName):
    allFiles = list()
    listOfFile = listdir(dirName)
    for entry in listOfFile:
        fullPath = path.join(dirName, entry) 
        allFiles.append(fullPath)   
    length=len(allFiles)                                    #finding number of elements
    ran=random.randint(0,length-1)                          #creating random number within the size inorder to use it as index
    newImg=allFiles[ran]                                    #picking a random image
    return newImg

def splashScreen(displayImage):
    window=Tk()                                             #create new window
    # window.title("Motivational Quotes")                   #Titlebar is removed so no need of this 
    window.geometry("450x550")                              #its width & height
    window.resizable(0,0)                                   #fixed size window can't resize
    window.configure(background = 'white')                  #background color of window
    
    load = Image.open(displayImage)                         #opening a image
    load = load.resize((430,430))                           #resizing to given width & height
    render = ImageTk.PhotoImage(load)
    img = Label(window, image=render,border=FALSE)
    img.image = render
    img.place(x=10, y=10)                                   #positioning it in fixed place

    width = 450
    height = 550
    wid = (window.winfo_screenwidth() // 2) - (width // 2)          #placing in hozizontal center of screen
    hei = (window.winfo_screenheight() // 2) - (height // 2)        #placing in vertical center of screen
    window.geometry('{}x{}+{}+{}'.format(width, height, wid, hei))  
    window.wm_attributes('-topmost',True)                           #show this window above any other software
    window.overrideredirect(True)                                   #revome titlebar. No close button and title

    txt=Label(window,text="Have a nice day", font=("Century gothic",25))        #text
    txt.place(x=90, y=450,width="275",height="50")                              #text position & size

    btn = ttk.Button(window, text = 'SURE',command = window.destroy)            #button 
    btn.place(x=190, y=505,width="70",height="30")                              #button position and size

    Style=ttk.Style()                                               #window style
    window.after(20000, window.destroy)                             #Window closes automatically after 15 sec
    window.mainloop()                                               #running this window

imageFolder="images"                                                #folder path wher images are present
renamingImages(imageFolder)                                         #renaming all images randomly
displayImage=fetchRandomImage(imageFolder)                          #picking a random pic
splashScreen(displayImage)                                          #display window