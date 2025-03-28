from customtkinter import *
from customtkinter import CTkLabel
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os

# x----------------RESOURCES----------------x

DARK_OLIVE = '#2C3930'
OLIVE = '#3F4F44'
OCHRE = '#A27B5C'
LIGHT_GREY = '#DCD7C9'
FONT_NAME = 'Lucida Calligraphy'

# x----------------MECHANISM----------------x

file = ''

def upload_image():
    global file
    file = filedialog.askopenfilename(filetypes =[('JPG File', '*.jpg'), ('PNG File', '*.png')])
    filename = file.split('/')[-1]
    if file is not None:
        file_name = CTkLabel(root,
                             text=f'Image Loaded: {filename}',
                             text_color=LIGHT_GREY,
                             font=(FONT_NAME, 13))
        file_name.grid(row=4, column=1)

def submit_image():
    global file
    image = Image.open(file)
    image = image.convert("RGBA")
    width, height = image.size
    font = ImageFont.truetype("arial.ttf", 50)

    text = input_text.get()

    text_img = Image.new("RGBA", (width-20, height-20), (255, 255, 255, 0))
    text_draw = ImageDraw.Draw(text_img)
    text_draw.text((width //4, height//4), font=font, fill=(255, 255, 255, 170), anchor='ms', text=text)

    text_img = text_img.rotate(45, expand=True)

    image.paste(text_img, (50,50), text_img)

    for widget in root.winfo_children():
        widget.destroy()

    file_name = file.split('/')[-1]
    file_name=file_name.split('.')[0]
    try:
        filepath = f'C:/Users/Admin/Pictures/Watermarked/{file_name}_watermarked.png'
        image.save(filepath)
    except FileNotFoundError:
        os.mkdir('C:/Users/ADMIN/Pictures/Watermarked')
        filepath = f'C:/Users/Admin/Pictures/Watermarked/{file_name}_watermarked.png'
        image.save(filepath)

    image.show()

    new_label = CTkLabel(root,
                         text=f'Your file has been saved to the path: \n\n\n\n{filepath}',
                         font=(FONT_NAME, 16, 'bold'),
                         wraplength=370)
    new_label.grid(padx=20,pady=20)



# x----------------UI SETUP----------------x

root = CTk()
root.title('Image Watermarking App')
root.geometry('450x250')
root.configure(padx=25, pady=25, fg_color=DARK_OLIVE)

welcome = CTkLabel(root, text='Welcome to watermarking your images!',
                font=(FONT_NAME, 16, "bold"),
                pady=15,
                padx=15,
                text_color=LIGHT_GREY)
welcome.grid(row=0, column=1)

input_label = CTkLabel(root,
                       text='Please input your text below.',
                       font=(FONT_NAME, 15),
                       padx=15,
                       pady=15,
                       text_color=LIGHT_GREY)
input_label.grid(row=1,column=1 )

input_text = CTkEntry(root,
                      width=150,
                      fg_color=OLIVE,
                      corner_radius=15,
                      border_color=OCHRE,
                      font=(FONT_NAME, 12))
input_text.grid(row=2, column=1)

button_frame = CTkFrame(root, fg_color=DARK_OLIVE)
button_frame.grid(row=3, column=1, pady=15)

upload_button = CTkButton(button_frame, text='Upload an image',
                   font=(FONT_NAME, 12),
                   corner_radius=15,
                   fg_color=OCHRE,
                   hover_color=OLIVE,
                   text_color='white',
                   command=upload_image)
upload_button.pack(side="left", padx=10)

submit_button = CTkButton(button_frame,
                   text='Submit the image',
                   font=(FONT_NAME, 12),
                   corner_radius=15,
                   fg_color=OCHRE,
                   hover_color=OLIVE,
                   text_color='white',
                   command=submit_image)
submit_button.pack(side="right", padx=10)


root.mainloop()