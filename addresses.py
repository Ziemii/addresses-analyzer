import sys
from emailanalyzer.mail_arguments_parser import MailArgumentsParser
from emailanalyzer.invalid_addresses_finder import InvalidAddressesFinder
from emailanalyzer.phrase_filter import PhraseFilter
from emailanalyzer.domain_grouper import DomainGrouper
from emailanalyzer.unused_email_log_finder import UnusedEmailLogFinder


def main():

    arguments = MailArgumentsParser(sys.argv[1:])

    if arguments.incorrect_emails:
        InvalidAddressesFinder(arguments.mails_directory).print_results()

    if arguments.search_phrase:
        PhraseFilter(arguments.mails_directory, arguments.search_phrase).print_results()

    if arguments.group_by_domain:
        DomainGrouper(arguments.mails_directory).print_results()

    if arguments.log_path:
        UnusedEmailLogFinder(
            arguments.mails_directory, arguments.log_path
        ).print_results()


if __name__ == "__main__":
    main()
