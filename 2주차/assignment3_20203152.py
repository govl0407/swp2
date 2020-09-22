
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
                if parse[1].isalpha()==True and parse[1].isdigit()==True and parse[1].isdigit()==True :
                    scoredb += [record]
                else :
                    print("wrong input")
            except IndexError :
                print("you should type name, age and score")

            except KeyError:
                print("Invalid command")

            

                
            
        # del 명령시 scoredb중 일부를 읽지 않는 문제  
        elif parse[0] == 'del':
            try:
                for p in scoredb:
                    #print(p)
                    if p['Name'] == parse[1]:
                        print(p['Name']+"deleted")
                        scoredb.remove(p)
                    else :
                        print(p['Name']+"alive")
            except KeyError:
                print("Invalid command")
            except IndexError :
                print("Invalid command")
            



                    
        elif parse[0] == 'show':
            try:
                sortKey ='Name' if len(parse) == 1 else parse[1]
                showScoreDB(scoredb, sortKey)
            except KeyError:
                print("Invalid command")
            except IndexError :
                print("Invalid command")



        elif parse[0] =='find' :
            try:
                for p in scoredb:
                    if p['Name'] == parse[1]:
                        for attr in sorted(p):
                            print(attr + "=" + p[attr], end=' ')
                        print()
            except KeyError:
                print("Invalid command")
            except IndexError :
                print("Invalid command")



        elif parse[0] =='inc' :
            try:
               for p in scoredb:
                   if p['Name'] == parse[1]:
                       k = int(p['Score'])
                       n = str(k+int(parse[2]))
                       p['Score'] = n
            except KeyError:
                print("Invalid command")
            except IndexError :
                print("Invalid command")
                   
                   
    

        elif parse[0] == 'quit':
            try:
                break
            
            except KeyError:
                print("Invalid command")
            except IndexError :
                print("Invalid command")

        else:
            print("Invalid command: " + parse[0]) 




scoredb = readScoreDB(fname)
doScoreDB(scoredb)
writeScoreDB(scoredb)


