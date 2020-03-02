from urllib.request import urlopen

#from pyexcel_xls import read_data

url = input(" Enter a url \n")

print(url,":)\n")

u = url

#OPEN THE URL
fo = urlopen(url)

#READ THE URL
a = fo.read()

#ARRANGE IT BY BEAUTIFULSOUP
from bs4 import BeautifulSoup
soup = BeautifulSoup(a,"html.parser")
for script in soup(["script","style"]):
    script.extract()

text = soup.get_text()
lines = (line.strip() for line in text.splitlines())
s = list(lines)     #list of lines of text
d = "".join(s)
c = d.split()   #all words


#DISPLAY THE WORD IN LIST FORMAT
print("displaying the words in list format ---->\n",c,":)\n")


#CALCULATE TOTAL NUMBER OF WORDS
e = len(c)      #in the webpage
print("Total number of words ->",e,"\n")

#CALCULATE THE OCCURENCE
wordfreq = [c.count(w) for w in c]


#READ THE SELECTED WORD
key = input(" Enter a keyword\n")
r = key.split(',')
print(r,"\n")

#CONVERT IT AS DICT FORMAT
dic={}
for s1 in r:

    s1=s1.lower()
    for k,v in zip(c,wordfreq):
        k=k.lower()
        if s1==k:
            dic[s1]=v              

print("frequency of given keywords in dictionary format --->",dic,"\n")


#CALCULATE DENSITY OF THE WORD
den=[]
b1=list(dic.values())   #it's frequency in the webpage
c1=list(dic.keys())     #keyword/keywords given

print("Formula for density \n")
print("Density = Given word frequency / total number of words \n")
print ("Total number of words in the url given is: ",e,":)\n")

for d1 in b1:
    den.append((d1/e)*100)
    print("Density is :--->",den," :)\n")





