import unittest
from emailanalyzer.mail_arguments_parser import MailArgumentsParser


class TestParserMethods(unittest.TestCase):
    def test_mail_parser_mail_directory(self):
        testargs = ["./emails"]
        parser = MailArgumentsParser(testargs)

        self.assertEqual(parser.mails_directory, "./emails", "Path to emails incorrect")

    def test_mail_parser_incorrect_emails(self):
        testargs = ["-ic", "./emails"]
        parser = MailArgumentsParser(testargs)

        self.assertEqual(parser.incorrect_emails, True, "-ic is False")

        testargs = ["--incorrect-emails", "./emails"]
        parser = MailArgumentsParser(testargs)

        self.assertEqual(parser.incorrect_emails, True, "--incorrect-emails is False")

    def test_mail_parser_search(self):
        testargs = ["-s", "phrase", "./emails"]
        parser = MailArgumentsParser(testargs)

        self.assertEqual(parser.search_phrase, "phrase", "incorrect -s phrase")

        testargs = ["--search", "phrase", "./emails"]
        parser = MailArgumentsParser(testargs)

        self.assertEqual(parser.search_phrase, "phrase", "incorrect --search phrase")

    def test_mail_parser_gbd(self):
        testargs = ["-gbd", "./emails"]
        parser = MailArgumentsParser(testargs)

        self.assertEqual(parser.group_by_domain, True, "-gbd is False")

        testargs = ["--group-by-domain", "./emails"]
        parser = MailArgumentsParser(testargs)

        self.assertEqual(parser.group_by_domain, True, "--group-by-domain is False")

    def test_mail_parser_log_path(self):

        testargs = ["-feil", "log path", "./emails"]
        parser = MailArgumentsParser(testargs)

        self.assertEqual(parser.log_path, "log path", "incorrect -feil log path")

        testargs = ["--find-emails-not-in-logs", "log path", "./emails"]
        parser = MailArgumentsParser(testargs)

        self.assertEqual(
            parser.log_path, "log path", "incorrect --find-emails-not-in-logs log path"
        )

    def test_mail_parser_all_at_once(self):

        testargs = ["-ic", "-s", "phrase", "-gbd", "-feil", "log path", "./emails"]
        parser = MailArgumentsParser(testargs)

        self.assertEqual(parser.mails_directory, "./emails", "Path to emails incorrect")
        self.assertEqual(parser.incorrect_emails, True, "-ic is False")
        self.assertEqual(parser.search_phrase, "phrase", "incorrect -s phrase")
        self.assertEqual(parser.group_by_domain, True, "-gbd is False")
        self.assertEqual(parser.log_path, "log path", "incorrect -feil log path")


if __name__ == "__main__":
    unittest.main()
