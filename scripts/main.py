import os
import re
import zipfile
import shutil

def list_files(directory: str) -> None:
    try:
        files = os.listdir(directory)
        print("Files in directory:", directory)
        for file in files:
            print(file)
    except Exception as e:
        print(f"Error occurred: {e}")

def natural_sort_key(s: str) -> str:
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def copy_file(source_file: str, destination_file: str) -> None:
    try:
        shutil.copyfile(source_file, destination_file)
        print(f"File '{source_file}' copied to '{destination_file}' successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

def move_files(source_folder: str, destination_folder: str) -> None:
    # List all files in the source folder
    files = os.listdir(source_folder)
    # Move each file to the destination folder
    for file in files:
        source_file_path = os.path.join(source_folder, file)
        destination_file_path = os.path.join(destination_folder, file)
        shutil.move(source_file_path, destination_file_path)
        print(f"Moved: {source_file_path} to {destination_file_path}")


def count_files_in_folder(folder_path: str) -> int:
    # List all files in the folder
    files = os.listdir(folder_path)
    # Count the number of files
    num_files = len(files)
    return num_files

def final_folder_to_manga_name_folder(folder_path: str, manga_name: str) -> None:
    # Create a folder named "Chainsaw man" if it doesn't exist
    manga_name_folder = os.path.join(folder_path, manga_name)
    final_folder = os.path.join(manga_name_folder, 'final')
    # Rename final_folder to manga_name_folder    
    end_folder_name = os.path.join(manga_name_folder, manga_name)
    os.rename(final_folder, end_folder_name)
    print(f"Renamed {final_folder} to {end_folder_name}")

    # Zip manga_name_folder
    shutil.make_archive(end_folder_name, 'zip', root_dir=folder_path, base_dir=manga_name)

    # Rename the zip file to .cbz
    os.rename(f"{end_folder_name}.zip", f"{end_folder_name}.cbz")
    print(f"Renamed {end_folder_name}.zip to {end_folder_name}.cbz")


def rename_cbz_to_zip(folder_path: str, manga_name: str) -> None:
    
    # Create a folder named "Chainsaw man" if it doesn't exist
    manga_name_folder = os.path.join(folder_path, manga_name)
    processing_folder = os.path.join(manga_name_folder, 'processing')
    final_folder = os.path.join(manga_name_folder, 'final')
    if not os.path.exists(manga_name_folder):
        os.mkdir(manga_name_folder)
        print(f"Created folder: {manga_name_folder}")
        # Create a folder inside this folder
        os.mkdir(processing_folder)
        print(f"Created folder: {processing_folder}")
        # Create a folder inside this folder
        os.mkdir(final_folder)
        print(f"Created folder: {final_folder}")
    
    # List all files in the folder
    files = sorted(os.listdir(folder_path), key=natural_sort_key)
    print(files)
    
    # Iterate over each file
    for file in files:
        if file.endswith('.cbz'):
            # Construct old and new file paths
            old_file_path = os.path.join(folder_path, file)
            new_file_path = os.path.join(folder_path, file.replace('.cbz', '.zip'))
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed {old_file_path} to {new_file_path}")

            # Unzip the file
            with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                zip_ref.extractall(processing_folder)
                print(f"Unzipped {new_file_path}")
            
            processing_count = count_files_in_folder(processing_folder)
            final_count = count_files_in_folder(final_folder)

            pages = sorted(os.listdir(processing_folder))
            addition_to_folder_name = final_count + 1

            for idx, page in enumerate(pages[:-1]):

                new_page_name = f"{addition_to_folder_name + idx}.jpg"

                old_page_path = os.path.join(processing_folder, page)
                new_page_path = os.path.join(final_folder, new_page_name)
                
                os.rename(old_page_path, new_page_path)
                print(f"Renamed {old_page_path} to {new_page_path}")

    

            # Call the function to move files
            move_files(processing_folder, final_folder)

            shutil.rmtree(processing_folder)
            print(f"Deleted all files from {processing_folder}")
    
    # list_files(manga_name_folder) - check files in dir 
    source_file = '/Users/mateuszbuziak/Dokumenty/Manga/0.jpg'
    destination_file = os.path.join(final_folder, os.path.basename(source_file))
    copy_file(source_file, destination_file)

    final_folder_to_manga_name_folder(folder_path, manga_name)


if __name__ == "__main__":
    manga_name = 'Chainsaw Man'
    folder_path = '/Users/mateuszbuziak/Dokumenty/Manga/Chainsaw Man/' # Change this to the path of your folder
    rename_cbz_to_zip(folder_path, manga_name)
