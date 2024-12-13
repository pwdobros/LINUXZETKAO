import csv

def readSimpleCSV():
    with open("data_simple.csv", "rt") as fData:
        while True:
            row = fData.readline()
            if not row:
                break
    
        row = row.strip()
        row = row.split(",")
        print(row)
        print(row[1],type(row(1)))
        print (row[0], type(row[0])), int(row[0])
        type(int(row[0]))

def readCSV():
    with open("data_simple.csv", "rt") as fData:
        csvReader = csv.Reader(fData, delimiter=",")
        lineCount = 0
        for row in csvReader:
            if lineCount == 0:
                print (f"Column names are {", ".join(row)}'")
            else:
                print(row)
                print(row[1])
            lineCount += 1
    print (f"Number of rows: {lineCount}")

def readCSVIntoDict():
    with open("data_simple.csv", "rt") as fData:
        csvReader = csv.DictReader(fData, delimiter=",")
        lineCount = 0
        for row in csvReader:
            if lineCount == 0:
                print (f"Column names are {", ".join(row)}'")
            else:
                print(row)
                print(row[1])
            lineCount += 1
    print (f"Number of rows: {lineCount}")

def writeDataLisToCSV():
    with open("data out from list.csv", "wt") as fOut:
        csvWriter = csv.writer(fOut, delimiter=",",quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csvWriter.writerow([3,"c,d", 987.6])
        csvWriter.writerow([3,"e,f", 54.3])

def writeDataDictToCSV():
    with open("data out from dict.csv", "wt") as fOut:
        columnNames = ["c1", "c2", "c3"]
        csvWriter = csv.writer(fOut, fieldnames = columnNames, delimiter=",",quotechar='"', quoting = csv.QUOTE_MINIMAL)

        csvWriter.writeheader()

        csvWriter.writerow(["c1": 3,"c2": "c,d", "c3": 987.6])
        csvWriter.writerow(["c2": "e,f", "c3": 54.3, "c1":4])


def main():
    #readSimpleCSV
    #readCSV
    readCSVIntoDict
    writeDataLisToCSV




if __name__ == "__main__":
    main()