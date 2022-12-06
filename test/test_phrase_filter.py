from pathlib import Path
import unittest
import io
import sys
import os
from emailanalyzer.phrase_filter import PhraseFilter


class PhraseDuplicatesTest(unittest.TestCase):

    _ROOT_PATH = Path(os.path.abspath(os.path.dirname(__file__))).parent
    _EMAILS_PATH = str(_ROOT_PATH.joinpath("emails"))
    _ANSWER_PHRASE = "agustin"
    _DUPLICATE_PHRASE = "rhodkiewicz"

    def test_for_duplicates(self):

        answer_receiver = io.StringIO()
        sys.stdout = answer_receiver

        answer = "Found emails with 'rhodkiewicz' in email (1):\n    rhodkiewicz@thompson.net\n"
        PhraseFilter(self._EMAILS_PATH, self._DUPLICATE_PHRASE).print_results()

        self.assertEqual(
            sorted(answer),
            sorted(answer_receiver.getvalue()),
            "Result doesn't match expected answer."
        )
        sys.stdout = sys.__stdout__

    def test_phrase_filter(self):

        answer_receiver = io.StringIO()
        sys.stdout = answer_receiver

        with open(
            os.path.abspath(os.path.dirname(__file__)) + "/answers/task_2_answer.txt",
            encoding="UTF_8",
        ) as file:
            answer = file.read()
            answer += "\n"  # Add additional newline to match answer file newline characters count

        PhraseFilter(self._EMAILS_PATH, self._ANSWER_PHRASE).print_results()
        self.assertEqual(
            sorted(answer),
            sorted(answer_receiver.getvalue()),
            f"Address with phrase '{self._ANSWER_PHRASE}' wasn't found."
        )
        sys.stdout = sys.__stdout__


if __name__ == "__main__":
    unittest.main()
