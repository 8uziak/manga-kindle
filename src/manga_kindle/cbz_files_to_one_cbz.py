import os
import re
import zipfile
import shutil
import uuid
from tkinter.messagebox import showinfo

class CbzFilesToOneCbz:
    def __init__(self, folder_path: str, manga_name: str, custom_cover_path: str | None) -> None:
        self.folder_path = folder_path
        self.manga_name = manga_name
        self.custom_cover_path = custom_cover_path
        self.manga_name_folder = os.path.join(self.folder_path, manga_name)

        self.copy_cbz_files = os.path.join(self.manga_name_folder, self.create_unique_folder_name('cbz_copy_file'))
        self.processing_folder = os.path.join(self.manga_name_folder, self.create_unique_folder_name('processing'))
        self.final_folder = os.path.join(self.manga_name_folder, self.create_unique_folder_name('final'))

        self.create_folders_to_process_operation(self.manga_name_folder)
        self.create_folders_to_process_operation(self.copy_cbz_files)
        self.create_folders_to_process_operation(self.processing_folder)
        self.create_folders_to_process_operation(self.final_folder)

        self.move_files_from_source_dir_to_temporary_folder(self.folder_path, self.copy_cbz_files)
        self.rename_cbz_to_zip(self.copy_cbz_files, self.processing_folder, self.final_folder)
        self.list_files(self.manga_name_folder)
        self.remove_temp_workpath(self.copy_cbz_files)

        if self.custom_cover_path:
            self.custom_cover(self.custom_cover_path, self.final_folder)

        self.final_folder_to_manga_name_folder(self.folder_path, self.create_unique_folder_name(manga_name))

    def create_unique_folder_name(self, folder_name: str | None):
        folder_name_with_uuid = folder_name + '-' + str(uuid.uuid4())
        if os.path.exists(os.path.join(self.manga_name_folder, folder_name)):
            if os.path.exists(os.path.join(folder_name_with_uuid)):
                self.create_unique_folder_name(folder_name_with_uuid)
            else:
                return folder_name_with_uuid
        return folder_name

    def create_folders_to_process_operation(self, folder_name: str | None) -> None:
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            print(f"Created folder: {folder_name}")

    def move_files_from_source_dir_to_temporary_folder(self, folder_path: str, copy_cbz_files: str) -> None:
        files = os.listdir(folder_path)
        for file in files:
            if file.endswith('.cbz'):
                folder_path_file = os.path.join(folder_path, file)
                copy_cbz_files_file = os.path.join(copy_cbz_files, file)
                self.copy_file_from_one_destination_to_other_destination(folder_path_file, copy_cbz_files_file)

    def list_files(self, directory: str) -> None:
        try:
            files = os.listdir(directory)
            print("Files in directory:", directory)
            for file in files:
                print(file)
        except FileNotFoundError:
            showinfo(f"Error: Directory '{directory}' not found.")
        except PermissionError:
            showinfo(f"Error: Permission denied for directory '{directory}'.")
        except OSError as e:
            showinfo(f"Error: {e}")
        except Exception as e:
            showinfo(f"An unexpected error occurred: {e}")

    def natural_sort_key(self, s: str) -> str:
        return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

    def copy_file_from_one_destination_to_other_destination(self, source_file: str, destination_file: str) -> None:
        try:
            shutil.copyfile(source_file, destination_file)
            print(f"File '{source_file}' copied to '{destination_file}' successfully.")
        except (shutil.SameFileError, shutil.SpecialFileError) as e:
            showinfo(f"Error: {e}")
        except FileNotFoundError:
            showinfo(f"Error: Source or destination file not found.")
        except PermissionError:
            showinfo(f"Error: Permission denied to access files.")
        except OSError as e:
            showinfo(f"Error: {e}")
        except Exception as e:
            showinfo(f"An unexpected error occurred: {e}")

    def move_files(self, source_folder: str, destination_folder: str) -> None:
        files = os.listdir(source_folder)

        for file in files:
            source_file_path = os.path.join(source_folder, file)
            destination_file_path = os.path.join(destination_folder, file)
            shutil.move(source_file_path, destination_file_path)
            print(f"Moved: {source_file_path} to {destination_file_path}")


    def count_files_in_folder(self, folder_path: str) -> int:
        files = os.listdir(folder_path)
        num_files = len(files)
        return num_files

    def final_folder_to_manga_name_folder(self, folder_path: str, manga_name: str) -> None:
        end_folder_name = os.path.join(self.manga_name_folder , manga_name)
        os.rename(self.final_folder , end_folder_name)
        print(f"Renamed {self.final_folder } to {end_folder_name}")

        shutil.make_archive(end_folder_name, 'zip', root_dir=os.path.join(folder_path, self.manga_name), base_dir=manga_name)

        os.rename(f"{end_folder_name}.zip", f"{end_folder_name}.cbz")
        print(f"Renamed {end_folder_name}.zip to {end_folder_name}.cbz")
    
    def custom_cover(self, custom_cover_path: str, final_folder: str) -> None:
        destination_file = os.path.join(final_folder, os.path.basename(custom_cover_path))
        self.copy_file_from_one_destination_to_other_destination(custom_cover_path, destination_file)
    
    def remove_temp_workpath(self, workpath: str) -> None:
        shutil.rmtree(workpath)
        print(f"Deleted all files from {workpath}")

    def rename_cbz_to_zip(self, copy_cbz_files: str, processing_folder: str, final_folder: str) -> None:
        files = sorted(os.listdir(copy_cbz_files), key=self.natural_sort_key)
        for file in files:
            if file.endswith('.cbz'):
                old_file_path = os.path.join(copy_cbz_files, file)
                new_file_path = os.path.join(copy_cbz_files, file.replace('.cbz', '.zip'))
                
                os.rename(old_file_path, new_file_path)
                print(f"Renamed {old_file_path} to {new_file_path}")

                with zipfile.ZipFile(new_file_path, 'r') as zip_ref:
                    zip_ref.extractall(processing_folder)
                    print(f"Unzipped {new_file_path}")
                
                final_count = self.count_files_in_folder(final_folder)

                pages = sorted(os.listdir(processing_folder))
                addition_to_folder_name = final_count + 1

                for idx, page in enumerate(pages[:-1]):

                    new_page_name = f"{addition_to_folder_name + idx}.jpg"

                    old_page_path = os.path.join(processing_folder, page)
                    new_page_path = os.path.join(final_folder, new_page_name)
                    
                    os.rename(old_page_path, new_page_path)
                    print(f"Renamed {old_page_path} to {new_page_path}")

                self.move_files(processing_folder, final_folder)
                self.remove_temp_workpath(processing_folder)                 