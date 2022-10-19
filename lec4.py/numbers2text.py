# numbers2text.py
#     A program to convert a sequence of Unicode numbers into 
#         a string of text.

def main():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents.\n")

    # Get the message to encode
    in_string = input("Please enter the Unicode-encoded message: ")

    # Loop through each substring and build unicode message
    message = ""
    for num_str in in_string.split():
        # convert the (sub)string to a number
        code_num = int(numstr)
        # append character to message
        message = message + chr(code_num)

    print("\nThe decoded message is:", message)
