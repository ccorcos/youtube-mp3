import os
import re

links = """

http://www.youtube.com/watch?v=eac-hElBkFA

http://www.youtube.com/watch?v=mWRsgZuwf_8

http://www.youtube.com/watch?v=ktvTqknDobU

"""

links = re.sub(r',',' ',links)
links = re.sub(r'\n',' ',links)
links = re.sub(r' +',' ',links)

links = links.lstrip().rstrip().split(' ')

[os.system('open http://youtubeinmp3.com/fetch/?video='+ l) for l in links]

open http://youtubeinmp3.com/fetch/?video=http://www.youtube.com/watch?v=KVYup3Qwh8Q
