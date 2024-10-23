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
