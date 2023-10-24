encrypted_message = input()

command = input()

encrypted_message_list = [letter for letter in encrypted_message]

while command != "Decode":
    command_list = command.split("|")
    action = command_list[0]

    if action == "Move":
        number_of_letters = int(command_list[1])
        encrypted_message_list.extend(encrypted_message_list[0:number_of_letters])
        del encrypted_message_list[0:number_of_letters]

    elif action == "Insert":
        index = int(command_list[1])
        value = command_list[2]
        encrypted_message_list.insert(index, value)

    elif action == "ChangeAll":
        substring = command_list[1]
        replacement = command_list[2]
        for index, letter in enumerate(encrypted_message_list):
            if letter == substring:
                encrypted_message_list[index] = replacement

    command = input()

encrypted_message = "".join(encrypted_message_list)
print(f"The decrypted message is: {encrypted_message}")