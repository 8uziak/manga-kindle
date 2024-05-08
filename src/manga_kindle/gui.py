from manga_kindle.cbz_files_to_one_cbz import CbzFilesToOneCbz 
from manga_kindle.gui_functionality import GuiFunctionality
import tkinter as tk
from tkinter import Canvas, Entry, Button, PhotoImage
from tkinter.messagebox import showinfo

class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.gui_functionality = GuiFunctionality()

        self.title('mangaKindle')
        self.geometry("700x700")

        iconPhoto = PhotoImage(file = self.gui_functionality.relative_to_assets("icon.png"))
        self.iconphoto(False, iconPhoto)
        
        self.configure(bg = "#FFFFFF")
        self.main = CbzFilesToOneCbz()

        canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 700,
            width = 700,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_rectangle(
            0.0,
            0.0,
            700.0,
            700.0,
            fill="#434343",
            outline="")

        button_image_1 = PhotoImage(
            file=self.gui_functionality.relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: [entry_1.delete(0,"end"), entry_1.insert(0, self.gui_functionality.browseDirectory())],
            relief="flat"
        )
        button_1.place(
            x=92.0,
            y=279.0,
            width=515.0,
            height=71.0
        )


        entry_image_1 = PhotoImage(
            file=self.gui_functionality.relative_to_assets("entry.png"))
        entry_bg_1 = canvas.create_image(
            348.5,
            378.5,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#4A4A4A",
            fg="white",
            highlightthickness=0
        )
        entry_1.place(
            x=106.0,
            y=359.0,
            width=485.0,
            height=37.0
        )

        button_image_2 = PhotoImage(
            file=self.gui_functionality.relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: [entry_2.delete(0,"end"), entry_2.insert(0, self.gui_functionality.browseFiles())],
            relief="flat"
        )
        button_2.place(
            x=91.0,
            y=419.0,
            width=515.0,
            height=71.0
        )

        entry_image_2 = PhotoImage(
            file=self.gui_functionality.relative_to_assets("entry.png"))
        entry_bg_2 = canvas.create_image(
            348.5,
            518.5,
            image=entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#4A4A4A",
            fg="white",
            highlightthickness=0
        )
        entry_2.place(
            x=106.0,
            y=499.0,
            width=485.0,
            height=37.0
        )             

        button_image_3 = PhotoImage(
            file=self.gui_functionality.relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.convert(
                entry_1.get() if entry_1.get() != '' else None, 
                entry_2.get() if entry_2.get() != '' else None
                ),
            relief="flat"
        )
        button_3.place(
            x=91.0,
            y=559.0,
            width=515.0,
            height=71.0
        )
        self.resizable(False, False)
        self.mainloop()
    
    def convert(self, entry_add_directory, entry_add_file):
        try:
            self.main.rename_cbz_to_zip(entry_add_directory, entry_add_file)
            showinfo("Window", "Conversion successful!")
        except TypeError:
            showinfo("Window", 'Entry 1 or Entry 2 not filled in')
        except FileNotFoundError:
            showinfo("Window", "No such directory " + entry_add_directory)
        except OSError:
            showinfo("Window", "Can't create file " + entry_add_file)