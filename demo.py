import csv

with open('names.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

f = open('csvfile.csv','w')
f.write('hi there\n') #Give your csv text here.
## Python will convert \n to os.linesep
f.close()

data = ['yahoo', 'machao', 'wohoo']
with open('eggs.csv', "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:



            writer.writerow(line)




            with open(EasyWordOutput, 'w') as csvfile2 :
                writer2 = csv.DictWriter(csvfile2, fieldnames=fieldnames)
            writer2.writeheader()

            for key in FinalCorpuse :
                if FinalCorpuse.get(key) < AvgMarks:
                    writer2.writerow({'Word': key, 'Frequency': FinalCorpuse.get(key)})
                if FinalCorpuse.get(key) > AvgMarks:
                    writer.writerow({'Word': key, 'Frequency': FinalCorpuse.get(key)})
