## Polygonize a Raster band

from osgeo import gdal, ogr
import sys

##gdal.UseExceptions()

src_ds = gdal.Open("open.tif")
if src_ds is None:
    print 'Unable to open open.tif'
    sys.exit(1)

try:
    srcband = src_ds.GetRasterBand(3)
    
except RuntimeError, e:
    print 'Band (3) not found'
    print e
    sys.exit(1)

dst_layername = "POLYGONIZED_STUFF"
drv = ogr.GetDriverByName("ESRI Shapefile")
dst_ds = drv.CreateDataSource(dst_layername + ".shp")
dst_layer = dst_ds.CreateLayer(dst_layername, srs = None)

gdal.Polygonize(srcband, None, dst_layer, -1, [], callback=None)
