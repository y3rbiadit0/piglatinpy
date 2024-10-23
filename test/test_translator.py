from unittest import TestCase

from src.error import PigLatinError
from src.translator import PigLatinTranslator


class TestPigLatinTranslator(TestCase):

    def test_get_phrase(self):
        # Arrange
        input_phrase = "phrase"
        translator = PigLatinTranslator(input_phrase)

        # Act
        result_phrase = translator.get_phrase()

        # Assert
        self.assertEqual(result_phrase, input_phrase)

    def test_translate_empty_string(self):
        # Arrange
        empty_string = ""
        translator = PigLatinTranslator(empty_string)
        expected_output = "nil"

        # Act
        result_phrase = translator.translate()

        # Assert
        self.assertEqual(result_phrase, expected_output)

    def test_translate_word_starting_vowel_ends_with_y(self):
        # Arrange
        empty_string = "any"
        translator = PigLatinTranslator(empty_string)
        expected_end = "nay"

        # Act
        result_phrase = translator.translate()

        # Assert
        self.assertEqual(result_phrase[-3:], expected_end)

    def test_translate_word_starting_vowel_ends_with_vowel(self):
        # Arrange
        empty_string = "epoque"
        translator = PigLatinTranslator(empty_string)
        expected_end = "yay"

        # Act
        result_phrase = translator.translate()

        # Assert
        self.assertEqual(result_phrase[-3:], expected_end)

    def test_translate_word_starting_vowel_ends_with_consonant(self):
        # Arrange
        empty_string = "ink"
        translator = PigLatinTranslator(empty_string)

        # Act
        result_phrase = translator.translate()

        # Assert
        self.assertEqual(result_phrase, "inkay")


    def test_translate_word_starting_vowel_invalid_char(self):
        # Arrange
        translator = PigLatinTranslator("ink1")

        # Assert
        self.assertRaises(PigLatinError, translator.translate)