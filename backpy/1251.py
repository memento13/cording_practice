w = input()
word_list = list()

def exchange(eword):
    eword = list(eword)
    eword.reverse()
    return "".join(eword)

def divide(word):
    length = len(word)
    for i in range(1,length-3):
        for j in range(i+1,length-2):
            i_word = word[:i]
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

