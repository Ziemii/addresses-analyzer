from re import search as search_address
from emailanalyzer.addresses_reader_abc import AddressesReaderABC
from emailanalyzer.results_printer_abc import ResultsPrinterABC


class PhraseFilter(AddressesReaderABC, ResultsPrinterABC):
    """Filters out addresses without searched phrase."""

    def __init__(self, mails_directory, phrase):
        super(PhraseFilter, self).__init__(mails_directory)
        self._addresses_containing_phrase = []
        self._phrase = phrase
        self._remove_duplicates()
        self._filter_addresses_by_phrase()

    def _filter_addresses_by_phrase(self):
        self._addresses_containing_phrase = [
            ("    " + address)
            for address in self._addresses_list
            if self._is_phrase_in_address(address)
        ]

    def _is_phrase_in_address(self, address):
        return search_address(self._phrase, address)

    def print_results(self):
        print(
            f"Found emails with '{self._phrase}' in email ({len(self._addresses_containing_phrase)}):"
        )
        print(*self._addresses_containing_phrase, sep="\n")
