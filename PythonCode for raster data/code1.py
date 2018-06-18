## Get Raster MetaData

from osgeo import gdal
gtif = gdal.Open("open.tif")
print gtif.GetMetadata('Area')
