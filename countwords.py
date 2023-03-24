import os
import string

counts = dict()

# enter your directory
directory = input("Enter a directory: ")

try:
    # Loop over each file in this directory
    for filename in os.listdir(directory):
        # If the file ends with ".txt", open the file
        if filename.endswith(".txt"):
            # Constructs the full path to the file
            fh = os.path.join(directory,filename)
            with open(fh,'r') as file:
                # Convert all of the characters to lowercase
                # Strips white spaces,punctuations and digits
                # Split each line into a list of words
                for line in file:
                    line = line.lower().rstrip()
                    line = line.translate(line.maketrans('','',string.punctuation))
                    line = line.translate(line.maketrans('', '', string.digits))
                    words = line.split()

                    #For each word, update the word count in the counts dictionary
                    for word in words:
                        counts[word]= counts.get(word,0)+1

# Create a list called 'newlst'
# Append tuples of word counts and words into it
    newlst= list()
    for key,val in counts.items():
        a = (val,key)
        newlst.append(a)
# Sort newlst in reverse order based on the word counts
    newlst = sorted(newlst, reverse=True)

# Print the top five most frequent words in all the files
    for val, key in newlst[:5]:
        print(key, val)

except FileNotFoundError:
    print("Directory not found.")