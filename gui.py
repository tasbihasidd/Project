from tkinter import*
from PIL import Image ,ImageTk # to integrate  jpg and jpeg images

import action1
import speech_to_text

def ask():
    # user = speech_to_text.speech_to_text()
    # bot = action1.action(user)
    # textbox.insert(END,'User: '+ user + '\n')
    # if bot is not None:
    #     textbox.insert(END, 'Bot: ' + str(bot) + '\n')
    # if bot == 'okay sir':
    #     root.destroy() # to shutdown the desktop ai assistant
     print('askingggg')

def delete():
    print('deletingg')
def send():
    print('sendingg')

def resize_image(width, height):
    # Open the original image
    original_image = Image.open('va.jpg')
    # Resize the image
    resized_image = original_image.resize((width, height))
    # Convert the resized image to PhotoImage
    photo_image = ImageTk.PhotoImage(resized_image)
    return photo_image
root = Tk()
root.title("Desktop Virtual Assistant")
root.geometry('600x675') # to set width and size of frame
root.resizable(False,False) #by making it false i cant resize it
root.config(bg='HotPink4')

#making frame for a picture and label
frame= LabelFrame(root, padx=10,pady=10,borderwidth=3,relief='raised')
frame.configure(bg='HotPink4')
frame.grid(row=0,column=1,padx=10,pady=10,sticky='nsew')
#adding text label
text_label = Label(frame,text='Desktop Virtual Assistant',font=('comic Sans ms',14,'bold'),bg='HotPink3')
text_label.grid(row=0,column=0,padx=10,pady=0)
#for image
resized_img = resize_image(200, 200)
image_label = Label(frame, image=resized_img)
image_label.grid(row=1, column=0,padx=10,pady=10,sticky='nsew')
# # Column and row configuration to make the frame expandable
frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
# Column configuration for the root window
root.columnconfigure(1, weight=1)

# Adding a textbox
textbox = Text(root,font='courier 10 bold',bg='HotPink3')
textbox.grid(row=2,column=0)
textbox.place(x=100,y=325,width=375,height=100)

#adding a entry bar
entry = Entry(root,justify=CENTER)
entry.place(x=100,y=450,width=375,height=30)

#adding buttons
button1= Button(root,text='Ask',bg='HotPink3',pady=16,padx=40,borderwidth=3,relief=SOLID,command=ask)
button1.place(x=70,y=500)
button2= Button(root,text='Delete',bg='HotPink3',pady=16,padx=40,borderwidth=3,relief=SOLID,command=delete)
button2.place(x=220,y=500)
button3= Button(root,text='Send',bg='HotPink3',pady=16,padx=40,borderwidth=3,relief=SOLID,command=send)
button3.place(x=380,y=500)



root.mainloop()