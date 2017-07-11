from PIL import Image
import os 
import numpy as np

#Parse images
img_dir = "njtransit/"
data = []
for filename in os.listdir(img_dir):
	day = int(filename[19:21])

	im = Image.open(os.getcwd() +"/"+ img_dir+filename)
	pix = im.load()

	pos = [[79,207],[185,1513],[551,1513],[873,1513]]
	data.append([day,[pix[x[0],x[1]] for x in pos]])

#Engineer some features
def get_averages(values):
	add = []
	for x in range(1,len(values),3):
		avg = 0
		for num in range(x,x+3):
			avg += values[num]
		avg = avg/3
		add.append(avg)
	add.append(np.average(add[1:]))
	return add

avg_titles = ','+','.join(['r'+str(x)+'_avg' for x in range(1,6)])

#Write data out in .csv
with open("color_data.csv",'w') as out:
	out.write('Day,r11,r12,r13,r21,r22,r23,r31,r32,r33,r41,r42,r43'+avg_titles)
	for row in data:
		values = []
		values.append(row[0])
		for x in row[1]:
			for y in x:
				values.append(y)
		avgs = get_averages(values)
		values = ','.join(str(e) for e in values)
		print(values)
		out.write('\n'+values+','+','.join(str(round(e,2)) for e in avgs))
out.close()
