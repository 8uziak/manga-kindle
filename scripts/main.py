from cbz_files_to_one_cbz import CbzFilesToOneCbz

if __name__ == "__main__":
    manga_name = 'Chainsaw Man'
    folder_path = '/Users/mateuszbuziak/Dokumenty/Manga/Chainsaw Man/' # Change this to the path of your folder
    CbzFilesToOneCbz.rename_cbz_to_zip(folder_path, manga_name)