#Programmed by Alison Page 9/9/25

import geopandas as gpd #gpd is the convention used to shorten the phrase geopandas. 

FILE_PATH = r"C:\Programming\LocalGovernmentArea.shp" #Global Variable set for input file location. 
OUTPUT_FOLDER_PATH = r"C:\Programming\Output" #Global variable set for Output folderpath

#print(FILE_PATH) #print file path location


#print(gdf.columns) #this provides the details of the columns within the shape file. 

def transformFromWgs84ToMGA2020Z56(filePath, ESPG=4326): # Coordinate System is WGS 84
    

    if isinstance(filePath,str):
        print("Your filepath is formatted as a string!\n")
    else:
        raise ValueError ("Error - you need to enter the file path as a string\n")
    
    if isinstance(ESPG,int):
        print("Your Coordinate System code is an integer!\n") # not working
    else:
        raise ValueError ("Error - you need to enter the ESPG as an integer\n")
    

    try:
        gdf = gpd.read_file(filePath) #request to read the file
        print(gdf.crs) #print coordinate refernce system - current system is WGS84
        gdf = gdf.to_crs(epsg=ESPG) #default is set in the function - can be changed via dafault value to alter to a seperate coodrinate system when needed. 

    except Exception as e:
        print("**************************************ERROR***************************************************\n", e) # Error coded for printing out to the console in case there is an issue. 
    
    return gdf #returns geodataframe object. 

gdftransformed = transformFromWgs84ToMGA2020Z56(FILE_PATH,ESPG=7856) #creates a variable to transform the Coordinate system to MGA2020Z56


def exportGdfToGeoJson(gdf, OUTPUT_FOLDER_PATH): #geodataframe passed to the output file 

    fulloutputPathWithFileName = OUTPUT_FOLDER_PATH + "\\" + "output.GeoJson"   #using Driver GeoJson
    gdf.to_file(fulloutputPathWithFileName, driver="GeoJSON")

exportGdfToGeoJson(gdftransformed,OUTPUT_FOLDER_PATH)

