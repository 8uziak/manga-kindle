from cbz_files_to_one_cbz import CbzFilesToOneCbz
from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog
import os


class GuiFunctionality:
    def __init__(self) -> None:    
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / 'gui_elements' 
        
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def browseDirectory(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            return directory_path

    def browseFiles(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            file_name = os.path.basename(file_path)
            return file_name