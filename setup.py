import os
import shutil

icon='loading.ico'
name='GIF TO BOOT ANIMATION'

current_path = os.getcwd()
command=f'pyinstaller --noconfirm --onefile --windowed --icon "{current_path}/{icon}" --name "{name}" --add-data "{current_path}/create_boot_animation.py;." --add-data "{current_path}/gifextract.py;." --add-data "{current_path}/{icon};." --add-data "{current_path}/customtkinter;customtkinter/"  "{current_path}/boot_to_gif.py"'
os.system(command)
copy_path=f'{current_path}/dist/{name}.exe'
dest_path=f'{current_path}/{name}.exe'
shutil.copy(copy_path,dest_path)
os.remove(f'{name}.spec')
shutil.rmtree(current_path+'/dist')
shutil.rmtree(current_path+'/build')
