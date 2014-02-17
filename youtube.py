import os
import re
import urllib
import glob
import eyed3

links = """

http://www.youtube.com/watch?v=hN5X4kGhAtU

http://www.youtube.com/watch?v=mWRsgZuwf_8

http://www.youtube.com/watch?v=ktvTqknDobU

"""

links = re.sub(r',',' ',links)
links = re.sub(r'\n',' ',links)
links = re.sub(r' +',' ',links)
links = links.lstrip().rstrip().split(' ')

home = os.getenv("HOME")
d = home+"/Downloads/"
os.chdir(d)

for link in links:

	print "\nyoutube link: "+ link

	f = urllib.urlopen("http://youtubeinmp3.com/fetch/?api=advanced&video=" + link)
	r =  f.read()

	r = re.sub(r'<.*?>','\n',r)
	name = re.search(r'Title: (.*)\n',r).group(1).lstrip().rstrip()
	artist = name.split('-')[0].lstrip().rstrip()
	song = name.split('-')[1].lstrip().rstrip()

	print "found:\n   artist: " +artist+"\n   song: "+song

	l = re.search(r'Link: (.*)\n',r).group(1)

	print "downloading song from link: \n" + l +"\n"

	os.system('curl -o "'+name+'.mp3" "'+l+'"')

	f = eyed3.load(glob.glob(name+".mp3")[0])
	f.tag.artist = unicode(artist)
	f.tag.title = unicode(song)
	f.tag.save()




# curl -o "song.mp3" "http://youtubeinmp3.com/download/grabber/?mp3=Imagine_Dragons_-_Demons_Official_Music_Video.mp3&i=mWRsgZuwf_8&t=Imagine+Dragons+-+Demons+%28Official+Music+Video%29&s=2"

# [os.system('open http://youtubeinmp3.com/fetch/?video='+ l) for l in links]

#open http://youtubeinmp3.com/fetch/?video=http://www.youtube.com/watch?v=KVYup3Qwh8Q


#  http://youtubeinmp3.com/fetch/?api=advanced&video=http://www.youtube.com/watch?v=i62Zjga8JOM

# url="http://youtubeinmp3.com/download/grabber/?mp3=Cage_The_Elephant_-_Come_A_Little_Closer_Official_Video.mp3&i=KVYup3Qwh8Q&t=Cage+The+Elephant+-+Come+A+Little+Closer+%28Official+Video%29&s=4"
# filename=$(curl -sI  $url | grep -o -E 'filename=.*$' | sed -e 's/filename=//')
# curl -o $filename -L $url