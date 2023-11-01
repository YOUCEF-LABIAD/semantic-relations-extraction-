class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.term_ids = []

# Example usage:
# Create a TrieNode instance
node = TrieNode()



#To implement the Aho-Corasick algorithm to read a file and construct a corresponding Trie for searching composed words, you can follow these steps in Java:

#  1-First, create a TrieNode class to represent nodes in your Trie:
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.term_ids = []


#  2-Create a Trie class to build the Trie and perform searches:


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, term, term_id):
        current = self.root
        for c in term:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.is_end_of_word = True
        current.term_ids.append(term_id)

    def search(self, text):
        matched_term_ids = []
        current = self.root

        for c in text:
            if c in current.children:
                current = current.children[c]
                if current.is_end_of_word:
                    matched_term_ids.extend(current.term_ids)
            else:
                current = self.root

        return matched_term_ids

if __name__ == "__main__":
    # Create a Trie instance
    trie = Trie()

    # Read and process the file containing composed words
    with open("your_input_file.txt", "r") as file:
        for line in file:
            parts = line.strip().split(";")
            if len(parts) >= 3:
                term_id = int(parts[0])
                term = parts[1]
                trie.insert(term, term_id)

    # Perform a search in the Trie
    search_text = "sir Sacheverell Sitwell and Marcel Gotlieb Gotlib"
    matched_term_ids = trie.search(search_text)

    # Print the matched term IDs
    print("Matched Term IDs:", matched_term_ids)










class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.term_ids = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, term, term_id):
        current = self.root
        for c in term:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.is_end_of_word = True
        current.term_ids.append(term_id)

    def search(self, text):
        matched_term_ids = []
        current = self.root

        for c in text:
            while current is not None and c not in current.children:
                current = current.failure_link
            if current is None:
                current = self.root
            else:
                current = current.children[c]
                if current.is_end_of_word:
                    matched_term_ids.extend(current.term_ids)

        return matched_term_ids

# Create a Trie instance
trie = Trie()

# Read and process the file containing composed words
with open("your_input_file.txt", "r") as file:
    for line in file:
        parts = line.strip().split(";")
        if len(parts) >= 3:
            term_id = int(parts[0])
            term = parts[1]
            trie.insert(term, term_id)

# Perform a search in the Trie
search_text = "sir Sacheverell Sitwell and Marcel Gotlieb Gotlib"
matched_term_ids = trie.search(search_text)

# Print the matched term IDs
print("Matched Term IDs:", matched_term_ids)
	




//Replace "your_input_file.txt" with the actual path to your file containing the composed words.
// This code will read the file, construct the Trie, and perform a search for terms in a given text.
// The matched term IDs will be printed to the console.
