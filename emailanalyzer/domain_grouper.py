from emailanalyzer.addresses_reader_abc import AddressesReaderABC
from emailanalyzer.results_printer_abc import ResultsPrinterABC


class DomainGrouper(AddressesReaderABC, ResultsPrinterABC):
    """Groups and sorts addresses by domain."""

    def __init__(self, mails_directory):
        super(DomainGrouper, self).__init__(mails_directory)
        self._domains = {}
        self._remove_duplicates()
        self._remove_invalid_addresses()
        self._group_valid_addresses_by_domain()
        self._sort_domains()

    def _group_valid_addresses_by_domain(self):
        for address in self._addresses_list:
            self._add_address_to_domains(address)

    def _add_address_to_domains(self, address):
        address_domain = address.split(sep="@")[1]
        if address_domain in self._domains.keys():
            self._domains[address_domain].append(address)
        else:
            self._domains[address_domain] = [address]

    def _sort_domains(self):
        sorted_domains_keys = sorted(self._domains)
        sorted_domains_dict = {}

        for domain in sorted_domains_keys:
            sorted_domains_dict[domain] = sorted(self._domains[domain])

        self._domains = sorted_domains_dict

    def print_results(self):
        for domain in self._domains:
            print(f"Domain {domain} ({len(self._domains[domain])}):")
            for address in self._domains[domain]:
                print(f"    {address}")
