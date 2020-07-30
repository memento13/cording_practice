import sys

sentence = sys.stdin.readline()
blank = sentence.count(' ')
sentence = list(sentence.split())
print("문장의 단어 수 = %d"%len(sentence))
print("띄어쓰기의 갯 수 = %d" %blank)
