from worm import *

if __name__ == "__main__":

    def main() -> None:
        """
        Main function creates an empty worm_list and gets from the user number of worms
        that should be created and appended to this list.
        After the creating and adding the worms to the list function prints every worm's information
        and a previous host address

        """
        worm_list = []

        # Get number of worms that will be created
        num_of_worms = int(input("Enter number of worms: "))

        # Add specified num_of_worms to worm_list
        for worm in range(num_of_worms):
            # Enter single worm data
            worm_name = input("Enter worm name: ")
            unique_signature = input("Enter unique signature: ")
            previous_host = input("Enter previous host IPv4: ")

            # Create a worm with specified data
            worm = Worm(worm_name, unique_signature, previous_host)
            # Append created worm to the list
            worm_list.append(worm)

        # Print every worm data and IP class of previous worm host
        for worm in worm_list:
            # Print data about a worm in a convenient for user format
            print(worm)
            # Print data about previous hosts class
            worm.address_class()


    # try-except block that calls main function
    try:

        main()
    # if ValueError appears raise ValueError exception
    except ValueError as v:
        print(v)
    # if TypeError appears raise TypeError exception
    except TypeError as t:
        print(t)
