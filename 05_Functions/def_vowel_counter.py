def count_vowels(text):
    count = 0
    for i in text:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count = count + 1
    print("Total vowels are", count)

word = input("Enter a word: ")
count_vowels(word)