from osgeo import ogr
location = r"C:\Users\Dell\Desktop\Python\Python GDAL\New ShapeFile\local_unit\Local Unit"

driver = ogr. GetDriverByName('ESRI shapefile')
data_source = driver.Open(location, 0)

layer= data_source.GetLayer()

nagarpalika = []
GaunPalika = []
UpaMahanagarpalika = []
Mahanagarpalika = []
Wildlife_reserve = []
water_shed = []
National_Park =  []
hunting = []
development = []
Wildlife_reserve = []

for feature in layer:
    #print(feature.GetField('Type_GN'))
    if feature.GetField('Type_GN')=='Nagarpalika':
        nagarpalika.append(feature.GetField('Type_Gn'))
    elif feature.GetField('Type_GN')=='Gaunpalika':
        GaunPalika.append(feature.GetField('Type_Gn'))
    elif feature.GetField('Type_GN')=='Upamahanagarpalika':
        UpaMahanagarpalika.append(feature.GetField('Type_Gn'))
    elif feature.GetField('Type_GN')=='Mahanagarpalika':
        Mahanagarpalika.append(feature.GetField('Type_Gn'))
    elif feature.GetField('Type_GN')=='Wildlife Reserve':
        Wildlife_reserve.append(feature.GetField('Type_Gn'))
    elif feature.GetField('Type_GN')=='Watershed and Wildlife Reserve':
        water_shed.append(feature.GetField('Type_Gn'))    
    elif feature.GetField('Type_GN')=='National Park':
        National_Park.append(feature.GetField('Type_Gn'))    
    elif feature.GetField('Type_GN')=='Hunting Reserve':
        hunting.append(feature.GetField('Type_Gn'))    
    elif feature.GetField('Type_GN')=='Development Area':
        development.append(feature.GetField('Type_Gn'))

print("Total GaunPalika: ", len(GaunPalika))
print('Total Nagarpalika: ', len(nagarpalika))
print("Total Upamahanagarpalika: ", len(UpaMahanagarpalika))
print("Total Mahanagarpalika: ", len(Mahanagarpalika))
print("Total Wildlife Reserve", len(Wildlife_reserve))
print("Total Watershed and Wildlife Reserve", len(water_shed))
print("Total National Park", len(National_Park))
print("Total Hunting Reserve: ", len(hunting))
print("Total Development Area", len(development))

        
