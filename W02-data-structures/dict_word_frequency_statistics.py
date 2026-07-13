sentence = "The quick brown fox jumps over the lazy dog. The dog barked at the fox."

word_count = {}

for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.items():
    print(f"{word}: {count}")
    

