"""
Calculator app
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
class Calculator:
    def __init__(self):
        self.last_result = 0

    def get_hello_message(self):
        """ Show welcome message """
        return "== Calculatrice v1.0 =="

    def addition(self, v1, v2):
        """ Add 2 values """
        self.last_result = v1 + v2
        return self.last_result

    def subtraction(self, v1, v2):
        """ Subtract 2 values """
        self.last_result = v1 - v2
        return self.last_result

    def multiplication(self, v1, v2):
        """ Multiply 2 values. """
        self.last_result = v1 * v2
        return self.last_result

    def division(self, v1, v2):
        """ Divide 2 values. Show an error if V2 is zero. """
        if (v2 != 0):
            self.last_result = v1 / v2
            return self.last_result
        else:
            self.last_result = "Error"
            return "Erreur : division par zéro"

if __name__ == "__main__":
    is_running = 1
    my_calculator = Calculator()
    message = my_calculator.get_hello_message()
    print(message)

    while is_running == 1:
        print("Operation : additionner deux valeurs")
        val_x = input("Saisissez la valeur 1 : ")
        val_y = input("Saisissez la valeur 2 : ")
        my_calculator.addition(int(val_x), int(val_y))
        print('V1 + V2 =', my_calculator.last_result)
        is_running = int(input("Voulez-vous faire une autre addition ? [1 = Oui | 2 = Non] : "))

    print("Au revoir :)")
    print("test")