
words_in_text = {}

text = input("Enter a text: ")
print(f"Text: {text}")
words = text.split()

for word in words:
    try:
        words_in_text[word] += 1
    except KeyError:
        words_in_text[word] = 1


