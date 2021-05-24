# This is an example of a basic encryption code using RSA algoritms
#This code only contins encryption code, decryption code is in a different file

def get_key():

    try:
        n = int(input('\n insert FIRST public key code: '))
        p = int(input('\n insert SECOND public key code:'))
    except:
        print('someting was wrong :/ please verify both codes are only numbers without dots, letters or symbols')
        n, p = get_key()

    return n, p


if __name__=='__main__':

    print('RSA ENCRYPTION CODE \n')
    print('The public key is composed of two integer codes, insert these two codes \n')

    n, p = get_key()
    print('n= {}, p= {}'.format(n,p))
