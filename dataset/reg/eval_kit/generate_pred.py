# output format:
# inst#		actual	predicted	error(pred - actual)	ID				Tweet	Affect_Dimension: valence
# 1			0.141	0.309		0.168					2018-En-02354	'So @Ryanair site crashes everytime I try to book - how do they help? Tell me there\"s nothing wrong &amp; hang up #furious #helpless @SimonCalder'	
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import codecs
import time

# open prediction file
file_path 	= sys.argv[1]
fp 			= codecs.open(file_path, 'rb', encoding = "utf-8", errors = "ignore")
reader 		= csv.reader(fp)

# writing results into prediction plaintext
write_fp = "Predict-2018-Valence-reg-En-dev-" + str(int(time.time())) + ".csv"
ofile  = open(write_fp, "wb")
writer = csv.writer(ofile, delimiter='\t')

writer.writerow(["inst#", "actual", "predicted", "error", "ID", "Tweet", "Affect_Dimension"])
counter = 0
for row in reader:
	counter += 1
	content = []
	content.append(str(counter))
	content.append(str(row[1]))
	content.append(str(row[2]))
	content.append(str(float(row[2]) - float(row[1])))
	content.append(str(row[0]))
	content.append("'" + str(row[4]) + "'")
	content.append("valence")
	writer.writerow(content)

fp.close()
ofile.close()

