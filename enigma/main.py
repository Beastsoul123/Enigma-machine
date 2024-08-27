class Rotor:
    def __init__(self,wiring,position):
        self.wiring=wiring
        self.position=position
    def encrypt(self,char):
        rotated_wiring=self.wiring[self.position:]+self.wiring[:self.position]
        encrypted_char=rotated_wiring[ord(char)-65]
        return encrypted_char

class Reflector:
    def __init__(self,wiring):
        self.wiring=wiring
    def reflect(self,char):
        return self.wiring[ord(char)-65]
class Plugboard:
    def __init__(self,wiring):
        self.wiring=wiring

    def swap(self,char):
        return self.wiring.get(char,char)
class Enigma:
    def __init__(self,rotors,reflector,plugboard):
        self.rotors=rotors
        self.reflector=reflector
        self.plugboard=plugboard
    def encrypt(self,message):
        encrypted_message=""
        for char in message:
            char = self.plugboard.swap(char)
            for rotor in self.rotors:
                char = rotor.encrypt(char)
            char = self.reflector.reflect(char)
            for rotor in reversed(self.rotors):
                char = rotor.encrypt(char)
            char =self.plugboard.swap(char)
            encrypted_message += char
        return encrypted_message
rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 0)
rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", 0)
rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", 0)
reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
plugboard = Plugboard({"A": "J", "B": "G", "C": "D", "D": "C", "E": "K", "F": "P", "G": "B", "H": "X", "I": "F", "J": "A", "K": "E", "L": "R", "M": "T", "N": "H", "O": "L", "P": "F", "Q": "S", "R": "L", "S": "Q", "T": "M", "U": "W", "V": "N", "W": "U", "X": "H", "Y": "Z", "Z": "Y"})
enigma_machine = Enigma([rotor1, rotor2, rotor3], reflector, plugboard)
message = input("Enter a message to encrypt: ")
message = message.upper()
encrypted_message = enigma_machine.encrypt(message)
print(f"Encrypted message: {encrypted_message}")
