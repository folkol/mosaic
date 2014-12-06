import fnmatch
import os
from PIL import Image
import sys
import itertools
from numpy import multiply as mul
from numpy import mean
from numpy import linalg
from numpy import array
from numpy import var


FRAGMENT_SIZE = 40;

def closest_color(c, list):
    return min(list, key = lambda (x, _): linalg.norm(array(c) - array(x)))

def cartesian(dim):
    w, h = dim
    return itertools.product(range(w), range(h))

def generate_palette():
    colors = []
    for root, dirnames, filenames in os.walk('img'):
        for filename in fnmatch.filter(filenames, '*.jpg'):
            print 'Parsing ', filename, 
            path = os.path.join(root, filename)
            size = (FRAGMENT_SIZE, FRAGMENT_SIZE)
            im = Image.open(path).resize(size, Image.ANTIALIAS)
            pix = im.load()
            tuples=[]
            for x, y in cartesian(im.size):
                tuples.append(pix[x, y])
            mean_color = tuple(map(mean, zip(*tuples)))
            print var(tuples)
            if var(tuples) < 500:
                colors.append((mean_color, im))
    print 'Number of colors: ', len(colors)
    return colors

def generate_mosaic(path, w, h):
    im = Image.open(path)
    im.thumbnail((w, h), Image.ANTIALIAS)
    pixel_data = im.load()
    mosaic = Image.new("RGB", tuple(mul(FRAGMENT_SIZE, (w, h))))
    for x, y in cartesian(im.size):
        sys.stdout.write('.')
        sys.stdout.flush()
        color = pixel_data[x, y]
        _, image = closest_color(color, colors)
        mosaic.paste(image, tuple(mul(FRAGMENT_SIZE, (x, y))))
    return mosaic


print 'Loading database'
print 'Generating palette'
colors = generate_palette()

im = sys.argv[1]
w = int(sys.argv[2])
h = int(sys.argv[3])

print 'Generating mosaic'
mosaic = generate_mosaic(im, w, h)

mosaic.save('example.jpg')
