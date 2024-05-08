## 1. Install Python

Before using Tkinter Designer, you'll need to install Python.  
- [Here is a link to the Python downloads page.](https://www.python.org/downloads)  
- [Here is a helpful guide to installing Python on various operating systems.](https://wiki.python.org/moin/BeginnersGuide/Download)

*Later in this guide, you will use the Package Installer for Python (pip), which may require you to add Python to your system PATH.*

## 2. Install Manga-Kindle

*Two options:*

1. Install Manga Kindle from PyPI.

    ``` 
    pip install -i https://test.pypi.org/simple/ manga-kindle==0.0.1
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

        If *pip* install doesn't work try replacing it with one of these
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
