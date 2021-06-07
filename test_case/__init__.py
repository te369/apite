import sys
from pathlib import Path
current_folder = Path(__file__).absolute().parent

sys.path.append(str(current_folder.parent))
# print("---------->",current_folder.parent)
# os.chdir(str(current_folder)) # 切工作区
# print(current_folder)
