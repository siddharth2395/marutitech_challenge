import csv

#file name of input data
file='Python Problem - Sample Data.csv'
reader = csv.DictReader(open(file, 'rb'))

segment = [
	['1-250'],
	['251-500'],
	['501-1000'],
	['1001-1500'],
	['1501-2000'],
	['2001-3000'],
	['3001-4000'],
	['4001-5000'],
	['5001-100000']
]

def segmantations(row):
	if int(row['MarketPlaceValuation']) in range(251):
		segment[0].append(row)
	elif int(row['MarketPlaceValuation']) in range(501):
		segment[1].append(row)
	elif int(row['MarketPlaceValuation']) in range(1001):
		segment[2].append(row)
	elif int(row['MarketPlaceValuation']) in range(1501):
		segment[3].append(row)
	elif int(row['MarketPlaceValuation']) in range(2001):
		segment[4].append(row)
	elif int(row['MarketPlaceValuation']) in range(3001):
		segment[5].append(row)
	elif int(row['MarketPlaceValuation']) in range(4001):
		segment[6].append(row)
	elif int(row['MarketPlaceValuation']) in range(5001):
		segment[7].append(row)
	elif int(row['MarketPlaceValuation']) in range(100001):
		segment[8].append(row)
	else:
		print "error",row['MarketPlaceValuation']

for line in reader:
	segmantations(line)

c=0
write_data=[]

for i in segment:
	AvgMarketPlaceEGP=0
	AvgMarketPlaceGrossProfit=0
	AvgDirectEGP=0
	AvgDirectGrossProfit=0
	c_AvgMarketPlaceEGP=0
	c_AvgMarketPlaceGrossProfit=0
	c_AvgDirectEGP=0
	c_AvgDirectGrossProfit=0
	for k in range(1,len(i)):
		c_AvgMarketPlaceEGP+=float(i[k]['MarketPlaceEGP'])
		c_AvgMarketPlaceGrossProfit+=float(i[k]['GrossProfit'])
		c_AvgDirectEGP+=float(i[k]['DirectEGP'])
		c_AvgDirectGrossProfit+=float(i[k]['GrossProfit'])
	AvgMarketPlaceEGP=int(c_AvgMarketPlaceEGP/len(i))
	AvgMarketPlaceGrossProfit=int(c_AvgMarketPlaceGrossProfit/len(i))
	AvgDirectEGP=int(c_AvgDirectEGP/len(i))
	AvgDirectGrossProfit=int(c_AvgDirectGrossProfit/len(i))
	write_data.append(
	{
		"Valuation Segment":i[0],
		"AvgMarketPlaceEGP":AvgMarketPlaceEGP,
		"AvgMarketPlaceGrossProfit":AvgMarketPlaceGrossProfit,
		"AvgDirectEGP":AvgDirectEGP,
		"AvgDirectGrossProfit":AvgDirectGrossProfit
	})

with open('out.csv', 'w') as csvfile:
	fieldnames = ['Valuation Segment', 'AvgMarketPlaceEGP','AvgMarketPlaceGrossProfit','AvgDirectEGP','AvgDirectGrossProfit']
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	for d in write_data:
		writer.writerow(d)
