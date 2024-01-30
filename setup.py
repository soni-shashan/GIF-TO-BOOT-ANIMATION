import os

current_path = os.getcwd()
command=f'pyinstaller --noconfirm --onefile --windowed --icon "{current_path}/loading.ico" --name "GIF TO BOOT ANIMATION" --add-data "{current_path}/create_boot_animation.py;." --add-data "{current_path}/gifextract.py;." --add-data "{current_path}/loading.ico;." --add-data "{current_path}/customtkinter;customtkinter/"  "{current_path}/boot_to_gif.py"'
os.system(command)