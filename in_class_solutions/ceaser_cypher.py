#Vincent Qu, 341089043

inp = input()
word, temp_shift = inp.split()
word = word[0 : len(word)-1].lower()
shift = int(temp_shift)%26

cypher = []
for i in range(2):
    for j in range(26):
        cypher.append(chr(j + ord('a')))

for char in word:
    print((cypher[ord(char) - ord('a') + shift]), end = "")

