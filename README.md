##__To clone a Git repository using the HTTPS URL , you can use the following git clone command__
###git clone https://github.com/soni-shashan/GIF-TO-BOOT-ANIMATION.git
##__To Install A Requirements Library , you can use the following pip install command__
###cd GIT-TO-BOOT-ANIMATION
###pip install -r requirements.txt
##__To Create Exe File,you can use Pyinstaller & the followinf pyinstaller command(Please replace according to your usage in Python 312)__
###pip install pyinstaller
###pyinstaller --noconfirm --onefile --windowed --icon "%cd%/loading.ico" --name "GIF TO BOOT ANIMATION" --add-data "%cd%/create_boot_animation.py;." --add-data "%cd%/gifextract.py;." --add-data "%cd%/loading.ico;." --add-data "C:/Users/shash/AppData/Roaming/Python/Python312/site-packages/customtkinter;customtkinter/"  "%cd%/boot_to_gif.py"
