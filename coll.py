#Given an array of strings (str), group the anagrams together. You can return the answer in any order.

def group_anagrams(strs):
    from collections import defaultdict
    anagram_dict = defaultdict(list)
    
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word].append(word)
    
    return list(anagram_dict.values())

strings = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams = group_anagrams(strings)
print(anagrams)
