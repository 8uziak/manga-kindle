
from cbz_files_to_one_cbz import CbzFilesToOneCbz
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r'/Users/mateuszbuziak/Code/manga-kindle/scripts/gui_elements')


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def browseDirectory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        print("Selected Directory:", directory_path)	

def browseFiles():
    file_name = filedialog.askopenfilename()
    if file_name:
        print("Selected File:", file_name)

window = Tk()

window.geometry("700x700")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
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
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=browseDirectory,
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
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=browseFiles,
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
    file=relative_to_assets("button_3.png"))
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
window.resizable(False, False)
window.mainloop()
