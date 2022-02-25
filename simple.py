import hashlib
import pprint
from itertools import count

def doit():
    blocksize=1024
    dedupedict={}
    count=0
    dedupeditems=0

    with open("dedupetest__90pct_1g","rb") as f:
        while True:
            read_data = f.read(blocksize)
            if not read_data:
                break 
            count+=1
            h=hashlib.new('sha256')
            h.update(read_data)
            digest=(h.hexdigest())
            if digest in dedupedict.keys():
                dedupedict[digest]=dedupedict[digest]+1
            else:
                dedupedict[digest]=1
    print("Total Lines read")        
    print(count)
    dedupehisto={}
    for key in dedupedict.keys():
        duplicates=dedupedict[key]
        if duplicates in dedupehisto.keys():
            dedupehisto[duplicates]=dedupehisto[duplicates]+1
            dedupeditems=dedupeditems+1
        else:
            dedupehisto[duplicates]=1
    pprint.pprint(dedupehisto)
    print("Deduped items=",dedupeditems)
    print("Original items=",count)    
    print("Ratio = ",dedupeditems/count)
    print("PCT = ",(dedupeditems/count)*100)

if __name__=="__main__":
    doit()