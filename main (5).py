word = input("Word to convert: ")  # prompts user to enter word
count = int(input("How many letters at the end of the word should be converted? "))  # prompts user to enter the count
totalLength = len(word)  # calculates the total length of the user input word
startLength = totalLength - count  # gets the start length which won't be in uppercase

start = ""  # initialize variables
end = ""

# assigns the string from index=0 to index=startLength of variable start so that they won't be converted to uppercase
start = word[0:startLength]

# assigns the string from index=startLength to index=totalLength of variable end so that
# they can be converted to uppercase
end = word[startLength:totalLength]
end = end.upper()  # convert the string in variable end to uppercase

word = start + end  # appends both start and end strings
print(word)  # prints the resultant word on the screen
