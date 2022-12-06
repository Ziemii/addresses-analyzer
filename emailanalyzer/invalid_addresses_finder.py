from emailanalyzer.addresses_reader_abc import AddressesReaderABC
from emailanalyzer.results_printer_abc import ResultsPrinterABC
from emailanalyzer.address_validator import is_address_valid


class InvalidAddressesFinder(AddressesReaderABC, ResultsPrinterABC):
    """Finds invalid email addresses."""

    def __init__(self, mails_directory):
        super(InvalidAddressesFinder, self).__init__(mails_directory)
        self._invalid_emails = []
        self._find_invalid_mail_addresses()

    def _find_invalid_mail_addresses(self):
        self._invalid_emails = [
            ("    " + address)
            for address in self._addresses_list
            if not is_address_valid(address)
        ]

    def print_results(self):
        print(f"Invalid emails ({len(self._invalid_emails)}):")
        print(*self._invalid_emails, sep="\n")
