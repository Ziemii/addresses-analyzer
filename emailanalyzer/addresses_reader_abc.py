from abc import ABCMeta, abstractmethod
from os import listdir as list_directory_items
from csv import DictReader
from emailanalyzer.address_validator import is_address_valid


class AddressesReaderABC(metaclass=ABCMeta):
    """Provides addresses reading functionality for more specialized children."""

    _addresses_list = []

    @abstractmethod
    def __init__(self, mails_directory):
        self.mails_directory = mails_directory
        try:
            self._read_addresses_from_directory()
        except FileNotFoundError:
            print("Emails location invalid, please try again.")

    def _read_addresses_from_directory(self):
        files_in_directory_list = list_directory_items(self.mails_directory)
        for file_name in files_in_directory_list:
            if file_name.endswith(".txt"):
                self._read_addresses_from_text_file(file_name)
            if file_name.endswith(".csv"):
                self._read_addresses_from_csv_file(file_name)

    def _read_addresses_from_text_file(self, file_name):
        with open(
            self.mails_directory + "/" + file_name, "r", encoding="UTF_8"
        ) as txtfile:
            self._addresses_list += [line.rstrip("\n") for line in txtfile]
          
    def _read_addresses_from_csv_file(self, file_name):
        with open(
            self.mails_directory + "/" + file_name, newline="", encoding="UTF_8"
        ) as csvfile:
            reader = DictReader(csvfile, delimiter=";")
            self._addresses_list += [row["email"] for row in reader]

    def _remove_invalid_addresses(self):
        valid_addresses_list = [
            address
            for address in self._addresses_list
            if is_address_valid(address)
        ]
        self._addresses_list = valid_addresses_list

    def _remove_duplicates(self):
        self._addresses_list = list(set(self._addresses_list))
