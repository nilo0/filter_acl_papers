__version__ = '0.1.0'
import os


current_file_path = os.path.abspath(__file__)
current_dir_path = os.path.dirname(current_file_path)


ACL_PAPER_PATH = os.path.join(current_dir_path, "output", "acl_paper_data")
os.makedirs(ACL_PAPER_PATH, exist_ok=True)
