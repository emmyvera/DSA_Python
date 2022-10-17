'''
Construct an algorithm to check whether two words 
(or phrases) are anagrams or not!

"An anagram is a word or phrase formed by 
rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once"

For example: restful and fluster
'''

def is_anagram(word1, word2):
    
    #Check if the length is the same
    if len(word1) != len(word2):
        return False
    str1 = sorted(word1)
    str2 = sorted(word2)

    if str1 != str2:
        return False
    else:
        return True

print(is_anagram('restful', 'fluster'))
print(is_anagram('restful', 'fluste'))
print(is_anagram('restful', 'flusser'))