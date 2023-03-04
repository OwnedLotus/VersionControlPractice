#caesar cipher shift left 3
codex = '3456789012'

def encode(_input_string):
     #super secret encoding strategy
     _return_list = []
     for char in _input_string:
          _return_list.append(codex.index(char))
          
     return _return_list

def decode():
     #TODO
     pass

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