# importing required modules
import PyPDF2
import re;
import csv;

# creating a pdf file object
pdfFileObj = open('Investors.pdf', 'rb')
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# printing number of pages in pdf file
print(pdfReader.numPages)
lexicon = {};
# creating a page objectrf
pageObj = pdfReader.getPage(0)

OnePage = pageObj.extractText().lower().encode('ascii', 'ignore').decode('ascii') #removing all the asccii character or special character
OnePage = OnePage.replace('\n', ' ').replace('\r', '') #remove All enters seprately to replace by a space key
#OnePage = re.sub(r'[^a-zA-Z ]',r'',OnePage); ## remove all except the alphabets
OnePage = re.sub(' +',' ',OnePage); ## remove double space
#RemoveEnter = OnePage.replace('\n', ' ').replace('\r', '')
words = OnePage.split(" ")
# extracting text from page
p = 0;
lexicon.update({'virjvierv': 1})
p = lexicon.get('virjvierv')+1


i = 1;
for word in words :
    if(word.__len__() < 20 and word.__len__()>0 and word.isalpha()):
        i2 = lexicon.get(word)  # will return the index of the word that will be the key
        if i2:  # if i2 is not null then this
            lexicon.update({word: (i2+1) })
        else :
            lexicon.update({word: 1})
#print(lexicon)
searchfile = open("data.txt", "r")
RankedWord = {};
total  =0;
for line in searchfile :
    words = line.split("\t");
    if (words[1].__len__() > 3 ):
        RankedWord.update({words[1].lower():int(words[3])})
        total = total+ int(words[3]);
FinalCorpuse = {};
for word in lexicon :
    rank = RankedWord.get(word);
    if rank is None  :
        rank = 1  # just to avoid a 0 because it gives infinte in divison
    marks = int(total/(rank*lexicon.get(word)));
    FinalCorpuse.update({word:marks});
print(total)


with open('poc.csv', 'w') as csvfile:
    fieldnames = ['Word', 'Frequency']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for key in FinalCorpuse :
        writer.writerow({'Word': key, 'Frequency': FinalCorpuse.get(key)})
    searchfile.close()

#this below code is to ignore any utf-8 script it will remove it and then publish it to the doc...
#
#yourstring = yourstring.encode('ascii', 'ignore').decode('ascii')
pdfFileObj.close()



# let see if it works