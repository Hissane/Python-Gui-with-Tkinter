from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk,Image

root = Tk()
root.title("Music")
root.iconbitmap(r'music_gsF_icon.ico')
root.geometry("800x500")
root.config(background='#000000')

frame = Frame(root, bg='#000000')
left_frame = Frame(root, bg='#000000')
right_frame = Frame(root, bg='#000000')
frame2 = Frame(root, bg='#000000')

def browseFile():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
    text_box.insert(END, root.filename)
    print(root.filename)

def displayRock():
	messagebox.showinfo("Information","This is a rock song")

browse_button = Button(frame, text="Browse", bg='#ffffff', fg="black", command=browseFile)
#.grid(row=0, column=1)
browse_button.pack(side = RIGHT)

text_box = Text(frame, height=1, width=30)
#.grid(row=0, column=0, padx=5, pady=200)
text_box.pack()

bg_button = Button(frame2, text="Predict", bg='#ffffff', fg="black", command=displayRock)
bg_button.pack()

frame.pack(expand=YES)
frame2.pack(expand=YES, fill=Y)

root.mainloop()