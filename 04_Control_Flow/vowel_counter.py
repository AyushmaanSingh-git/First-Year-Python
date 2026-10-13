count = 0
text = input("Enter a word: ")
for i in text:
    if i.lower() in 'aeiou':
        count = count + 1
print("Total vowels are", count)