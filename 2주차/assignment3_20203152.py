
import sys, pickle# import
#test3_2.dat 
#파일 open
fname = input("Enter data file name: ")

#파일 읽기 함수
def readScoreDB(dbfilename):
    try:
        fH = open(dbfilename)
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return[]
    else:
        print("Open DB: ", dbfilename)

    scdb = []
    
    for line in fH:
        dat = line.strip()
        person = dat.split(",")
        record = {}
        for attr in person:
            kv = attr.split(":")
            record[kv[0]] = kv[1]
        scdb += [record]
    return scdb
    


#파일 쓰기 함수
def writeScoreDB(scoredb):
    fH = open(fname, 'w')
    for p in scoredb:
        pinfo = []
        for attr in p:
            pinfo += [attr + ":" + p[attr]]
        line = ','.join(pinfo)
        fH.write(line + '\n')
    fH.close()



#파일내용 출력함
def showScoreDB(scoredb, keyname):
    for p in sorted(scoredb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()

def doScoreDB(scoredb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "":
            continue
        parse = inputstr.split(" ")

        if parse[0] == 'add':
            try:
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                scoredb += [record]
            except IndexError :
                print("you should type name, age and score")
            """try :
                a, b = int(record[1]), int(record[2])
                    
            except : 
                scoredb += [record]
            else :
                print("age and score should be int")"""
            

        elif parse[0] == 'del':
            for p in scoredb:
                if p['Name'] == parse[1]:
                    scoredb.remove(p)
                    break
                    
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scoredb, sortKey)

        elif parse[0] == 'quit':
            break

        else:
            print("Invalid command: " + parse[0]) 




scoredb = readScoreDB(fname)
doScoreDB(scoredb)
writeScoreDB(scoredb)

#출력
"""for line in fH:
    words = line.split()
    
for word in wordcount:
    if word in wordcount:
        wordcount[word] += 1
    else:
        wordcount[word] = 1
        """
