#Vincent Qu, 341089043

def ceaser_cypher(word, shift):
    ''' function encrypts word by shifting each character by that number of positions in the alphabet
    
    Args:
        word: the word to be encrypted, string
        shift: the number of positions to shift each letter by, works with negative numbers
    
    Returns:
        a string representing the encrypted ceaser cypher of the original word and shift values
    '''
    cypher = []
    ans = []
    for i in range(2):
        for j in range(26):
            cypher.append(chr(j + ord('a')))

    for char in word:
        ans.append(cypher[ord(char) - ord('a') + shift])

    return "".join(ans)


inp = input()
word, temp_shift = inp.split()
word = word[0 : len(word)-1].lower()
shift = int(temp_shift)%26

print(ceaser_cypher(word, shift))
