from pathlib import Path
import unittest
import io
import sys
import os
from emailanalyzer.unused_email_log_finder import UnusedEmailLogFinder


class UnusedEmailLogFinderTest(unittest.TestCase):

    _ROOT_PATH = Path(os.path.abspath(os.path.dirname(__file__))).parent
    _EMAILS_PATH = str(_ROOT_PATH.joinpath("emails"))
    _LOGS_LOCATION = _ROOT_PATH.joinpath("email-sent.logs")

    def test_unused_email_log_finder(self):

        answer_receiver = io.StringIO()
        sys.stdout = answer_receiver

        with open(
            os.path.abspath(os.path.dirname(__file__)) + "/answers/task_4_answer.txt",
            encoding="UTF_8",
        ) as file:
            answer = file.read()
            answer += "\n"  # Add additional newline to match answer file newline characters count

        UnusedEmailLogFinder(self._EMAILS_PATH, self._LOGS_LOCATION).print_results()

        self.assertEqual(answer, answer_receiver.getvalue(), "Answers not equal.")


if __name__ == "__main__":
    unittest.main()
