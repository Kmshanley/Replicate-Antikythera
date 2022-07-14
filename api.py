import json
import requests

HorizonsID_Planets_dict = {
  "Mercury": "199",
  "Venus": "299",
  "year": "399",
  "Mars": "499",
  "Jupiter" : "599",
  "Saturn"  : "699",
  "Uranus"  : "799",
  "Neptune" : "899",
}

def gen_url(objid, start_time, stop_time, stepsize, center):
    '''Generates a url for accessing horizions for the specified parameters'''
    link = "https://ssd.jpl.nasa.gov/api/horizons.api"
    link += "?format=json"
    link += "&COMMAND='"+ str(objid) +"'"
    link += "&MAKE_EPHEM='YES'"
    link += "&EPHEM_TYPE=VECTORS"
    link += "&START_TIME='"+ start_time +"'"
    link += "&STOP_TIME='"+ stop_time +"'"
    link += "&STEP_SIZE='"+ stepsize + "'"
    link += "&OUT_UNITS='KM-S'"
    link += "&REF_PLANE='ECLIPTIC'"
    link += "&REF_SYSTEM='J2000'"
    link += "&VEC_LABELS='YES'"
    link += "&VEC_DELTA_T='NO'"
    link += "&OBJ_DATA='NO'"
    link += "&VEC_TABLE='1'"
    link += "&CSV_FORMAT='YES'"
    link += "&CENTER='"+ center + "'"
    return(link)

def query_horizons(objid, start_time, stop_time, stepsize='1d', center='@sun'):
    '''Queries the horizions database for the specified parameters, returns a dict with the following structure:
    
    ****************************************************
            JDTDB       :       TUPLE(  X,  Y,  Z)
    ****************************************************
            KEY         :             VALUES


    JDTDB = Julian Date relative to TDB
    TDB = Barycentric Dynamical Time
    '''
    response = requests.get(gen_url(objid, start_time, stop_time, stepsize, center))
    resultsReturn = dict()

    if (response.status_code == 200):
        try:
            data = json.loads(response.text)
        except ValueError:
            print("Unable to decode JSON results")
            return None
        
        res = data.get('result') #data string is under 'results' key
        #response json object also has 'signature' key, with api information
        header = res[0:res.index('$$SOE')] #extract header string
        rawData = res[res.index('$$SOE') + 5:res.index('$$EOE')] #extract data string between markers
        rawData = rawData.split(",") #turn into list of strings

        for i in range(0, len(rawData) - 1, 5):
            corrds = (float(rawData[i+2]), float(rawData[i+3]), float(rawData[i+4])) #create tuple corrds, convert scientific notation strings to python ints
            resultsReturn.update({float(rawData[i].strip("\n")):corrds}) #add to dict, key is time, value is tuple of corrds

        return resultsReturn

    else:
        print("Error querying Horizions; response code: {0}".format(response.status_code))
        return None


if __name__ == "__main__":
    print(query_horizons(HorizonsID_Planets_dict["Mars"], '2000-01-01', '2001-02-01')) #example query