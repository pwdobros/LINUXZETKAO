import json

def readJSONFile():
    with open ("data.json", "rt") as fData:
        data = json.load(fData)

    print(data["string"])
    print(data["object"]["a"][1])

def writeJSONFile():
    data = {"k1": "v1", "k2": 123}
    with open("data_out.json", "wt") as fOut:
        json.dump(data, fOut)

def fromJSONStringToObject():
    x = '{"k1": 1, "k2": "abc"}'
    y = json.loads(x)
    print(y["k2"])

def fromObjectToJSONString():
    x = '{"k1": 1, "k2": "abc"}'
    y = json.dump(x)
    print(y)
    print(type(y))


    


def main ():
    readJSONFile()
    

if __name__ == "__main__":
    main()