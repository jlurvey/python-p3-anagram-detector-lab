# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, word_list):
        anagrams = []

        lower_case_word = self.word.lower()

        for word in word_list:
            lower_case_list_word = word.lower()

            if lower_case_word != lower_case_list_word and sorted(lower_case_word) == sorted(lower_case_list_word):
                anagrams.append(lower_case_list_word)

        return anagrams

