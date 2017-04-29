

from PIL import Image

from os import listdir
from os.path import isfile, join

from skimage import color
from skimage import io


##target_dir = './annotations/validation'
target_dir = './annotations/training'

imagesfiles = [f for f in listdir(target_dir ) if isfile(join(target_dir, f))]

print imagesfiles

for image in imagesfiles:

	img = color.rgb2gray(io.imread(join(target_dir, image)))
	##img = Image.open(join(target_dir, image)).convert('L', (0.2125,  0.7154, 0.0721, 0))
	filename = image.split(".")[0]
	io.imsave(join(target_dir, image), img)		
