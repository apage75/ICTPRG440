#Programmed by Alison Page 9/9/25
 
import geopandas as gpd #gpd is the convention used to shorten the phrase geopandas.
 
FILE_PATH = r"C:\Programming\CorrectionalFacility\Correctional Facility.shp" #Global Variable set for input file location.
OUTPUT_FOLDER_PATH = r"C:\Programming\Output" #Global variable set for Output folderpath
print(FILE_PATH) #print file path location
 
 
def transformFromWgs84ToMGA2020Z56(filePath, EPSG=4283): # Coordinate System is GDA 94
 
    if isinstance(filePath,str):
        print("Your filepath is formatted as a string!\n")
    else:
        raise ValueError ("Error - you need to enter the file path as a string\n")
   
    if isinstance(EPSG,int):
        print("Your Coordinate System code is an integer!\n") # not working
    else:
        raise ValueError ("Error - you need to enter the ESPG as an integer\n")
   
    try:
        gdf = gpd.read_file(filePath) #request to read the file
        print(gdf.crs) #print coordinate reference system - current system is GDA 94
        gdf = gdf.to_crs(epsg=EPSG) #default is set in the function - can be changed via dafault value to alter to a seperate coodrinate system when needed.
        #print(gdf.head)
     
    except Exception as e:
        print("**************************************ERROR***************************************************\n", e) # Error coded for printing out to the console in case there is an issue.
   
    return gdf #returns geodataframe object.
   
    print(type, gdf)
 
def exportGdfToGeoJson(gdf,OUTPUT_FOLDER_PATH): #geodataframe passed to the output file
   
        """This function is creating an output file as a string the file name created is output.GeoJson.
        Nothing else is returned
       
        """
       
        isGdf = isinstance(gdf,gpd.geodataframe)
        print(f"You have entered a Geodataframe")
        isGdf != isinstance(gdf,gpd.geodataframe)
        print(f"You have not entered a Geodataframe")
 
        fulloutputPathWithFileName = OUTPUT_FOLDER_PATH + "\\" + "output.GeoJson"   #using Driver GeoJson
        gdf.to_file(fulloutputPathWithFileName, driver="GeoJSON")
   
        return None
 
gdftransformed = transformFromWgs84ToMGA2020Z56(FILE_PATH,EPSG=7856) #creates a variable to transform the Coordinate system to MGA2020Z56
 
exportGdfToGeoJson(gdftransformed,OUTPUT_FOLDER_PATH)
 
# Now we need a loop to show the spatial data, attribute table, row by row in the console. using a python looping method.
 
 