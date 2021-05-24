# This is an example of a basic encryption code using RSA algoritms
#This code only contins encryption code, decryption code is in a different file
import random
import os

def get_key():

    try:
        n = int(input('\n insert FIRST public key code: '))
        e = int(input('\n insert SECOND public key code:'))
    except:
        print('someting was wrong :/ please verify both codes are only numbers without dots, letters or symbols')
        n, e = get_key()

    return n, e

#_____________________________________________________________________________________________________________________________________________________

# This function is for transform the encrypted list in a string message
def list_to_string(code_list):

    #this list is for use as separators (just for a improve visualy the encrypted word)
    separator_list = ['a','A','b','B','c','C','d','D','>','<',':','*','-','+','%','@','&',';']

    encrypted_message = ''
    for code in code_list:
        rand_sep = random.sample(separator_list, 1)
        encrypted_message = encrypted_message + ''.join(rand_sep) + str(code)

    return encrypted_message

#_____________________________________________________________________________________________________________________________________________________
def Encryp(n, e):

    letters_code = {'z': 1, 'y': 2, 'x': 3, 'w': 4, 'v': 5, 'u': 6, 't': 7, 's': 8, 'r': 9, 'q': 10, 'p': 11, 'o': 12, 'ñ': 13, 'n': 14,
                    'm': 15, 'l': 16, 'k': 17, 'j': 18, 'i': 19, 'h': 20, 'g': 21, 'f': 22, 'e': 23, 'd': 24, 'c': 25, 'b': 26, 'a': 27, ' ':28}

    message = input('insert the text to encrypt: ').lower()

    letters = list(message)

    first_code = []
    for letter in letters:

        encrypt_letter =  (letters_code[letter]**e) % n
        first_code.append(encrypt_letter)

    return first_code


#_____________________________________________________________________________________________________________________________________________________
if __name__=='__main__':

    print('RSA ENCRYPTION CODE \n')
    print('The public key is composed of two integer codes, insert these two codes \n')

    n, e = get_key()
    encrypted_code = Encryp(n,e)

    #visual improvement in text format
    final_message = list_to_string(encrypted_code)
    print(final_message)
    os.system('pause')