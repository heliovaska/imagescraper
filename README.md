# imagescraper
Python script for fetching images from webpage

This program is run from command line
- Webpage url is given as command line attribute
- Image urls are searched from inside img -tags from src -attributes
- Only complete image urls are handled
	- Relative image paths are ignored
- Only images, which are loaded, when webpage is opened, are noticed
	- Webpage scrolling to trigger dynamic image loading is not implemented
- Images are saved to same folder, where script is executed
	- Image name consists of "image_" and 4-digit running number
	- Filename extension is read from image url
- Image urls are stored into "imageURLs.txt" -text file
	- If webpage doesn't include any images, only empty text file is created
- Error handling for nonexistent webpage urls or incompatible image filenames are not implemented.
