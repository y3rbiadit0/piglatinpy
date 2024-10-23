from src.error import PigLatinError


class PigLatinTranslator:
    _phrase: str

    def __init__(self, phrase: str):
        """
        Creates a pig latin translator given a phrase.
        :param phrase: the phrase.
        :raise PigLatinError: for any error situation.
        """
        self._phrase = phrase

    def get_phrase(self) -> str:
        """
        Returns the phrase.
        :return: the phrase.
        """
        return self._phrase

    def translate(self) -> str:
        """
        Returns the Pig Latin translation of the phrase.
        :return: the translation.
        """

        translator_map = {
            self._is_empty_phrase(): "nil",
            self._ends_with_y(): self._phrase + "nay",
            self._ends_with_vowel(): self._phrase + "yay",
            self._ends_with_consonant(): self._phrase + "ay"
        }

        translate_attempt = translator_map.get(True)
        if not translate_attempt:
            raise PigLatinError()
        return translate_attempt

    def _is_empty_phrase(self):
        return self._phrase == ""

    def _ends_with_y(self):
        return len(self._phrase) > 1 and self._phrase[-1] == "y"

    def _ends_with_vowel(self):
        return len(self._phrase) > 1 and self._phrase[-1].lower() in "aeiou"

    def _ends_with_consonant(self):
        return len(self._phrase) > 1 and self._phrase[
            -1].lower() in "bcdfghjklmnpqrstuvwxz"
