def main():
    path = filePath()
    with open(path) as file:
        fileContents = file.read()
        # print(fileContents)
        words = fileContents.split()
        
        wCount = wordCount(words)

        charsDict = charCount(words)
        #print(wCount)
        #print(charsDict)

        sortedCharDict = sortDict(charsDict)
        #print(" ")
        #print(sortedCharDict)
        
        print(f"-- Begin report of {path} ---")
        print(f"{wCount} words found in the document")
        print(" ")
        for index in sortedCharDict:
            print(f"The '" + f"{index['letter']}" + f"' character was found {index['count']} times")
        print("--- End report ---")


def filePath():
    return "books/frankenstein.txt"

def wordCount(book):
    return len(book)

def charCount(words):
    
    charDictionary = {}

    for word in words:
        for char in word:
            if char.lower() in charDictionary:
                charDictionary[f"{char.lower()}"] += 1
            else:
                charDictionary[f"{char.lower()}"] = 1
    
    return charDictionary

def sortParm(dict):
    return dict["count"] 

def sortDict(dictionary):
    sortedList = []

    for key in dictionary:
        if key.isalpha():
            sortedList.append({"letter": key, "count": dictionary[key]})

    sortedList.sort(reverse = True, key=sortParm)
    return sortedList

main()
