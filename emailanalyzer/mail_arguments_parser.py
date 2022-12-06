import argparse


class MailArgumentsParser:
    """Parses arguments and exposes usable values."""

    def __init__(self, args):
        self._create_parser()
        self._add_arguments_to_parser()
        self._save_provided_arguments(args)

    def _create_parser(self):
        self._parser = argparse.ArgumentParser()

    def _add_arguments_to_parser(self):
        self._parser.add_argument("mails_directory", help="Directory with email files")
        self._parser.add_argument(
            "--incorrect-emails",
            "-ic",
            action="store_true",
            help="Prints incorrect emails",
        )
        self._parser.add_argument(
            "--search", "-s", help="Prints addresses with searched phrase in them"
        )
        self._parser.add_argument(
            "--group-by-domain",
            "-gbd",
            action="store_true",
            help="Prints addresses grouped by domain",
        )
        self._parser.add_argument(
            "--find-emails-not-in-logs",
            "-feil",
            help="Prints addresses unused in provided log path",
        )

    def _save_provided_arguments(self, args):
        arguments = self._parser.parse_args(args)
        self._mails_directory = arguments.mails_directory
        self._incorrect_emails = arguments.incorrect_emails
        self._search_phrase = arguments.search
        self._group_by_domain = arguments.group_by_domain
        self._find_emails_not_in_logs = arguments.find_emails_not_in_logs

    @property
    def mails_directory(self):
        return self._mails_directory

    @property
    def incorrect_emails(self):
        return self._incorrect_emails

    @property
    def search_phrase(self):
        return self._search_phrase

    @property
    def group_by_domain(self):
        return self._group_by_domain

    @property
    def log_path(self):
        return self._find_emails_not_in_logs
