import os
import inverted_index

doc_dir = "./documents"

if not os.path.exists(doc_dir):
    print(f"Error: The directory {doc_dir} was not found")
else:
    for filename in os.listdir(doc_dir):
     if filename.endswith(".txt"):
          file_path = os.path.join(doc_dir, filename)
          with open(file_path,'r', encoding = 'utf-8') as f:
               current_offset = 0
               for line_num, line_text in enumerate(f,1):
                    words = inverted_index.manual_clean(line_text)

                    for word in words:
                        inverted_index.add_to_index(word,filename,line_num, current_offset)
                    current_offset += len(line_text)


def get_snippet(filename, offset, length=50):
    file_path = os.path.join("./documents", filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        # Moving the 'cursor' to the stored offset
        f.seek(offset)
        snippet = f.read(length)
        return snippet.replace('\n', ' ')

user_query = input("\nEnter word to search: ").strip().lower()

cleaned_query = inverted_index.manual_clean(user_query)

if not cleaned_query:
    print("Please enter a valid word.")
else:
    word = cleaned_query[0]
    
    if word in inverted_index.inverted_index:
        results = inverted_index.inverted_index[word]
        
        sorted_files = sorted(results.items(), key=lambda x: x[1]['count'], reverse=True)

        print(f"\n--- Found '{word}' in {len(sorted_files)} files ---")

        for filename, metadata in sorted_files:
            print(f"\n {filename} (Occurrences: {metadata['count']})")
            
            first_offset = metadata['offsets'][0]
            context = get_snippet(filename, first_offset)
            print(f"   Snippet: ...{context}...")
            print(f"   Found on line(s): {metadata['lines']}")

    else:
        print(f"No results found for '{word}'.")
