Mosaic generator
----------------

This program will build up a palette from the jpg images found under
the img folder, and construct a mosaic of the image passed as
parameter.


Install and run:

 > pip install Pillow
 > time PYTHONPATH=/usr/local/lib/python2.7/site-packages python mosaic.py img/gallery/image-666.jpg 200 150
 > open example.jpg


Prune gallery (Remove images with higher variance than 100):

 > python prune.py


Notes:

*) I had to use 'PYTHONPATH=/usr/local/lib/python2.7/site-packages'

*) The mosaic generation is incredibly slow for larger tempate images
   because of the scan for closest match, calculate a Voronoi diagram
   beforehand and use that for sampling instead of a search.

*) Persist the Voronoi diagram in between executions?

*) Code needs cleaning up, but it was too fun to play with the
   generation, I will do that some other time :P
