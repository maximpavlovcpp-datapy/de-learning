numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 22, 33]
words = ["apple", "Banana", "cherry", "Date", "Elderberry"]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
squares=[n**2 for n in numbers if n%2==0]
print(squares)
long_lower=[n.lower() for n in words if len(n)>5]
print(long_lower)
word_lengths={word: len(word) for word in words}
print(word_lengths)
initials={n[0] for n in words}
print(initials)
flat=[n for row in matrix for n in row]
print(flat)
