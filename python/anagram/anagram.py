class _AnagramChecker:
    def __init__(self, word: str):
        self._word_lowered = word.lower()
        self._word_lowered_sorted = sorted(self._word_lowered)

    def is_anagram(self, candidate: str) -> bool:
        candidate_lowered = candidate.lower()
        return (
            self._word_lowered != candidate_lowered
            and self._word_lowered_sorted == sorted(candidate_lowered)
        )


def find_anagrams(word: str, candidates):
    checker = _AnagramChecker(word)
    return filter(checker.is_anagram, candidates)
