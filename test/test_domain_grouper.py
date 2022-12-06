from pathlib import Path
import unittest
import io
import sys
import os
from emailanalyzer.domain_grouper import DomainGrouper


class DomainGrouperTest(unittest.TestCase):

    _ROOT_PATH = Path(os.path.abspath(os.path.dirname(__file__))).parent
    _EMAILS_PATH = str(_ROOT_PATH.joinpath("emails"))

    def test_domain_grouping(self):

        answer_receiver = io.StringIO()
        sys.stdout = answer_receiver

        with open(
            os.path.abspath(os.path.dirname(__file__)) + "/answers/task_3_answer.txt",
            encoding="UTF_8",
        ) as file:
            answer = file.read()
            answer += "\n"  # Add additional newline to match answer file newline characters count

        DomainGrouper(self._EMAILS_PATH).print_results()

        self.assertEqual(answer, answer_receiver.getvalue(), "Answers not equal.")

    def test_for_duplicates(self):

        answer_receiver = io.StringIO()
        sys.stdout = answer_receiver

        DomainGrouper(self._EMAILS_PATH).print_results()
        self.assertNotIn(
            "rhodkiewicz@thompson.net\n    rhodkiewicz@thompson.net",
            answer_receiver.getvalue(),
            "Duplicates found.",
        )


if __name__ == "__main__":
    unittest.main()
