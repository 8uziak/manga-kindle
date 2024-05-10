## 1. Install Python

Before using Manga Kindle, you'll need to install Python.  
- [Here is a link to the Python downloads page.](https://www.python.org/downloads)  
- [Here is a helpful guide to installing Python on various operating systems.](https://wiki.python.org/moin/BeginnersGuide/Download)

*Later in this guide, you will use the Package Installer for Python (pip), which may require you to add Python to your system PATH.*

## 2. Install Manga-Kindle

*Two options:*

1. Install Manga Kindle from PyPI.

    ``` 
    pip install -i https://test.pypi.org/simple/ manga-kindle==0.0.2
    ```

2. To run Manga-Kindle from the source code, follow the instructions below.

   1. Download the source files for Manga-Kindle by downloading it manually or using GIT.

        ```
        git clone https://github.com/8uziak/manga-kindle.git
        ```

   2. Change your working directory to Manga-Kindle.

        ```
        cd manga-kindle
        ```

   3. Install the necessary dependencies by running

        ```
        pip install -r requirements.txt
        ```
        ```
        pip install -e .
        ```

        If *pip install* doesn't work try replacing it with one of these
        - `pip3 install`
        - `python -m pip install`
        - `python3 -m pip install`

   This will install all requirements and Manga-Kindle.

## 3. How to make it works

1. If you installed Manga-Kindle using PIP
    
    1. Create main.py file and copy paste code below to main.py
        
        ```python   
        from manga_kindle.main import main 
                                              
        if __name__ == '__main__':        
            main()                        
        ```

    2. Copy paste code below to CMD

        ```
        python main.py
        ```
        
        or 

        ```
        python3 main.py
        ```

2.  If you installed Manga-Kindle using git clone

    1. Copy paste code below to CMD

        ```
        python src/manga-kindle/main.py
        ```
        
        or 

        ```
        python3 src/manga-kindle/main.py
        ```

## 4. GUI (How does it work)

1. **[Not Required]** Add custom cover lets you add your cover of choice. It means it cant be whatever image (jpg/png) you want! 

2. **[Required]** Add directory: you can click a 'Add directory' button or write it yourself below the button. It's going to be a directory from which the program will take all your CBZ files and turn it to a one CBZ file. 
NOTE: all input CBZ files need to be sortable, because an app sorts every file in directory and then it renames files inside these CBZ files one by one. I
It means there should be naming pattern (name + number) e.g:
- attack_on_titan_chapter_1, attack_on_titan_chapter_2, attack_on_titan_chapter_3
- attack_on_titan_1, attack_on_titan_2, attack_on_titan_3
- 1_attack_on_titan, 2_attack_on_titan, 3_attack_on_titan
- etc.

3. **[Required]** Add file: you can click a 'Add file' button or write it yourself below the button. It's going to be a name of a folder with final CBZ file.

4. Click Convert button to convert many to one CBZ file.


### Egzample workpath before
```
.
└── manga_folder/
    ├── attack_on_manga chapter 1.cbz
    ├── attack_on_manga chapter 2.cbz
    ├── attack_on_manga chapter 3.cbz
    ├── attack_on_manga chapter 4.cbz
    ├── attack_on_manga chapter 5.cbz
    └── ... etc.cbz
```
### Egzample workpath after (assuming you put 'attack_on_manga' in Add folder textbox)
```
.
└── manga_folder/
    ├── attack_on_manga chapter 1.cbz
    ├── attack_on_manga chapter 2.cbz
    ├── attack_on_manga chapter 3.cbz
    ├── attack_on_manga chapter 4.cbz
    ├── attack_on_manga chapter 5.cbz
    ├── ... etc.cbz
    └── attack_on_manga/
        ├── attack_on_manga/
        │   ├── 0.jpg # <- if you added your custom manga cover (using Add custom cover)
        │   ├── 1.jpg
        │   ├── 2.jpg
        │   ├── 3.jpg
        │   └── ... etc.jpg
        └── attack_on_manga.cbz # <- with all jpg files which you can see in attack_on_manga folder
```