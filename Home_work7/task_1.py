word = str(input("Введите ваше предложение : "))
word_s = word.split(" ")
new_word = {}
for w in word_s:
    if w in new_word:
        new_word[w] += 1
    else:
        new_word[w] = 1
print(new_word)
