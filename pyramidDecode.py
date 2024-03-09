
decodedMessage = []
mapDictionary = {}
lastElements = []

def storeInDict (words):
    wordList = words.split()
    mapDictionary.update({ wordList[0] : wordList[1]})

def toPyramid(dict):
    keys_list = list(dict.keys())
    totalPrinted = 0
    nextLine = 1
    i = 1
    while i < len(keys_list)+1:
        print(i, end=" ")
        totalPrinted+=1
        if totalPrinted == nextLine:
            lastElements.append(i)
            print()
            nextLine+=1
            totalPrinted=0
        i+=1

def readFromPyramid(elements):
    for element in elements:
        value = mapDictionary.get(str(element))
        print(value, end=" ")

def main():

    f = open("Desktop/decode/coding_qual_input.txt")
    for line in f:
        storeInDict(line)
    toPyramid(mapDictionary)
    print(lastElements)
    readFromPyramid(lastElements)

if __name__ == "__main__":
    main()

