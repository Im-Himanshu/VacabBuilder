# importing required modules
import PyPDF2
import re;
import csv;

#define all variable here # this is more like a setting of this app
PdfFileName = 'ToProcessFile/Investors.pdf'
CorpusefileName = "InputFiles/20K.txt";
HardWordOutput = "OutputResults/hard.csv"; # name of file stroing hard word predicted
EasyWordOutput = "OutputResults/Easy.csv"; #name of the file stroing the easy word  (hard Union easy = universal set)
AllWordsFromDictionary = {}; # all words from data base with thier frequency
Words_from_doc = {}; # this will store all the words extracted from the pdf after doing all the filter and parsin
FinalCorpuse = {};
MinWordLength = 3; # to remove all word of length lower than this
MaxWordLength = 20;  # to remove all the word larger than this, this is to remove junk like URL, based on the assumption that most of the english word are of lower length than this
Totalfreq =0 ; # this will calcualte the sum of freq given in the corpuse
TotalMarks = 0; #cumulative score of all the marks in the lexicon to give some average number and define he easy and hard word

def getNumberOfPages () :
    pdfFileObj = open(PdfFileName, 'rb')
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # printing number of pages in pdf file
    NumPages =  pdfReader.numPages;
    pdfFileObj.close();
    return NumPages;




#this will read the pdf and return the page at given pageNumber of the pdf after reading
def ReadPdf (pageNumber):
    # creating a pdf file object
    pdfFileObj = open(PdfFileName, 'rb')
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # printing number of pages in pdf file
    print(pdfReader.numPages)
    # creating a page objectrf
    pageObj = pdfReader.getPage(pageNumber)
    TextString = pageObj.extractText();
    pdfFileObj.close()
    return TextString;
# this will perform removal of unwanted text and character from the string
def TextFilterAndProcessing (TextString) :
    #pageObj = ReadPdf();
    OnePage = TextString.lower().encode('ascii', 'ignore').decode('ascii') #removing all the asccii character or special character
    OnePage = OnePage.replace('\n', ' ').replace('\r', '') #remove All enters seprately to replace by a space key
    #OnePage = re.sub(r'[^a-zA-Z ]',r'',OnePage); ## remove all except the alphabets
    OnePage = re.sub(' +',' ',OnePage); ## remove double space
    #RemoveEnter = OnePage.replace('\n', ' ').replace('\r', '')
    words = OnePage.split(" ")
    return words
    # extracting text from page

def AddWordsToLexicon (words):
    i = 1;
    lexicon_local = {};
    for word in words :
        if(word.__len__() < MaxWordLength and word.__len__()>MinWordLength and word.isalpha()):
            CurrentFreq = lexicon_local.get(word)  # will return the index of the word that will be the key
            if CurrentFreq is None :  # if i2 is null then insert the word with freq 1
                lexicon_local.update({word: 1})
            else :
                lexicon_local.update({word: (CurrentFreq+1) }) #update the freq to +1
    return lexicon_local;

def ReadFrequencyData():
    global Totalfreq ;
    Totalfreq = 1;
    AllWordsFromDictionary_local = {};
    searchfile = open(CorpusefileName , "r")
    for line in searchfile :
        if (words[0].__len__() > MinWordLength ):
            AllWordsFromDictionary_local.update({words[0].lower():Totalfreq}) #at words[1] is the word and at 3 is the freq, dispersion is at 4
            Totalfreq = Totalfreq+ 1; #this will give totalFreq for formula derived later
    return AllWordsFromDictionary_local;
# at this point we have read all the pdf and files and stored it in data now time to give results
def GetWordMarks():
    global  Words_from_doc;
    global  TotalMarks;
    global  AllWordsFromDictionary;
    global FinalCorpuse;
    default = len(AllWordsFromDictionary)
    print(AllWordsFromDictionary)
    for word in Words_from_doc :
        #rank2 = AllWordsFromDictionary[word];
        rank = AllWordsFromDictionary.get(word, default);
        FinalCorpuse.update({word:rank})
        # lastKey = None;
        # for key in AllWordsFromDictionary : # so exit when the first if condition is executed.. that is lastkey is set to soemthing
        #     if lastKey is not None :
        #         break;
        #     if  word in key or key in word :
        #         lastKey = key;
        # Score = 1   #default value to avoid 0
        # if lastKey is not None :
        #     Score = AllWordsFromDictionary.get(lastKey)
        # Marks = Totalfreq/ (Score*lexicon.get(word))
        # TotalMarks = TotalMarks+Marks;
        # FinalCorpuse.update({word: Marks})






#this function is to publish output in the final files as mentioned above
def PublishOutput():
    global  FinalCorpuse;
    AvgMarks = TotalMarks/FinalCorpuse.__len__();
    with open(HardWordOutput, 'w') as csvfile :
        fieldnames = ['Word', 'Frequency']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for key in FinalCorpuse :
            #if FinalCorpuse.get(key) >= AvgMarks:
            writer.writerow({'Word': key, 'Frequency': FinalCorpuse.get(key)})
    with open(EasyWordOutput, 'w') as csvfile2 :
        fieldnames2 = ['Word', 'Frequency']
        writer2 = csv.DictWriter(csvfile2, fieldnames=fieldnames2)
        writer2.writeheader()
        for key in FinalCorpuse :
            #if FinalCorpuse.get(key) < AvgMarks:
            writer2.writerow({'Word': key, 'Frequency': FinalCorpuse.get(key)})


#this is the main function of the class this will call all the function one by one in orderly manner to avoid mayhem
#def main():
pageNumber = getNumberOfPages();
OnePageObj = ReadPdf(pageNumber-1); #pagenumber gives the pagenumber which we have to read so applying a for loop here will loop through all pages
FilteredWords = TextFilterAndProcessing(OnePageObj) #this will be array or rather a list of words from the parsed page after filteration                                                     #and parsing
Words_from_doc = AddWordsToLexicon(FilteredWords); #this will update the lexicon to add the above word
AllWordsFromDictionary  = ReadFrequencyData();
GetWordMarks();
PublishOutput();





#if __name__== "__main__":
#    main()



#this below code is to ignore any utf-8 script it will remove it and then publish it to the doc...
#
#yourstring = yourstring.encode('ascii', 'ignore').decode('ascii')



# let see if it works