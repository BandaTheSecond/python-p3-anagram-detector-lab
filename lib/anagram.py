# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        matches = []
        sorted_word = sorted(self.word)
        
        for candidate in word_list:
            candidate_lower = candidate.lower()

            if sorted(candidate_lower) == sorted_word:
                matches.append(candidate)
        return matches
