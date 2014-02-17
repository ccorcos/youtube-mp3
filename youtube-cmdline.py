import os
import re
import urllib
import glob
import eyed3


home = os.getenv("HOME")
d = home+"/Downloads/"
os.chdir(d)

print "Download MP#'s from YouTube."
print "Press control-c to quit."
while True:
	link = raw_input('\nEnter a YouTube link: ')
	link = link.lstrip().rstrip()

	f = urllib.urlopen("http://youtubeinmp3.com/fetch/?api=advanced&video=" + link)
	r =  f.read()

	r = re.sub(r'<.*?>','\n',r)
	name = re.search(r'Title: (.*)\n',r).group(1).lstrip().rstrip()
	artist = name.split('-')[0].lstrip().rstrip()
	song = name.split('-')[1].lstrip().rstrip()

	print "\nartist: " +artist+"\nsong: "+song

	l = re.search(r'Link: (.*)\n',r).group(1)

	print "\ndownloading song from link: \n" + l +"\n"

	os.system('curl -o "'+name+'.mp3" "'+l+'"')

	f = eyed3.load(glob.glob(name+".mp3")[0])
	f.tag.artist = unicode(artist)
	f.tag.title = unicode(song)
	f.tag.save()