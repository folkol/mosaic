import fnmatch
import os
from PIL import Image
import sys
import itertools
from numpy import mean
from numpy import var


FRAGMENT_SIZE=25

def cartesian(dim):
    w, h = dim
    return itertools.product(range(w), range(h))

def prune_images(cutoff):
    for root, dirnames, filenames in os.walk('img'):
        for filename in fnmatch.filter(filenames, '*.jpg'):
            path = os.path.join(root, filename)
            size = (FRAGMENT_SIZE, FRAGMENT_SIZE)
            im = Image.open(path).resize(size, Image.ANTIALIAS)
            pix = im.load()
            samples=[]
            for x, y in cartesian(im.size):
                samples.append(pix[x, y])
            mean_color = tuple(map(mean, zip(*samples)))
            if var(samples) > cutoff:
                print 'pruning', filename
                os.remove(path)


if len(sys.argv) < 2:
    print 'usage: python prune.py 1337'
    print ''
    print '    This will remove all images under ./img/ with a RBG variance of above [1337].'
    sys.exit(1)

prune_images(int(sys.argv[1]))
