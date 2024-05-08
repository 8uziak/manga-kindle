from pathlib import Path
from tkinter import filedialog
import os
import webbrowser


class GuiFunctionality:
    def __init__(self) -> None:    
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / 'gui_elements' 
        
    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    def browseFilePlusDirectory(self):
        file_with_directory_name = filedialog.askopenfilename()
        if file_with_directory_name:
            return file_with_directory_name

    def browseDirectory(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            return directory_path

    def browseFiles(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            file_name = os.path.basename(file_path)
            return file_name
    
    def here_instructions_md(self, event):
        instructions = ("https://github.com/8uziak/manga-kindle/blob/master/docs/instructions.md")
        webbrowser.open_new_tab(instructions)
