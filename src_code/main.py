""" Programmed by Alison Page  September 2025 for tafe Unit ICTPRG440 - Assessment 2"""
import geopandas as gpd

FILE_PATH = r"C:\Programming\CorrectionalFacility\Correctional Facility.shp" #Global Variable set for input file location. code r refers to a raw string
OUTPUT_FOLDER_PATH = r"C:\Programming\GitHub\ICTPRG440\src_code\Output" #Global variable set for Output folderpath

#print(FILE_PATH) #prints file path location
#print(OUTPUT_FOLDER_PATH) #prints file path location

# read the file


def transformFromWgs84ToMGA2020Z56(FilePath, EPSG=4326): 
    """This function transforms the coordinators from WGS84 to another coordinate system currently set to WGS84"""

    if isinstance(FilePath,str): # check to ensure the file path is formatted as a string
            print("FILEPATH TYPE: Your filepath if formatted as a string")
    else:
        raise ValueError("You need to enter the file path as a string")
    
    if isinstance(EPSG,int): # check to ensure the coordinate system code is entered as an iteger
            print("EPSG: Your coordinate system is entered as an integer")
    else:
        raise ValueError("You need to enter an integer")

    try:
        gdf = gpd.read_file(FilePath) #function will return a geodataframe type that helps deal with geospatial data. 
        gdf = gdf.to_crs(epsg=EPSG)#redefining the Coordinate reference system to Projected Coordinate System GDA 2020 MGA 56
        
        #print (type(gdf))
        #print(gdf.crs) #checking the coordinate system that the data is created in

        #print(gdf.head()) #prints first 5 rows ofthe geodataframe - similar to the attribute table in Arc. 
        #print(gdf.columns) # prints the column header descriptors of the shape file. 
    except Exception as e:
        print("Error......................................................................\n", e)
    
    return gdf #returns the geodataframe object

transformGdf = transformFromWgs84ToMGA2020Z56(FILE_PATH, EPSG=7856)
"""Enter the cordinate system that you need the results returned as in this section"""

print(transformGdf.head()) # prints first 5 rows of the geodataframe


