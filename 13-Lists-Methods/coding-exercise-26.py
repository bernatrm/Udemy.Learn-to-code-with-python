# Define an encrypt_message function that accepts a string.
# The input string will consist of only alphabetic characters.
# The function should return a string where all characters have been moved
# "up" two spots in the alphabet. For example, "a" will become "c".
#
# EXAMPLES
# encrypt_message("abc") => "cde"
# encrypt_message("xyz") => "zab"
# encrypt_message("")    => ""
def encrypt_message(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_max_index = len(alphabet)
    encrypted_message = ""
    for letter in message:
        index = alphabet.index(letter) + 2
        if index >= alphabet_max_index:
            index -= alphabet_max_index
        encrypted_message += alphabet[index]
    return encrypted_message

print(encrypt_message("abc") == "cde")
print(encrypt_message("xyz") == "zab")
print(encrypt_message("") == "")

def encrypt_message_solution(message):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_max_index = len(alphabet)
    encrypted_message = ""
    for letter in message:
        encrypted_message += alphabet[(alphabet.index(letter) + 2) % alphabet_max_index]
    return encrypted_message

print(encrypt_message_solution("abc") == "cde")
print(encrypt_message_solution("xyz") == "zab")
print(encrypt_message_solution("") == "")