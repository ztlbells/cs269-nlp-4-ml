import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import re
import codecs
import nltk
# nltk.download('punkt')

emoji_pattern = re.compile(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)

# train
file_path 	= "0-1-train.csv"#"2018-Valence-reg-En-train.csv" #sys.argv[1]
fp 			= codecs.open(file_path, 'rb', encoding = "utf-8", errors = "ignore")
reader 		= csv.reader(fp)

# ofile  = open('0-1-train.csv', "wb")
# writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting = csv.QUOTE_ALL)

counter = 0
train = []
for row in reader:
# ID, Tweet, Affect Dimension, Intensity Score
# a score of 1: most positive mental state can be inferred; a score of 0: most negative mental state can be inferred
	# counter += 1

	# filter out emoji
	'''text = unicode(str(row[1]), errors='replace')
	text = emoji_pattern.sub(r'', text)
	b = TextBlob(text)
	tweet = str(b.correct())'''

	# print "tweet:", tweet

	'''if float(row[3]) > 0.5:
		t = (tweet, 'pos')
	else:
		t= (tweet, 'neg')'''
	train.append((unicode(str(row[0]), errors='replace'), str(row[1])))
	# writer.writerow([tweet, t[1]])

fp.close()
# ofile.close()

# train by NaiveBayes
start_time = time.time()
cl = NaiveBayesClassifier(train)
print "training cost", time.time() - start_time, "s"

# test/dev
file_path 	= "2018-Valence-reg-En-dev.csv" #sys.argv[1]
fp 			= codecs.open(file_path, 'rb')
reader 		= csv.reader(fp)

write_fp = "0-1-dev-result_" + str(int(time.time())) + ".csv"
ofile  = open(write_fp, "wb")
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting = csv.QUOTE_ALL)

# counter
cnt = 0
corr_cnt = 0

for row in reader:
	cnt += 1
	print "count:", cnt
	#text = emoji_pattern.sub(r'', str(row[1]))
	text = unicode(str(row[1]), errors='ignore')
	text = emoji_pattern.sub(r'', text)
	b = TextBlob(text)
	tweet = str(b.correct())

	prob_dist = cl.prob_classify(tweet)
	correct = ((float(row[3]) > 0.5) and (prob_dist.max() == 'pos')) or ((float(row[3]) < 0.5) and (prob_dist.max() == 'neg'))

	if correct == True:
		corr_cnt += 1;

	# ID, orig_score, est_score, 0-1 correct 
	writer.writerow([row[0], row[3], str(round(prob_dist.prob("pos"), 2)), str(correct)])
fp.close()
ofile.close()

print float(corr_cnt) / float(cnt)
