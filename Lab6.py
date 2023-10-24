# Kaleb Colon

def encode(encode_input):
    res = [int(i) for i in encode_input]
    encoded = ''
    for i in res:
        if i == 7:
            i = -3
        elif i == 8:
            i = -2
        elif i == 9:
            i = -1
        num = i + 3
        encoded += str(num)
    return int(encoded)


def decode_password(encoded_password):
    original_password = ""
    for digit in encoded_password:
        if digit.isdigit():
            original_digit = (int(digit) - 3) % 10
            original_password += str(original_digit)

    return original_password


def print_menu():
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")


if __name__ == '__main__':
    while True:
        print_menu()
        menu_option = input("Please enter an option: ")
        if menu_option == '1':
            encode_input = input("Please enter your password to encode: ")
            encoded_password = encode(encode_input)
            print("Your password has been encoded and stored!\n")
        elif menu_option == '2':
            original_password = decode_password(str(encode(encode_input)))
            print(f"The encoded password is {encoded_password}, and the original password is {original_password}.")
        elif menu_option == '3':
            break
