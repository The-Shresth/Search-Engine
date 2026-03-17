import os

# pointing to folder
doc_dir = "./documents"
inverted_index = {}

# reading files and mapping words to file names
for filename in os.listdir(doc_dir):
    if filename.endswith(".txt"):
        with open(os.path.join(doc_dir, filename), 'r') as f:
            content = f.read().lower() #making everything lowercase
            words = content.split() #breaking the text into list of words


            for word in words:
                if word not in inverted_index:
                    inverted_index[word] = set()
                
                inverted_index[word].add(filename) #adding filename to the set for this word
# print(f"Index built! I found {len(inverted_index)} unique words.")
#taking query from user
query = input("Search for the word: ").lower()

if query in inverted_index:
    print(f"Found '{query}' in: {inverted_index[query]}")
else:
    print("No results found.")


