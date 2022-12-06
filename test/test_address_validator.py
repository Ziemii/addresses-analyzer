import unittest
from emailanalyzer.address_validator import is_address_valid


class AddressValidatorTests(unittest.TestCase):

    correct_addresses = [
        "email@email.com",
        "lukasz.ziemacki@gmail.com",
        "rhodkiewicz@onet.net",
        "address.s@wo.net",
    ]

    incorrect_addresses = [
        "mail@com",
        "asd@o.o",
        "@mail.com",
        "@",
        "at@.com",
        "bubu.com",
    ]

    def test_address_validation_on_correct(self):
        for correct_address in self.correct_addresses:
            self.assertTrue(
                is_address_valid(correct_address),
                f"Marked {correct_address} as invalid.",
            )

    def test_address_validation_on_incorrect(self):
        for incorrect_address in self.incorrect_addresses:
            self.assertFalse(
                is_address_valid(incorrect_address),
                f"Marked {incorrect_address} as valid.",
            )


if __name__ == "__main__":
    unittest.main()
