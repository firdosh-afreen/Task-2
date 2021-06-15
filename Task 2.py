import request
import pandas as pd
from urllib.request import urlretrieve
from quarter import quaternally
quarter = quaternally()
quarter = quaternally()
api_Key = 'k50gwPRt2UfRDRIShbs0nmHpoa0vsNkv0yG53W45'
def fetchAPOD():
    
    URL_APOD = "https://api.nasa.gov/planetary/apod"
    date = '2021-06-14'
    params = {
      'api_key':api_Key,
      'date':date,
      'hd':'True'
       }
    response = request.get(URL_APOD,params=params).json()
    print(type(response))
    data = pd.DataFrame.from_dict(response,orient ='index')
    print(data)
    data.to_excel("output1.xlsx")


def fetchNeo():
    
    URL_NEO = "https://api.nasa.gov/neo/rest/v1/neo/browse/"
    date = '2021-06-15'
    params = {
      'api_key':api_Key,
      'date':date,
      'hd':'True'
       }
    response1 = request.get(URL_NEO,params=params).json()
    print(type(response1))
    print(response1)
    data = pd.DataFrame.from_dict(response1,orient ='index')
    print(data)
    data.to_excel("output2.xlsx")

fetchNeo()
fetchAPOD()
