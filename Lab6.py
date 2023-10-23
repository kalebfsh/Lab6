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
            print("Your password has been encoded and stored!\n")

        if menu_option == '3':
            break