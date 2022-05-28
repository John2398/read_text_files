# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    filename = input('Add file path: ')
    print(filename)
    with open(filename) as file:
        contents = file.read()
        print(contents)
        return "Hello World"

read_file_content('filename')


def count_words(filename):
    text = read_file_content("./story.txt")
    
    # [assignment] Add your code here
    dikt = {}
    with open("./story.txt") as file:
        for line in file:
            (key, val) = line.split()
            dikt[int(key)] = val

            print (d)
            return {"as": 10, "would": 20}
        
count_words('filename')