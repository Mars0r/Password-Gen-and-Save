import random
import os
import csv
import base64
from time import sleep




def menu():
  print('1 --> Generate password')
  print('2 --> Search password')
  print('3 --> Salir')
  option = input('Opción: ')
  if option == '1':
    generate()

  elif option == '2':
    search()

  elif option == '3':
    exit()

  else:
    os.system('clear')
    menu()


def generate():
  
  lines = ''
  password = ''
  
  length = input('How long sould the password be? (Deafault: between 12 and 20): ')
  service = input('Which service is this password for? (Can be empty): ')

  if length == '':
    length = random.randint(12, 20)
    print(f'Length default: {length}')

  else: 
    length = int(length)

  #Main program starts here
  for i in range(length):
    lines += '*'
    password += chr(random.randint(33,126)) 

  #Save password in a csv file
  with open('passwords.csv', 'a') as f_object:
    save = [base64.b64encode(password.encode("utf-32")), service]
    # You will get a object of DictWriter
    writer_object = csv.writer(f_object)

    #Pass the dictionary as an argument to the Writerow()
    writer_object.writerow(save)

    #Close the file object
    f_object.close()

  #Ouput
  print(lines)
  print(password)
  print(f'{lines}\n\n')

  sleep(2)
  menu()



def search():
  with open('passwords.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 1
    for row in csv_reader:
        print('')
        print(f'{line_count} --> {row[1]} password')
        line_count += 1
    csv_file.close()

  acount = int(input('Seleccione la cuenta de la cual quiere al contraseña: '))

  with open('passwords.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')     
    line_count = 0
    
    for row in csv_reader:
      line_count += 1
    
      if line_count == acount:
        hasht = (row[0]).replace("'", '')
        hasht = hasht[1:]
        a = bytes(hasht, 'utf-32')
        decod = base64.b64decode(a).decode('utf-32')
    
    csv_file.close()

  print('------------------------')
  print(decod)
  print(f'_______________________\n\n')

  sleep(2)
  menu()


menu()  
