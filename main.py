from tkinter import *
import tkinter.filedialog
import tkinter.messagebox as tmsg
from PIL import Image
from PIL import ImageTk
import cv2
from preprocessing import preprocess

def print_path():
    global f
    f = tkinter.filedialog.askopenfilename(
        parent=root,
        initialdir='',
        title='Select file',
        filetypes=[('jpg image', '.jpg')]
    )
    img1 = cv2.imread(f)
    newimg = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    newimg = cv2.resize(newimg, (512,512))
    cv2.putText(newimg,'Original',(5,25),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)
    img = Image.fromarray(newimg)
    imgtk = ImageTk.PhotoImage(image=img)
    x.imgtk = imgtk
    x.configure(image=imgtk)

def process():
    img_processed = preprocess(rf'{f}')
    cv2.putText(img_processed,'Preprocessed',(5,25),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)
    img = Image.fromarray(img_processed)
    imgtk = ImageTk.PhotoImage(image=img)
    y.imgtk = imgtk
    y.configure(image=imgtk)

root = Tk()
root.geometry("1200x750")
root.title("Image Preprocessing")
root.resizable(0, 0)

MF = Frame(root, bd=8, bg="lightgray", relief=GROOVE)
MF.place(x=0, y=0, height=50, width=1200)

menu_label = Label(MF, text="Image Preprocessing", font=("times new roman", 20, "bold"), bg="lightgray", fg="black", pady=0)
menu_label.pack(side=TOP, fill="x")

# Create a frame for buttons
button_frame = Frame(root)
button_frame.grid(row=1, column=0, pady=10)

# "Select Image" button
b1 = Button(button_frame, font=("times new roman", 20, "bold"), text='Select Image', command=print_path)
b1.grid(row=0, column=0, padx=10)

# "Preprocess" button
b2 = Button(button_frame, font=("times new roman", 20, "bold"), text='Preprocess', command=process)
b2.grid(row=0, column=1, padx=10)

# Create a frame for displaying images
image_frame = Frame(root)
image_frame.grid(row=0, column=0, padx=50, pady=50)

x = Label(image_frame, image=None)
x.grid(row=0, column=0, padx=10)

y = Label(image_frame, image=None)
y.grid(row=0, column=1, padx=10)

root.mainloop()
