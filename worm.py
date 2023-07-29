from malware import *
from checkings import*


class Worm(Malware):
    """
    Class that represents a computer worm
    """
    def __init__(self, program_name: str, unique_signature: str, previous_host: str):
        """
        Constructor that sets worm's fields
        :param program_name: name of program of a string type
        :param unique_signature: program unique signature of string type
        :param previous_host: string that represents ipv4 address of previous infected computer
        :raises ValueError - if one of passed arguments has not valid format
        :raises TypeError - if one of passed arguments has not valid type
        """
        super().__init__(program_name, unique_signature)
        self.previous_host = previous_host

    def __str__(self) -> str:
        """
        String represents all computer worm's attributes in a format that is convenient for the user
        :return: string that contains worm's attributes
        """
        return f"{super().__str__()}, previous infected computed address is {self.previous_host}"

    @property
    def previous_host(self) -> str:
        """
        Getter that returns the worm's previous infected host ipv4 address
        :return: string that represents previous infected host ipv4 address
        """
        return self.__previous_host

    @previous_host.setter
    def previous_host(self, previous_host: str) -> None:
        """
        Setter that sets previous infected host ipv4 address
        :param previous_host: string that contains ipv4 address
        :raises ValueError - if the given IPv4 address doesn't have a valid format
        :return: None
        """
        if not Checkings.check_if_ip_octets_are_valid(previous_host):
            raise ValueError("The ip address is invalid")
        self.__previous_host = previous_host

    def address_class(self) -> None:
        """
        Function that checks and print to what class belongs the previous infected host ipv4 address
        :raises ValueError - if the given IPv4 address doesn't have a valid format
        :return: None
        """

        num_of_octet = 0
        according_to_sign = "."

        # Get the first octet
        octet = int(self.previous_host.split(according_to_sign)[num_of_octet])

        # List that represents all classes with their ranges
        ip_classes = {"A": [1, 126],
                      "B": [128, 191],
                      "C": [192, 223]}

        for class_name, class_info in ip_classes.items():
            if octet in range(class_info[0], class_info[1] + 1):
                print(f"The previous infected host ip belongs to class {class_name} ")
                break
        else:
            raise ValueError("IP address is invalid")


