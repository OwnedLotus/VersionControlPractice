#Jonah Ringdahl
#caesar cipher shift left 3
codex = '3456789012'

def encode(_input_string):
     #super secret encoding strategy
     _return_str = ''
     for char in _input_string:
          _return_str += str(codex.index(char))
          
     return _return_str

def decode():
     enc_string = ''
     password = str(password)
     for num in password:
        num = int(num)
        password = int(password)
        if num >= 3:
            enc_num = (num - 3)
            enc_num = str(enc_num)
            enc_string += enc_num
        else:
            enc_num = ((num + 10) - 3) # For numbers that would be negative
            enc_num = str(enc_num)
            enc_string += enc_num
     return enc_string

def menu():
     _valid_input = False
     
     while not( _valid_input):
          print()
          print('Menu')
          print('-------------')
          print('1. Encode')
          print('2. Decode')
          print('3. Quit')
          print()
          
          _selection = input('Please enter an option: ')

          try:
               _input = int(_selection)
               _valid_input = True
          except:
               print('Failed to parse input')
               _valid_input = False
               
          if 1 <= _input <= 3:
               return _input
          else:
               print('Invalid Input')


def main ():
     password_buff = []
     
     while True:
          selection = menu()
          
          if selection == 1:
               _secret_string = input('Please enter your password to encode: ')
               password_buff = encode(_secret_string)
               print('Your password has been encoded and stored!')
          elif selection == 2:
               decode()
          elif selection == 3:
               quit()
          else:
               print('Unknown returned information')

if __name__ == '__main__':
     main()
