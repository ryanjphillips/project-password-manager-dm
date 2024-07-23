import random

class PasswordManager:
    def __init__(self):
        
        self.password = None
        self.requirements = {'min_length': 1, 'max_length': 24, 'special_char_allowed': False, 'duplicate_char_allowed': True, 'lowercase_required': False, 'uppercase_required': False, 'number_required': False, 'special_char_required': False}
        self.shortcut_key = None
        self.shortcut_key_length = 0

    def configure_requirements(self):
        self.requirements['min_length'] = input("Please enter the minimum password length (inclusive): ")
        self.requirements['max_length'] = input("Please enter the maximum password length (inclusive): ")

        self.requirements['special_char_allowed'] = True if input("Are special characters (!@#$%^&*) allowed? (y/n): ") == "y" else False
        self.requirements['duplicate_char_allowed'] = True if input("Are duplicate characters allowed? (y/n): ") == "y" else False

        self.requirements['lowercase_required'] = True if input("Is a lowercase letter (a-z) required? (y/n): ") == "y" else False
        self.requirements['uppercase_required'] = True if input("Is an uppercase letter (A-Z) required? (y/n): ") == "y" else False
        self.requirements['number_required'] = True if input("Is a number (0-9) required? (y/n): ") == "y" else False

    def new_shortcut_key(self):
        self.shortcut_key = []
        self.shortcut_key_length = 0
        valid_chars = self.valid_characters()
        print("\nA shortcut key consists of one or more combo-presses\n"
              "A combo-press involves hitting 5 keys simultaneously\n")
        ans = "y"
        while(ans == "y"):
            valid_input = True
            combo_keys = set()
            while(len(combo_keys) != 5):
                combo_keys = set(input("Enter 5 keys (no spaces or commas): "))

            for c in combo_keys:
                if c not in valid_chars:
                    valid_input = False
                    print("Invalid character: ",c)
            if valid_input:
                self.shortcut_key.append(combo_keys)
                self.shortcut_key_length += 1
                ans = ""
                while(ans != "y" and ans != "n"):
                    ans = input("Would you like to add another combo-press? (y/n): ")                

    """
    Purpose: to check what characters are allowed in the password, given self.requirements
    Returns: a list of characters
    Outputs: nothing
    Pre-conditions: none
    Post-conditions: none
    """
    def valid_characters(self):
        valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        if self.requirements['special_char_allowed']:
            valid_chars += "!@#$%^&*"
        return list(valid_chars)

    """
    Purpose: to compute the likelihood of randomly guessing the current password
    Returns: nothing
    Outputs: a message is displayed to the user containing:
                - the number of possible valid passwords given self.requirements
                - the probability of a uniform random guess matching the current password
    Pre-conditions: self.password != None
    Post-conditions: none
    """
    def password_strength(self):

        # Pre-condition to check the existence of the password. Sort've redundant, but just in case.

        if (self.password == None):
          print("\nYou do not have a password set")
          return

    """
    Purpose: to generate a new valid password
    Returns: nothing
    Outputs: nothing
    Pre-conditions: none
    Post-conditions: self.password contains a new, randomly generated password that follows self.requirements
    """
    def new_random_password(self):

        # List of Valid Characters and Numbers
        number_list = ['0','1','2','3','4','5','6','7','8','9']
        lowerCase_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        upperCase_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        special_list= ['!','@', '#', '$', '%', '^', '&','*']

        # Final List
        new_password = []

        # Generate Random Length Between the Min and Max
        randomLength = random.randint(int(self.requirements['min_length']), int(self.requirements['max_length']))

        # Number of requirements added
        added = 0

        # Ensure that there is the requirements are in the password
        if self.requirements['uppercase_required'] and added <= randomLength:
          randomItem = random.choice(upperCase_list)
          new_password.append(randomItem)
          added += 1

          if not self.requirements['duplicate_char_allowed']:
            upperCase_list.remove(randomItem) 

        if self.requirements['lowercase_required'] and added <= randomLength:
          randomItem = random.choice(lowerCase_list)
          new_password.append(randomItem)
          added += 1

          if not self.requirements['duplicate_char_allowed']:
            lowerCase_list.remove(randomItem) 

        if self.requirements['number_required'] and added <= randomLength:
          randomItem = random.choice(number_list)
          new_password.append(randomItem)
          added += 1

          if not self.requirements['duplicate_char_allowed']:
            number_list.remove(randomItem) 

        # Subtract any that were added
        print ("Random Length: " + str(randomLength))
        randomLength = randomLength - added

        # Define new sets
        newSet = number_list + lowerCase_list + upperCase_list
        newSetWithSpecial = number_list + lowerCase_list + upperCase_list + special_list

        i = 0
        # Loop to length of min and max of new password
        print ("Added Length: " + str(added))
        print ("Difference " + str(randomLength))

        # There is a maximum based on the amount of passwords that can be generated.
        while i < randomLength:
          if len(newSet) <= 0 or len(newSetWithSpecial) <= 0:
            print('Without Duplicates the max password is 70. If you want longer please consider allowing duplicates.')

            # Exit Loop
            i = randomLength


          elif self.requirements['special_char_allowed']:
            randomItem = random.choice(newSetWithSpecial)
            new_password.append(randomItem)

            if not self.requirements['duplicate_char_allowed']:
              newSetWithSpecial.remove(randomItem) 

          else:

            # I am supposing that A and a are different characters are not duplicates.

            randomItem = random.choice(newSet)
            new_password.append(randomItem)
            if not self.requirements['duplicate_char_allowed']:
              newSet.remove(randomItem) 

          # Increment Loop
          i = i + 1

        # List to string
        self.password = "".join(new_password)
        
        # Delete Later
        print(self.password)
        print(len(self.password))

    """
    Purpose: to compute the likelihood of randomly guessing a scrambled password. Helper to scramble_password()
    Returns: an integer, the number of distinct permutations (scrambles) of self.password
    Outputs: nothing
    Pre-conditions: self.password != None
    Post-conditions: none
    """
    def scramble_strength(self):
        pass

    """
    Purpose: to re-arrange the characters of the existing password
    Returns: nothing
    Outputs: message is displayed to the user containing:
                - the number of valid scrambles of their password
                - the probability of guessing the scramble if the old password is known
                - asking the user to confirm that they'd like to scramble their password
    Pre-conditions: self.password != None
    Post-conditions: self.password changed if user confirms, otherwise nothing happens
    """
    def scramble_password(self):

        # Check for an unset pass
        if self.password == None:
            print("\nYou do not have a password set")
            return

        # Length of Password
        length = len(self.password)
        lenFactorial = self.calc_factorial(length)

        # Number of valid scrambles, supposing no duplicates.
        if not self.requirements['duplicate_char_allowed']:
          print("Number of possible scrambles, without duplicates" + str(lenFactorial))
          prob = (1.0/float(lenFactorial)) * 100
          print("Probability of guessing the old password: " + str(prob) + " %") 

        # Different Forumula with duplicates n! / n!...k!
        else:
          duplicateDict = self.calc_duplicates()
          bottomFinal = 1

          for char, count in duplicateDict.items():
            bottomFinal *= self.calc_factorial(count)

            
          finalCalc = lenFactorial / bottomFinal
          formatted_number = f"{finalCalc:.0f}"
          print("Number of possible scrambles, with duplicates: " + str(formatted_number))
          prob = (1.0/float(formatted_number)) * 100
          print("Probability of guessing the old password: " + str(prob) + " %") 

        # Ask if the user wants to scramble the password.
        passwordList = list(self.password)
        random.shuffle(passwordList) if input("Shuffle the password. (y/n)") == "y" else print("Declined Shuffle")
        self.password = "".join(passwordList)
        print(self.password)

    def calc_factorial(self, size):
        finalnumber = 1
        for i in range(size, 0, -1):
          finalnumber *= i
        return finalnumber 

    def calc_duplicates(self):
        sorted_string = ''.join(sorted(self.password))

        counts = {}
        for char in sorted_string:
            if char in counts:
                counts[char] += 1
            else:
              counts[char] = 1
        return counts

    """
    Purpose: to compute the likelihood of randomly guessing the current shortcut key
    Returns: nothing
    Outputs: a message is displayed to the user containing:
                - the number of possible valid shortcut keys with self.shortcut_key_length combo-presses
                    - note: duplicate_char_allowed, lowercase_required, uppercase_required, and number_required DO NOT apply to the shortcut key
                    - special_char_allowed DOES apply to the shortcut key
                - the probability of a uniform random guess matching the current shortcut key
                    - note: assume that the guess has the correct length
    Pre-conditions: none
    Post-conditions: none
    """
    def shortcut_key_strength(self):
        pass
    def session(self):
        if self.password == None:
            print("\nYou do not have a password set")
            self.configure_requirements()
            print("Generating random password")
            self.new_random_password()
        if self.shortcut_key == None:
            ans = ""
            while (ans != "y" and ans != "n"):
                ans = input("You do not have a shortcut key, would you like to make one? (y/n): ")
            if ans == "y":
                self.new_shortcut_key()
                
        print("Your password is ", self.password, ". What would you like to do?")
        print("1) change password\n"
              "2) change shortcut key\n"
              "3) scramble password\n"
              "4) check password strength\n"
              "5) check shortcut key strength\n"
              "6) configure password requirements\n"
              "*) exit\n")
        option = input("Type 1-6 to proceed or anything else to exit: ")


        if option == "1":
            self.new_random_password()
        elif option == "2":
            self.new_shortcut_key()
        elif option == "3":
            self.scramble_password()
        elif option == "4":
            self.password_strength()
        elif option == "5":
            self.shortcut_key_strength()
        elif option == "6":
            self.configure_requirements()
        else:
            return

        self.session()
        

if __name__ == "__main__":
    pm = PasswordManager()
    pm.session()
