# Finding the longest word
def getLongestString(arrayOfStrings):
    logestString = ''
    for string in arrayOfStrings:
        if len(string) > len(logestString):
            logestString = string
            
    return logestString


# Mapping a string
def mapString(string):
    map = {}
    for i in range(len(string)):
        letter = string[i]
        if letter in map.keys():
            map[letter].append(i)
        else:
            map[letter] = [i]
            
    return map

# Finding subsequence
def isSubsequence(word, object):
    minIndex = 0
    for i in word:
        if i in object:
            minIndex = findNextIndex(object[i], minIndex)
            if minIndex == False:
                return False
        else:
            return False    
    return True

# Looking out the right place
def findNextIndex(array, minIndex):
    for i in array:
        if i >= minIndex:
            return i + 1
        
    return False

# Finding out a match subsequence
def longestMatch(string, dictionary):
    map = mapString(string)
    listOfSubsequences = []
    
    for element in dictionary:
        if isSubsequence(element, map):
            listOfSubsequences.append(element)
            
    listOfSubsequences.reverse()
    longest = getLongestString(listOfSubsequences)
    
    return longest


# Main
def run():
    strings = [
        'vascular',
        'vat',
        'avast',
        'javas',
        'art',
        'script'
    ] 
    stringSecuence = 'javascript'
    
    words = '\n'.join(strings)
    print(f'Words:\n{words}\n')
    
    print(f'The longest subsequence of {stringSecuence} is: ' + longestMatch(stringSecuence, strings))
    

if __name__ == '__main__':
    run()