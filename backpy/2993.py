w = input()
word_list = list()

def exchange(eword):
    eword = list(eword)
    length = len(eword)
    for i in range(length//2):
        temp = eword[length-1-i]
        eword[length-1-i] = eword[i]
        eword[i] = temp
    return "".join(eword)

def divide(word):
    length = len(word)
    for i in range(length-2):
        for j in range(i+1,length-1):
            i_word = word[:i+1]
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

