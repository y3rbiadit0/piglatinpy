from unittest import TestCase

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
