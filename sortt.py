import pandas as pd
from datetime import datetime
# from datetime import timedelta
def inserrt(dab, l):
    lisdate = datetime.strptime(l[3], "%d-%m-%Y")
    db = open(dab, 'r')
    dl = db.readlines()
    for i in range(len(dl)):
        dl[i] = dl[i].split(",")
    print(dl)
    i=1
    while(True):
        tempd = datetime.strptime(dl[i][3], "%d-%m-%Y")
        diff = (lisdate - tempd).days + 1
        if(diff>0):
            i+=1
        else:
            dl.insert(i, l)
            df = pd.DataFrame(dl)
            df.to_csv("db.csv", index=False,header=False)
            df.to_csv(index=False).encode("utf-8")
            print(df)
            df.to_csv("temp.csv",index=False, header=False)
            break

db = "db.csv"
# l = ['2022-11-5', "jhvjhvb", "1234567890", "9-11-2022", "aerwywgrf"]
l = ['2022-11-6', "jhvjhvb", "1234567890", "10-11-2022", "aerwywgrf"]
inserrt(db, l)

