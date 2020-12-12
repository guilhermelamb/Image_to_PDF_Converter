from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


#Starting the code
root = tk.Tk()


#Setting the canvas
canvas1 = tk.Canvas(root, width = 300, height = 300, bg ='whitesmoke', relief='raised')
canvas1.pack()


#Setting the label
label1 = tk.Label(root, text = "Image to PDF converter", bg = 'whitesmoke')
label1.config(font=("Arial", 20))
canvas1.create_window(150, 60, window=label1)


#Creating a function to get the file
def GetFile():
    global img1
    
    get_file_path = filedialog.askopenfilename()
    image1 = Image.open(get_file_path)
    img1 = image1.convert("RGB")
 
    
#Setting the get file button
getfilebutton = tk.Button(root, text = "Select file", command = GetFile, bg = 'DarkOliveGreen3',\
                          fg = 'black', font=('Arial', 12, 'bold'))
canvas1.create_window(150, 130, window = getfilebutton)    

#Creating a function to save the file
def SaveFile():
    global img1
    
    save_file_path = filedialog.asksaveasfilename(defaultextension = '.pdf')
    img1.save(save_file_path)
    
#Setting the save button
savefilebutton = tk.Button(root, text = "Convert to PDF", command = SaveFile, bg = 'DarkOliveGreen3',\
                           fg = 'black', font=('Arial', 12, 'bold'))
canvas1.create_window(150, 180, window = savefilebutton)


#Creating a function to exit the app
def ExitApp():
    MsgBox = tk.messagebox.askquestion("Exit", "Are you sure you want to exit?", icon = 'warning')
    if MsgBox == 'yes':
        root.destroy()


#Creating an exit button
exitbutton = tk.Button(root, text = 'Exit', command = ExitApp, bg = 'DarkOliveGreen3',\
                       fg = 'black', font=('Arial', 12, 'bold'))
canvas1.create_window(150, 230, window = exitbutton)

root.mainloop()

