import numpy as np 
import pylab
import mahotas as mh 

dna = mh.imread('images/dna.jpeg')
pen = mh.imread('images/Penguins.jpg')

#pylab.imshow(pen)
#pylab.show()


# dnaf = mh.gaussian_filter(dna, 8)
#change type to int for otsu to work
# dnaf = dnaf.astype('uint8')
# T = mh.thresholding.otsu(dnaf)
# pylab.imshow(dnaf > T)
# pylab.show()

dnaf = mh.gaussian_filter(dna, 8)
rmax = mh.regmax(dnaf)

pylab.imshow(mh.overlay(dna, rmax))
pylab.show()

pylab.imshow(dnaf)
pylab.show()
# labeled, nr_objects = mh.label(dnaf > T)
# print "nr_objects: {}".format(nr_objects) 
# pylab.imshow(labeled)
# pylab.jet()
# pylab.show()

# pylab.imshow(dna)
# pylab.show()



print dna.shape
print dna.dtype
print dna.max()
print dna.min()