import pickle
import re
def customResp(qname):
    (q, d) = pickle.load(open("responses.pickle", "rb"))
    if qname.startswith("checkin."):
        return {"TXT":d, "A":"0.0.0.0"}
    if qname[6:10]=="303a":
        d = "wait"
    q.append(qname);
    pickle.dump((q,d), open("responses.pickle", "wb"))
    return {"TXT":"ok", "A":"0.0.0.0"}
