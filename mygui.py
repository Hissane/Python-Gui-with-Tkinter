from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Music")
root.iconbitmap(r'music_gsF_icon.ico')
root.geometry("800x500")
#root.iconbitmap("music.jpg")
root.config(background='#000000')

frame = Frame(root, bg='#727272')

def browseFile():
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("mp3 files", "*.mp3"), ("all files", "*.*")))
    print(root.filename)


button1 = Button(frame, text="Browse", bg='#ffffff', fg="black", command=browseFile)
button1.pack()

frame.pack(expand=YES)

root.mainloop()