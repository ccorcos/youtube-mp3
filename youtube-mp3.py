import os
import re
import urllib
import glob
import eyed3


home = os.getenv("HOME")
d = home+"/Downloads/"
os.chdir(d)

print "\nDownload MP3's from YouTube."
print "Press control-c to quit."
while True:
	link = raw_input('\nEnter a YouTube link: ')
	link = link.lstrip().rstrip()

	print "http://youtubeinmp3.com/fetch/?api=advanced&video=" + link

	# else find t<a style="width:150px;height:30px;font-size:12px;" class="download" href="http://youtubeinmp3.com/download/?n=1&amp;video=http://www.youtube.com/watch?v=1GRDm5KUBRI">Convert And<br> Download MP3</a>

	# and find this <a style="width:150px;height:30px;font-size:16px;margin-top:-8px;" class="download" href="grabber/?id=1GRDm5KUBRI&amp;n=0&amp;t=There%27s+only+me+%5Binstrumental%5D&amp;mp3=Theres_only_me_instrumental.mp3&amp;s=4"><div style="padding-top:5px;">Download MP3</div></a>

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
