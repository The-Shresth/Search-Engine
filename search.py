import os
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Ensure NLTK data is available
# nltk.download('stopwords') 

# Initializing tools
stemmer = PorterStemmer()
try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

# Cleaning text
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    cleaned = [stemmer.stem(w) for w in words if w not in stop_words]
    return cleaned

# Pointing to folder
doc_dir = "./documents"
# Ensure the directory exists so the code doesn't crash
if not os.path.exists(doc_dir):
    os.makedirs(doc_dir)
    print(f"Created {doc_dir} folder. Please add .txt files to it!")

inverted_index = {}

# Indexing files
for filename in os.listdir(doc_dir):
    if filename.endswith(".txt"):
        with open(os.path.join(doc_dir, filename), 'r', encoding='utf-8') as f:
            tokens = clean_text(f.read())
            for token in tokens:
                if token not in inverted_index:
                    inverted_index[token] = set()
                inverted_index[token].add(filename)

# Search Interface
query = input("Search for the terms: ")
mode = input("Search in (AND/OR): ").strip().upper()

query_tokens = clean_text(query)
results = None

for token in query_tokens:

    current_word_files = inverted_index.get(token, set())

    if results is None:

        results = current_word_files
    else:

        if mode == "AND":
            results = results & current_word_files
        else:
            results = results | current_word_files


if results:
    print(f"\nFound {len(results)} match(es) using {mode} logic:")
    for doc in results:
        print(f"- {doc}")
else:
    print("\nNo matching documents found.")