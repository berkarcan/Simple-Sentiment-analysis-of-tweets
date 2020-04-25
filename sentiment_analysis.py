# Program to remove punctuation characters in the strings
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(s):
    for c in s:
        if c in punctuation_chars: s=s.replace(c,'')
    return s
 
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
def get_pos(sp):
    words=strip_punctuation(sp).lower().split()
    return len([word for word in words if word in positive_words])

# list of negative words to use
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(sn):
    words=strip_punctuation(sn).lower().split()
    return len([word for word in words if word in negative_words])

data = open("project_twitter_data.csv","r")
resultingdata = open("resulting_data.csv","w")

lines =  data.readlines()

resultingdata.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
resultingdata.write("\n")

for line in lines[1:]:
    lst= line.strip().split(',')
    resultingdata.write("{}, {}, {}, {}, {}".format(lst[1], lst[2], get_pos(lst[0]), get_neg(lst[0]), (get_pos(lst[0])-get_neg(lst[0]))))    
    resultingdata.write("\n")
    
data.close()
resultingdata.close()