"""
Word Occurrences
Estimate: 20 minutes
Actual:   35 minutes
"""

text = input("Text: ")
words = text.split()

word_counts = {}
for word in words:
   if word in word_counts:
     word_counts[word] = word_counts[word] + 1
   else :
    word_counts[word] = 1

max_word = max(len(word) for word in word_counts)
sorted_word = sorted(word_counts)

for word in sorted_word:
    print(f"{word:{max_word}}: {word_counts[word]}")