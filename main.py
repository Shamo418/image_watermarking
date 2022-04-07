from PIL import ImageDraw, ImageFont
import tkinter
from tkinter import *
from tkinter import filedialog
from PIL import Image

THEME_COLOR = "#375362"
margin = 20
text_font = ImageFont.truetype('tahoma.ttf', 24)


class ImageTooling:
    def __init__(self):
        self.widht = 0
        self.height = 0
        self.textwidth = 0
        self.textheight = 0

    def open_image(self):
        filetypes = (
            ('jpg files', '*.jpg'),
            ('jpeg files', '*.jpeg'),
            ('gif files', '*.gif'),
            ('All files', '*.*')
        )
        self.file_name = filedialog.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes
        )
        self.im = Image.open(self.file_name)
        self.widht = self.im.size[0]
        self.height = self.im.size[1]
        self.im.show()

    def image_dimensions(self):
        return self.widht, self.height

    def add(self):
        try:
            text_font = ImageFont.truetype('tahoma.ttf', 24)
            draw = ImageDraw.Draw(self.im)
            text = entry_text.get()
            self.textwidth, self.textheight = draw.textsize(text, text_font)
            # draw watermark
            draw.text((x_y_dict['x'], x_y_dict['y']), text, font=text_font)
            self.im.save('images/watermark.jpg')
            self.im.show()

        except AttributeError:
            tkinter.messagebox.showinfo("Error", "Please load a picture")

    def text_dimmensions(self):
        return self.textwidth, self.textheight


def radio_used():
    pass


def right_bottom():
    dimmension = test_image.image_dimensions()
    text_size = test_image.text_dimmensions()
    x_y_dict['x'] = dimmension[0] - text_size[0] - margin
    x_y_dict['y'] = dimmension[1] - text_size[1] - margin


def left_upper_corner():
    x_y_dict['x'] = margin
    x_y_dict['y'] = margin


def right_upper_corner():
    dimmension = test_image.image_dimensions()
    text_size = test_image.text_dimmensions()
    x_y_dict['x'] = dimmension[0] - text_size[0] - margin
    x_y_dict['y'] = margin


def left_bottom():
    dimmension = test_image.image_dimensions()
    text_size = test_image.text_dimmensions()
    x_y_dict['x'] = margin
    x_y_dict['y'] = dimmension[1] - text_size[1] - margin


x_y_dict = {
    'x': 0,
    'y': 0
}

test_image = ImageTooling()
screen = tkinter.Tk()
screen.title("Watermark_image")
screen.config(bg=THEME_COLOR, padx=20, pady=20)

# Entries
entry_text = tkinter.Entry(width=35)
entry_text.insert(END, string='Insert a text of watermark:)')
entry_text.grid(column=0, row=0, padx=20, pady=10)

# Buttons
button_open_image = tkinter.Button(text='Open image', command=test_image.open_image, width=30)
button_open_image.grid(column=0, row=1, padx=20, pady=10)
button_add_watermark = tkinter.Button(text='Add watermark', command=test_image.add, width=30)
button_add_watermark.grid(column=0, row=2, padx=20, pady=10)

# Radiobuttons

# Variable to hold on to which radio button value is checked.
radio_state = IntVar()

rb_corner_1 = tkinter.Radiobutton(text="Left upper corner", value=1, variable=radio_state,
                                  command=left_upper_corner, width=30)
rb_corner_1.grid(column=0, row=4, padx=0, pady=0)
rb_corner_2 = tkinter.Radiobutton(text="Right upper corner", value=2, variable=radio_state,
                                  command=right_upper_corner, width=30)
rb_corner_2.grid(column=0, row=5, padx=0, pady=0)
rb_corner_3 = tkinter.Radiobutton(text="Left bottom corner", value=3, variable=radio_state,
                                  command=left_bottom, width=30)
rb_corner_3.grid(column=0, row=6, padx=0, pady=0)
rb_corner_4 = tkinter.Radiobutton(text="Right bottom corner", value=4, variable=radio_state,
                                  command=right_bottom, width=30)
rb_corner_4.grid(column=0, row=7, padx=0, pady=0)

# labels
corner_label = tkinter.Label(text='Which corner of the photo you \n want the watermark to be on?',
                             width=30)
corner_label.grid(column=0, row=3, )

screen.mainloop()
