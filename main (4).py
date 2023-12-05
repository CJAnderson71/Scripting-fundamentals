# reading sentence from user
sentence = input("Sentence: ")

# reading word from user
word = input("Word to look for in sentence: ")

# replacing spaces from sentence
sentence = sentence.replace(" ","")

# converting sentence to lower case
sentence = sentence.lower()

# converting word to lower case
word = word.lower()

count = 0

# looping through each index of sentence
for i in range(len(sentence)):

    # checking word starts from index i
    if sentence[i:].startswith(word):

        # incrementing the value of count by 1
        count += 1

# printing the output
print("There are",count,"occurrences of '"+word+"' in the sentence")
