from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

r=requests.get("https://www.iexindia.com/marketdata/market_snapshot.aspx")
data=r.text
soup=BeautifulSoup(data,'lxml')

i=-1
j=0
k=0

#Create 9 lists to store the eight parameters
date1=list();
time1 = list();
purchase_bid1 = list();
sell_bid1 = list();
MCV1 = list();
cleared_vol1 = list();
vol_loss1 = list();
FSV1 = list();
MCP1 = list();

table=soup.find_all('table')[25]

for row in soup.findAll('table')[25].findAll('tr'):
	i+=1
	if (i==0 | i==1 ):
		continue
	if 	(row.findAll('td')[3].string==None):
		continue
	if(i==2):
		time = row.findAll('td')[3].string
		purchase_bid = row.findAll('td')[4].string
		sell_bid = row.findAll('td')[5].string
		MCV = row.findAll('td')[6].string
		cleared_vol = row.findAll('td')[7].string
		vol_loss = row.findAll('td')[8].string
		FSV = row.findAll('td')[9].string
		MCP = row.findAll('td')[10].string
	elif (i%4==2):
		time = row.findAll('td')[2].string
		purchase_bid = row.findAll('td')[3].string
		sell_bid = row.findAll('td')[4].string
		MCV = row.findAll('td')[5].string
		cleared_vol = row.findAll('td')[6].string
		vol_loss = row.findAll('td')[7].string
		FSV = row.findAll('td')[8].string
		MCP = row.findAll('td')[9].string			
	else:
		time = row.findAll('td')[1].string
		purchase_bid = row.findAll('td')[2].string
		sell_bid = row.findAll('td')[3].string
		MCV = row.findAll('td')[4].string
		cleared_vol = row.findAll('td')[5].string
		vol_loss = row.findAll('td')[6].string
		FSV = row.findAll('td')[7].string
		MCP = row.findAll('td')[8].string
	time1.append(time)
	purchase_bid1.append(float(purchase_bid))
	sell_bid1.append(float(sell_bid))
	MCV1.append(float(MCV))
	cleared_vol1.append(float(cleared_vol))
	vol_loss1.append(float(cleared_vol))
	FSV1.append(float(FSV))
	MCP1.append(float(MCP)) 

now=datetime.datetime.now()
now_str=str(now)
date=now_str[0:10]

for i in range(0,95):
	if i==0:
		date1.append(date)
	date1.append(None)

#print(date1)	

raw_data={'date':date1,'time':time1,'purchase_bid':purchase_bid1,'sell_bid':sell_bid1,'MCV':MCV1,'cleared_vol':cleared_vol1,'vol_loss':vol_loss1,'FSV':FSV1,'MCP':MCP1}

raw_df=pd.DataFrame(raw_data, columns=['date','time','purchase_bid','sell_bid','MCV','cleared_vol','volume_loss','FSV','MCP'])

#print(raw_data)
#print(raw_df)
#raw_df.plot(x='purchase_bid',y='MCP').show()
#print(raw_df.plot(x='purchase_bid',y='MCP'))

#Store as an excel file with today's date.
#now=datetime.datetime.now()
#date=str(now)[0:10]
#raw_df.to_excel(date+".xlsx",sheet_name='Sheet1')

