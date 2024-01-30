import os
import shutil
import site
import sys

icon='loading.ico'
name='GIF TO BOOT ANIMATION'
python_version = f"{sys.version_info.major}{sys.version_info.minor}"
current_path = os.getcwd()
user_site_packages = site.getuserbase()
python_path = os.path.join(user_site_packages, f"Python{python_version}")
command=f'pyinstaller --noconfirm --onefile --windowed --icon "{current_path}/{icon}" --name "{name}" --add-data "{current_path}/create_boot_animation.py;." --add-data "{current_path}/gifextract.py;." --add-data "{current_path}/{icon};." --add-data "{python_path}/site-packages/customtkinter;customtkinter/"  "{current_path}/boot_to_gif.py"'
os.system(command)
copy_path=f'{current_path}/dist/{name}.exe'
dest_path=f'{current_path}/{name}.exe'
shutil.copy(copy_path,dest_path)
os.remove(f'{name}.spec')
shutil.rmtree(current_path+'/dist')
shutil.rmtree(current_path+'/build')
os.system('cls')
print(f"EXE FILE: {name}.exe")
