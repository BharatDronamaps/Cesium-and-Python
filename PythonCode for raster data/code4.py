## Get Raster Band Information

from osgeo import gdal
import sys
gdal.UseExceptions()

def Usage():
    print("""
    $ getrasterband.py [band number] input-raster
    """)
    sys.exit(1)

band_num = 1;
input_file="open.tif"
src_ds = gdal.Open(input_file)
if src_ds is None:
    print 'Unable to open %s' % input_file
    sys.exit(1)

try:
    srcband = src_ds.GetRasterBand(band_num)
    except RuntimeError, e:
        print 'No band %i found' % band_num
        print e
        sys.exit(1)

    print "[No data value]= ", srcband.GetNoDataValue()
    print "[Min]= ", srcband.GetMinimum()
    print "[Max]= ", srcband.GetMaximum()
    print "[Scale]= ", srcband.GetScale()
    print "[Unit type]= ", srcband.GetUnitType()
    ctable = srcband.GetColorTable()

    if ctable is None:
        print 'No colorTable found'
        sys.exit(1)

    print "[Color Table Count]= ", ctable.GetCount()

    for i in range(0, ctable.GetCount() ):
        entry = ctable.GetColorEntry(i)
        if not entry:
            continue
        print "[Color Entry RGB]= ", ctable.GetColorEntryAsRGB(i, entry)

