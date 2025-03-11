import shutil
import os

vscode_dir = '.vscode'

if os.path.exists(vscode_dir):
    shutil.rmtree(vscode_dir)
    print(f"Removed {vscode_dir} directory.")
else:
    print(f"{vscode_dir} directory does not exist.")
