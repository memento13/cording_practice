w = input()
word_list = list()

def exchange(eword):
    eword.reverse()
    return "".join(eword)

def divide(word):
    word = list(word)
    length = len(word)
    if length ==3:
        word_list.append("".join(word))
    for i in range(1,length-1):
        for j in range(i+1,length):
            i_word = word[0:i]
            i_word=exchange(i_word)

            j_word = word[i:j]
            j_word=exchange(j_word)

            k_word = word[j:]
            k_word=exchange(k_word)

            temp = i_word+j_word+k_word
            word_list.append(temp)

divide(w)
word_list.sort()
print(word_list[0])

