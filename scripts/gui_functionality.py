from cbz_files_to_one_cbz import CbzFilesToOneCbz
from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog


class GuiFunctionality:
    def __init__(self) -> None:    
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r'/Users/mateuszbuziak/Code/manga-kindle/scripts/gui_elements')

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def browseDirectory(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            print("Selected Directory:", directory_path)	

    def browseFiles(self):
        file_name = filedialog.askopenfilename()
        if file_name:
            print("Selected File:", file_name)

    