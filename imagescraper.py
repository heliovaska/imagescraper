import urllib.request
import re
import sys

def fetchHTML(url):
	urlOpened = urllib.request.urlopen(url)
	htmlBytes = urlOpened.read()
	htmlString = htmlBytes.decode("utf8")
	urlOpened.close()
	return htmlString

def writeLineToFile(text, filename):
	file = open(filename,"a")
	file.write(text)
	file.write("\n")
	file.close()

def downloadPicture(url, pictureName):
	urllib.request.urlretrieve(url, pictureName)

filename = "imageURLs.txt"
file = open(filename,"w")
file.close()
htmlString = fetchHTML(sys.argv[1])
imgList = re.findall('<img.+?>', htmlString)
i = 0
for img in imgList:
	if re.search('src="', img):
		srcTemp = re.split('src="', img)
		src = re.split('"', srcTemp[1])[0]
		if src[0:4] == "http":
			writeLineToFile(src, filename)
			revSrc = src[::-1]
			pictureType = re.split('\.', revSrc)[0][::-1]
			pictureName = "image_%04d." % i + pictureType
			downloadPicture(src, pictureName)
			i += 1

