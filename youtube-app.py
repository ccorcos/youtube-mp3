from Tkinter import *

import os
import re
import urllib
import glob
import eyed3

# links = """

# http://www.youtube.com/watch?v=hN5X4kGhAtU

# http://www.youtube.com/watch?v=mWRsgZuwf_8

# http://www.youtube.com/watch?v=ktvTqknDobU

# """

# links = re.sub(r',',' ',links)
# links = re.sub(r'\n',' ',links)
# links = re.sub(r' +',' ',links)
# links = links.lstrip().rstrip().split(' ')

# home = os.getenv("HOME")
# d = home+"/Downloads/"
# os.chdir(d)

# for link in links:

#     print "\nyoutube link: "+ link

#     f = urllib.urlopen("http://youtubeinmp3.com/fetch/?api=advanced&video=" + link)
#     r =  f.read()

#     r = re.sub(r'<.*?>','\n',r)
#     name = re.search(r'Title: (.*)\n',r).group(1).lstrip().rstrip()
#     artist = name.split('-')[0].lstrip().rstrip()
#     song = name.split('-')[1].lstrip().rstrip()

#     print "found:\n   artist: " +artist+"\n   song: "+song

#     l = re.search(r'Link: (.*)\n',r).group(1)

#     print "downloading song from link: \n" + l +"\n"

#     os.system('curl -o "'+name+'.mp3" "'+l+'"')

#     f = eyed3.load(glob.glob(name+".mp3")[0])
#     f.tag.artist = unicode(artist)
#     f.tag.title = unicode(song)
#     f.tag.save()


class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.text = Text(frame)
        self.text.pack()

        self.button = Button(frame, text="download", command=self.download)
        self.button.pack()

    def download(self):
        print "downloading"

root = Tk()

app = App(root)

root.mainloop()