from re import search as find_address
from emailanalyzer.addresses_reader_abc import AddressesReaderABC
from emailanalyzer.results_printer_abc import ResultsPrinterABC


class UnusedEmailLogFinder(AddressesReaderABC, ResultsPrinterABC):
    """
    Cleans up initial addresses list, reads addresses from log file
    and compares both lists for addresses not used in log.
    """

    def __init__(self, mails_directory, log_path):
        super(UnusedEmailLogFinder, self).__init__(mails_directory)
        self._logged_addresses = []
        self._addresses_not_used_in_logs = []
        self._remove_duplicates()
        self._remove_invalid_addresses()
        self._sort_addresses()
        self._extract_addresses_from_log(log_path)
        self._find_addresses_not_used_in_log()

    def _sort_addresses(self):
        self._addresses_list = sorted(self._addresses_list)

    def _extract_addresses_from_log(self, log_path):
        try:
            with open(log_path, "r", encoding="UTF_8") as log:
                for line in log:
                    match = find_address("'(.*)'", line)
                    self._logged_addresses.append(match.group(1))
        except FileNotFoundError:
            print("File not found, please try again.")

    def _find_addresses_not_used_in_log(self):
        self._addresses_not_used_in_logs = [
            address
            for address in self._addresses_list
            if address not in self._logged_addresses
        ]

    def print_results(self):
        print(f"Emails not sent ({len(self._addresses_not_used_in_logs)}):")
        for address in self._addresses_not_used_in_logs:
            print(f"    {address}")
