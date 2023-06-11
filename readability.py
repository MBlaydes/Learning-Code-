from cs50 import get_string

# get text
text = get_string("Text: ")

letters = 0
words = 1
sentences = 0

# count letters, sentences and words
for i in text:
    if i.isalpha():
        letters+=1
    elif i == " ":
         words +=1
    elif i == '.', '?', '!')
    sentences +=1


# run readability formula
r = 0.0588 * (letters / words * 100) - 0.296 * (sentences / words * 100) - 15.8

# print results
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+ ")
else:
    print("Grade ", round(index))
