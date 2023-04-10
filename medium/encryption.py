# https://www.hackerrank.com/challenges/encryption/problem?isFullScreen=true

import math


def encryption(message):
    def get_num_of_rows_cols(stripped_message):
        sqrt_len_message = math.sqrt(len(stripped_message))
        num_rows = math.floor(sqrt_len_message)
        num_cols = math.ceil(sqrt_len_message)

        return num_rows, num_cols


    def create_message_matrix(stripped_message, rows, cols):
        message_matrix = []

        i = 0
        while i < rows:
            current_row = list(stripped_message[(i*cols):((i+1)*cols)])
            message_matrix.append(current_row)
            i += 1

        return message_matrix


    def encrypt_message_matrix(message_matrix, cols):
        encrypted_matrix = []

        i = 0
        while i < cols:
            encrypted_row = []

            for row in message_matrix:
                if i < len(row):
                    encrypted_row.append(row[i])

            encrypted_matrix.append(encrypted_row)
            i += 1

        return encrypted_matrix


    stripped_message = list("".join(message.split()))

    rows, cols = get_num_of_rows_cols(stripped_message)

    message_matrix = create_message_matrix(stripped_message, rows, cols)

    encrypted_matrix = encrypt_message_matrix(message_matrix, cols)

    encrypted_message = " ".join(list(map(lambda x: "".join(x), encrypted_matrix)))
    
    return encrypted_message


text1 = """\
if man was meant to stay on the ground god would have given us roots
"""

text2 = """\
Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua.
"""

text3 = "haveaniceday"

print(encryption(text1))
print(encryption(text2))
print(encryption(text3))