from manga_kindle.cbz_files_to_one_cbz import CbzFilesToOneCbz 
from manga_kindle.gui_functionality import GuiFunctionality
import tkinter as tk
from tkinter import Canvas, Entry, Button, PhotoImage
from tkinter.messagebox import showinfo


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.gui_functionality = GuiFunctionality()
        self.main = CbzFilesToOneCbz()
        
        self.window()
        self.background()
        self.clickable_here()
        self.button_custom_cover()
        self.button_add_directory()
        self.button_add_file()
        self.button_convert()

    def window(self):
        self.title('mangaKindle')
        self.geometry("700x700")

        self.iconPhoto = PhotoImage(file = self.gui_functionality.relative_to_assets("icon.png"))
        self.iconphoto(False, self.iconPhoto)
        
        self.configure(bg = "#FFFFFF")
        self.resizable(False, False)
       
    def background(self):
        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 700,
            width = 700,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            700.0,
            700.0,
            fill="#434343",
            outline="")
        
        self.canvas.create_text(
        178.0,
        73.0,
        anchor="nw",
        text="Need help? Check instructions ",
        fill="#FFFFFF",
        font=("Inter MediumItalic", 20 * -1)
        )
    
    def clickable_here(self):
        label = tk.Label(
            text="here",
            fg="#92B0FF",
            font=("Inter MediumItalic", 20),
            bg="#434343"         
        )
        label.place(x=450, y=69, anchor="nw")
        label.bind('<Button-1>', self.gui_functionality.here_instructions_md)

    def button_custom_cover(self):

        self.button_image_0 = PhotoImage(
            file=self.gui_functionality.relative_to_assets("button_0.png"))
        self.button_0 = Button(
            image=self.button_image_0,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: [self.entry_0.delete(0,"end"), self.entry_0.insert(0, self.gui_functionality.browseFilePlusDirectory())],
            relief="flat"
        )
        self.button_0.place(
            x=92.0,
            y=139.0,
            width=515.0,
            height=71.0
        )

        self.entry_image_0 = PhotoImage(
            file=self.gui_functionality.relative_to_assets("entry.png"))
        self.entry_bg_3 = self.canvas.create_image(
            348.5,
            238.5,
            image=self.entry_image_0
        )
        self.entry_0 = Entry(
            bd=0,
            bg="#4A4A4A",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_0.place(
            x=106.0,
            y=219.0,
            width=485.0,
            height=37.0
        )
        
    def button_add_directory(self):
        self.button_image_1 = PhotoImage(
            file=self.gui_functionality.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: [self.entry_1.delete(0,"end"), self.entry_1.insert(0, self.gui_functionality.browseDirectory())],
            relief="flat"
        )
        self.button_1.place(
            x=92.0,
            y=279.0,
            width=515.0,
            height=71.0
        )
        self.entry_image_1 = PhotoImage(
            file=self.gui_functionality.relative_to_assets("entry.png"))
        self.entry_bg_1 = self.canvas.create_image(
            348.5,
            378.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#4A4A4A",
            fg="white",
            highlightthickness=0
        )
        self.entry_1.place(
            x=106.0,
            y=359.0,
            width=485.0,
            height=37.0
        )

    def button_add_file(self):
        self.button_image_2 = PhotoImage(
            file=self.gui_functionality.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: [self.entry_2.delete(0,"end"), self.entry_2.insert(0, self.gui_functionality.browseFiles())],
            relief="flat"
        )
        self.button_2.place(
            x=91.0,
            y=419.0,
            width=515.0,
            height=71.0
        )
        self.entry_image_2 = PhotoImage(
            file=self.gui_functionality.relative_to_assets("entry.png"))
        self.entry_bg_2 = self.canvas.create_image(
            348.5,
            518.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#4A4A4A",
            fg="white",
            highlightthickness=0
        )
        self.entry_2.place(
            x=106.0,
            y=499.0,
            width=485.0,
            height=37.0
        )             

    def button_convert(self):
        button_image_3 = PhotoImage(
            file=self.gui_functionality.relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.convert(
                self.entry_0.get() if self.entry_0.get() != '' else None,
                self.entry_1.get() if self.entry_1.get() != '' else None, 
                self.entry_2.get() if self.entry_2.get() != '' else None
                ),
            relief="flat"
        )
        button_3.place(
            x=91.0,
            y=559.0,
            width=515.0,
            height=71.0
        )
        self.mainloop()
    
    def convert(self, entry_custom_cover, entry_add_directory, entry_add_file):
        try:
            self.main.rename_cbz_to_zip(entry_add_directory, entry_add_file, entry_custom_cover)
            showinfo("Window", "Conversion successful!")
        except TypeError:
            showinfo("Window", 'Add directory and/or Add file not filled in')
        except FileNotFoundError:
            showinfo("Window", "No such directory " + entry_add_directory)
        except OSError:
            showinfo("Window", "Can't create file " + entry_add_file)