from dataclasses import dataclass, field
from typing import ClassVar, List
import random


def load_words():
    words = open("words.txt", "r")
    line = words.readline()
    word_list = line.split(" ")
    print("words loaded successfully")
    return tuple(word_list)


@dataclass
class Words:
    _words: ClassVar[List[str]] = load_words()

    @classmethod
    def get_random_word(cls) -> str:
        words_num = len(cls._words)
        rand_num = random.randrange(0, words_num - 1)
        return cls._words[rand_num]


@dataclass
class Word:
    _word: str = field(default_factory=Words.get_random_word, init=False)
    _user_word: List[str] = field(init=False)
    _word_chars: set = field(init=False)
    _char_used: List[str] = field(default_factory=lambda _=0:[], init=False)
  
    def __post_init__(self):
        self._word_chars = set(self._word)
        self._user_word = ["-"] * len(self._word)

    def is_char_in(self, char: str) -> bool:
        return char in self._word_chars

    def show_char(self, char: str) -> None:
        for index, word_char in enumerate(self._word):
            if word_char == char:
                self._user_word[index] = char

    def guess(self, char: str) -> bool:
        if char in self._char_used:
            return False
        if not self.is_char_in(char):
            return False
        self.show_char(char)
        return True

    def get_user_word(self) -> str:
        return ''.join(self._user_word)
    
    def is_finished(self) -> bool:
        return self._word == ''.join(self._user_word)
