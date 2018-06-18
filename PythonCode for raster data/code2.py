## Get Raster Band

from osgeo import gdal
import sys
# this allow GDAL to throw Python Exceptions
gdal.UseExceptions()

try:
    src_ds = gdal.Open("open.tif")
except RuntimeError, e:
    print 'Unable to open open.tif'
    print e
    sys.exit(1)

try:
    srcband = src_ds.GetRasterBand(10)
except RuntimeError, e:
    print 'Band (%i) not found'
    print e
    sys.exit(1)
