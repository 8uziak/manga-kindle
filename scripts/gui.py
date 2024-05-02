
from cbz_files_to_one_cbz import CbzFilesToOneCbz
from gui_functionality import GuiFunctionality
from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog

class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.gui_functionality = GuiFunctionality()

        self.geometry("700x700")
        self.configure(bg = "#FFFFFF")

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

        # 'ADD DIRECTORY' button
        button_image_1 = PhotoImage(
            file=self.gui_functionality.relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.gui_functionality.browseDirectory,
            relief="flat"
        )
        button_1.place(
            x=92.0,
            y=315.0,
            width=515.0,
            height=71.0
        )

        # 'ADD FILE' button
        button_image_2 = PhotoImage(
            file=self.gui_functionality.relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.gui_functionality.browseFiles,
            relief="flat"
        )
        button_2.place(
            x=92.0,
            y=437.0,
            width=515.0,
            height=71.0
        )

        # 'CONVERT' button
        button_image_3 = PhotoImage(
            file=self.gui_functionality.relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"), #TODO CbzFilesToOneCbz
            relief="flat"
        )
        button_3.place(
            x=92.0,
            y=559.0,
            width=515.0,
            height=71.0
        )
        self.resizable(False, False)
        self.mainloop()

if __name__ == "__main__":
    Gui()