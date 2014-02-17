This script uses a 3rd party api to download mp3's from youtube

To compile into a commandline tool

pip install pyinstaller
pyi-makespec --onefile youtube-cmdline.py 
pyi-build youtube-cmdline.spec 
