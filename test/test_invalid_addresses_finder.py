from pathlib import Path
import unittest
import io
import sys
import os
from emailanalyzer.invalid_addresses_finder import InvalidAddressesFinder


class InvalidAddressesFInderTest(unittest.TestCase):

    _ROOT_PATH = Path(os.path.abspath(os.path.dirname(__file__))).parent
    _EMAILS_PATH = str(_ROOT_PATH.joinpath("emails"))

    def test_invalid_addresses_finder(self):
        with open(
            os.path.abspath(os.path.dirname(__file__)) + "/answers/task_1_answer.txt",
            encoding="UTF_8",
        ) as file:
            answer = file.read()
            answer += "\n"  # Add additional newline to match answer file newline characters count

        answer_receiver = io.StringIO(initial_value="baba")
        sys.stdout = answer_receiver

        InvalidAddressesFinder(self._EMAILS_PATH).print_results()
        self.assertEqual(
            sorted(answer), sorted(answer_receiver.getvalue()), "Answers not equal"
        )


if __name__ == "__main__":
    unittest.main()
