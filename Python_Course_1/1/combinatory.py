import csv

def filewrite(data):
    with open('combinatory_output.csv', 'a+', newline='') as f:

        writer = csv.writer(f, delimiter=',')
        datasec = data.split(',')
        writer.writerow(datasec)

aList = ['0','1','2','3','4','5','6','7','8','9']

for a in range(0, len(aList)):
    filewrite(aList[a])
    for b in range(0, len(aList)):
        filewrite(aList[a]+aList[b])
        for c in range(0, len(aList)):
            filewrite(aList[a]+aList[b]+aList[c])
            for d in range(0, len(aList)):
                filewrite(aList[a]+aList[b]+aList[c]+aList[d])
                for e in range(0, len(aList)):
                    filewrite(aList[a]+aList[b]+aList[c]+aList[d]+aList[e])
                    for f in range(0, len(aList)):
                        filewrite(aList[a]+aList[b]+aList[c]+aList[d]+aList[e]+aList[f])
                        for g in range(0, len(aList)):
                            filewrite(aList[a]+aList[b]+aList[c]+aList[d]+aList[e]+aList[f]+aList[g])
                            for h in range(0, len(aList)):
                                filewrite(aList[a]+aList[b]+aList[c]+aList[d]+aList[e]+aList[f]+aList[g]+aList[h])
                                for i in range(0, len(aList)):
                                    filewrite(aList[a]+aList[b]+aList[c]+aList[d]+aList[e]+aList[f]+aList[g]+aList[h]+aList[i])
                                    for j in range(0, len(aList)):
                                        filewrite(aList[a]+aList[b]+aList[c]+aList[d]+aList[e]+aList[f]+aList[g]+aList[h]+aList[i]+aList[j])
