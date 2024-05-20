import sys
if sys.version_info[0] < 3:
    raise ImportError("This package requires Python 3 or later")


__version__ = '0.0.3'
__license__ = 'BSD 3-Clause License'
__copyright__ = '2024, Mateusz Buziak <matbuziak@gmail.com>'
__docformat__ = 'restructuredtext en'
__all__ = ['cbz_files_to_one_cbz', 'gui_functionality','gui','main']