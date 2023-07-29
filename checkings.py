class Checkings():

    # check for Malware
    @staticmethod
    def check_str_length(str_to_check: str, max_len: int) -> bool:
        """
        Function that gets as parameters a string and a number,
        checks if string's length is less than a given number
        :param str_to_check: string to check its length
        :param max_len: max length of a string we want to check
        :return: True if a string's length is less than a passed value,
        otherwise returns False
        """
        return len(str_to_check) < max_len

    @staticmethod
    def check_type(value, expected_type) -> bool:
        """
        Function checks if the given value is of the expected type
        :param value: The value to check
        :param expected_type: The expected type
        :return: True if a string's type if of the expected type,
        otherwise returns False
        """
        return isinstance(value, expected_type)

    @staticmethod
    def check_length_and_chars(signature: str, str_len: int, possible_values: str):
        """
        Function gets as parameters string to check, integer that represents length to check
        and string that represents possible values that may contain that string
        :param signature: string to check its length and letters it contains
        :param possible_values: string of possible value that are allowed for the right string to contain
        :param str_len: length that is allowed for the string that we check
        :return: True if string is of the checked length and contains only allowed chars, otherwise False
            """
        # Check if signature equal to the demanded length
        if len(signature) == str_len:
            for letter in signature:
                # Check if current letter is presented in allowed letters string
                if letter not in possible_values:
                    return False
            return True
        return False

    # ip checkings
    @staticmethod
    def split_octets_into_list_of_numbers(ipv: str) -> list:
        """
        Function gets a string that represents an ipv address and splits it into segments
        Than function returns list of segments that were converted from string values into int values
        :param ipv: string that represents ip address
        :return: list of numbers
        """
        list_of_str = ipv.split(".")

        # Convert octet values to int and set them into a list
        list_res = [int(num) for num in list_of_str if num.isdigit()]
        return list_res

    @staticmethod
    def check_if_ip_octets_are_valid(ipv: str) -> bool:
        """
        Function ensures that the given IP address has the correct format and values for each octet, not returns false.
        :param ipv: string that represent IPv4 that we check
        :return: True if a passed IPv4 address is valid, otherwise returns false
        """

        min_octet_number = 0
        max_octet_numer = 255
        first_octet_exception = [0, 127, 224]
        min_list_length = 4

        # Split the IP string into list of numbers
        octets_list = Checkings().split_octets_into_list_of_numbers(ipv)

        # First check if list contain 4 numbers
        if not len(octets_list) == min_list_length:
            return False

        for i, num in enumerate(octets_list):
            # check of 2-4 octet values
            if not type(num) == int or num < min_octet_number or num > max_octet_numer:
                return False
            # check of first octet exceptions
            if i == 0 and num in first_octet_exception or num > first_octet_exception[2]:
                return False
        return True
