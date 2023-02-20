import os
os.system('cls')
import random

def options():
  options= ('piedra','papel', 'tijera')
  user_option= input('Piedra,papel o tijera: ')
  user_option=user_option.lower()
  if not user_option in options:
    print('opcion inválida. Se anula este round')
    return None, None
  computer_option=random.choice(options)
  print('PC elige: ', computer_option)
  return user_option, computer_option

def rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('user gano!')
      user_wins += 1
    else:
      print('Papel gana a piedra')
      print('computer gano!')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user gano')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('computer gano!')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user gano!')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('computer gano!')
      computer_wins += 1
  return user_wins, computer_wins

def winner(user_wins,computer_wins):
  if computer_wins==2:
    print('Gana la PC. Mejor suerte para la próxima')
    exit()
  if user_wins==2:
    print('gana el usuario, felicidades')
    exit()

def game():
  computer_wins=0
  user_wins=0
  rounds=1
  print('Comienza el juego')
  while True:
    print('*'*10)
    print('ROUND', rounds)
    print('*'*10)
    print('computer: ', computer_wins)
    print('User: ', user_wins)
    rounds+=1

    user_option, computer_option =options()
    user_wins, computer_wins = rules(user_option,computer_option,user_wins,computer_wins)
    winner(user_wins,computer_wins)

if __name__== "__main__":
  game()
  


 
    

  

