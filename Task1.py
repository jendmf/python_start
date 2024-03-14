import string

text = input('text ').lower()
x = {}

for word in string.punctuation:
    text = text.replace(word, ' ')
text = text.split()

for word in text:
    if word not in x:
        x[word] = text.count(word)

print(x)
