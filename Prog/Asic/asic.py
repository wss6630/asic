import requests
import json
from requests.auth import HTTPDigestAuth
#import bs4 as BS
from bs4 import BeautifulSoup
t = 0
r = requests.get('http://192.168.1.23/cgi-bin/minerStatus.cgi', auth=HTTPDigestAuth('root', 'root'))
soup = BeautifulSoup (r.text, 'lxml')
soup_2 = BeautifulSoup (r.text, 'html.parser')
list_tag = soup.find_all('td', class_='cbi-value-field')
print(r.text)
#r = requests.get('http://192.168.1.23')

#soup.find ('div', class_='cbi-value-field')

 # json = res.json()
#print(res.json())
#soup.find(text='ant_ghsav') 
#print(r.text)
#print(r.headers)
 
#print(r.status_code)
#print (r.text)
 
#for i in list_tag:
  #  print (i.text, t)
    


#print (list_tag)
    

#print(r.headers)
#print(soup)
#print('Time work  : ',soup.find ('div', class_='cbi-section-node').find_next('td', class_='cbi-value-field').text)
#print('Time work  : ',soup.find ('div', class_='cbi-section-node').find('div', id='cant_ghs5s'))
def info():
    r = requests.get('http://192.168.1.23/cgi-bin/minerStatus.cgi', auth=HTTPDigestAuth('root', 'root'))
    soup = BeautifulSoup (r.text, 'lxml')
    list_tag = soup.find_all('td', class_='cbi-value-field')
    
    r_config = requests.get('http://192.168.1.23/cgi-bin/minerConfiguration.cgi',auth=HTTPDigestAuth('root', 'root'))
    soup_config = BeautifulSoup (r.text, 'lxml')
    list_config = soup.find_all('td', class_='ant_low_vol')
        
    print('Response  ',r.status_code)
    print ('GH/S RT   '   , list_tag[1].text.strip())
    print ('Alive      ', list_tag[11].text.strip())
    print ('HW total  ', list_tag[77].text.strip())
    print ('chain  Temp    Chip num   Rt        HW')
    
    print ('',list_tag[93].text.strip(), '   ', list_tag[100].text.strip() , '       ' ,list_tag[94].text.strip(), '    ',list_tag[97].text.strip(),'  ',list_tag[98].text.strip() )
    print ('',list_tag[102].text.strip(), '   ', list_tag[109].text.strip() , '       ' ,list_tag[103].text.strip(), '    ',list_tag[106].text.strip(),'  ',list_tag[107].text.strip() )
    print ('',list_tag[111].text.strip(), '   ', list_tag[118].text.strip() , '       ' ,list_tag[112].text.strip(), '    ',list_tag[115].text.strip(),'  ',list_tag[116].text.strip() )
    print ('',list_tag[120].text.strip(), '   ', list_tag[127].text.strip() , '       ' ,list_tag[121].text.strip(), '    ',list_tag[124].text.strip(),'  ',list_tag[125].text.strip() )
    #print ('',list_tag[118].text.strip(), '   ', list_tag[111].text.strip() , '       ' ,list_tag[112].text.strip(), '    ',list_tag[115].text.strip(),'  ',list_tag[116].text.strip() )
    
    
    print ('Temp chip 4 ',list_tag[109].text.strip())

    print ('Temp chip4 {} HW {} ', list_tag[107].text.strip())

info()
    