import requests,datetime
from bs4 import BeautifulSoup

URL = "https://enterprise.gov.ie/en/What-We-Do/Workplace-and-Skills/Employment-Permits/Current-Application-Processing-Dates/"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib') #should be in try catch block , if url is down etc (above snippet)

# print(soup.prettify())

def checkUpdateStatus():
    todayDate = datetime.datetime.now()
    print('CurrentDateTime')
    print(todayDate,"\n")

   
for para in soup.find_all("p"):
    
   
    strPara = para.get_text()
    
    strIndex = strPara.find('As of')

    # print(strPara)
    
    if (strIndex != -1):
        strCommaIndex = strPara.find(',') # start index is AS OF and end index is upto comma
        print('Last Updated ') # As Of is ending at index 6
        print(strPara[6:strCommaIndex],"\n")
        checkUpdateStatus()

for para in soup.find_all("tbody"):
   
    strPara = para.get_text()
    
    strIndex = strPara.find('Trusted')
    if (strIndex != -1):
        print ('Yes found Trsuted')
        strStandardIndex = strPara.find('Standard') # end index just before Standard
        print(strPara[15:strStandardIndex],"\n")

    
    strIndex = strPara.find('Standard')
    if (strIndex != -1):
        print ('Yes found Standard')
        
        print(strPara[strIndex+8:],"\n")  # standard is of 8 letters

    strIndex = strPara.find('Review')
    if (strIndex != -1):
        print ('Yes found Review')
        
        print(strPara[strIndex+16:],"\n")    # Reviews received is of 16 letters
    
    strIndex = strPara.find('Requests received')
    if (strIndex != -1):
        print ('Yes found Stamp 4')
        strSpaceNBIndex = strPara.find('NB') # end index just before spaceNB
        print(strPara[strIndex+17:strSpaceNBIndex])  # Request Received is of 17 letters



