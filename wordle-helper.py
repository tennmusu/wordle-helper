import sqlite3
import re
hint={}
notused=[]
conn=sqlite3.connect("./wnjpn/wnjpn.db")
while True:
    pattern = '^'+input('正規表現は？')+'$' 
    y=input('黄色は？')
    if y!='':
        yellow=y.split(' ')
        for y in yellow:
            pair=list(y)
            if hint.get(pair[0], "Null")=="Null":
                hint[pair[0]]=[int(pair[1])]
            else:
                hint.get(pair[0]).append(int(pair[1]))
    notused.extend(list(input('使わないのは？')))
    cur = conn.execute("select lemma from word where lang='eng'")
    isfilled=True
    for row in cur:
        m=re.match(pattern,row[0])
        isfilled=True
        if m!=None:
            keys=hint.keys()
            for k in keys:
                if not k in (row[0]):
                    isfilled=False
                    break
                else:
                    l=list(row[0])
                    for n in hint.get(k):
                        if l[n-1]==k:
                            isfilled=False
                            break
            if isfilled:
                for n in notused:
                    if  n in (row[0]):
                        isfilled=False
                        break

                if isfilled:
                    print(m.group(0))