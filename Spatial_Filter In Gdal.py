from osgeo import ogr
import os
shapefile = r"C:\Users\Dell\Desktop\Python\Python GDAL\Nepal Data\hermes_NPL_new_wgs\hermes_NPL_new_wgs"

driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(shapefile, 0)
layer = dataSource.GetLayer()

for feature in layer:
    print (feature.GetField("GaPa_NaPa"))
layer.ResetReading()