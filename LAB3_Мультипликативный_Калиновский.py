alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
m = 4096
y = [0]*8
y[0] = 502
a = 9

num_word_str =[]
num_word = []
word_encode = []
decode_word = []
word = input('Введите слово: ').upper()

for i in word:
    num_word_str.append(alph.index(i)+1)

for i in range(1, len(word)):
    y[i] = (a * y[i-1] ) % m
print(y)

for i in range(len(num_word_str)):
    num_word.append((y[i] + num_word_str[i])%len(alph))


for i in num_word:
    word_encode.append(alph[i])


word2 = ''.join(word_encode)
print(word2)
num_word_str_decode = []
num_word_decode = []
for i in word2:
    num_word_str_decode.append(alph.index(i))


for i in range(len(num_word_str_decode)):
    num_word_decode.append((num_word_str_decode[i]+26 - y[i])%len(alph))

for i in num_word_decode:
    decode_word.append(alph[i-1])
print(''.join(decode_word))
