import random
import os 
import pyperclip
from datetime import date

today = date.today()
from datetime import datetime
now = datetime.now()

current_time = now.strftime("%H:%M:%S")


def message(title, message):
    os.system('notify-send "'+title+'" "'+message+'"')
#list for words mixed with numbers to create passoword
random_mixed1 = ['a', '1', 'b', '2', 'c', '3', 'd', '4', 'e', '5', 'f', '6', 'g', '7', 'h', '8', 'i', '9', 'j', '0', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_mixed2 = ['a', '1', 'b', '2', 'c', '3', 'd', '4', 'e', '5', 'f', '6', 'g', '7', 'h', '8', 'i', '9', 'j', '0', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_mixed3 = ['a', '1', 'b', '2', 'c', '3', 'd', '4', 'e', '5', 'f', '6', 'g', '7', 'h', '8', 'i', '9', 'j', '0', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_mixed4 = ['a', '1', 'b', '2', 'c', '3', 'd', '4', 'e', '5', 'f', '6', 'g', '7', 'h', '8', 'i', '9', 'j', '0', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_mixed5 = ['a', '1', 'b', '2', 'c', '3', 'd', '4', 'e', '5', 'f', '6', 'g', '7', 'h', '8', 'i', '9', 'j', '0', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_mixed6 = ['a', '1', 'b', '2', 'c', '3', 'd', '4', 'e', '5', 'f', '6', 'g', '7', 'h', '8', 'i', '9', 'j', '0', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_mixed7 = ['a', '1', 'b', '2', 'c', '3', 'd', '4', 'e', '5', 'f', '6', 'g', '7', 'h', '8', 'i', '9', 'j', '0', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_mixed8 = ['a', '1', 'b', '2', 'c', '3', 'd', '4', 'e', '5', 'f', '6', 'g', '7', 'h', '8', 'i', '9', 'j', '0', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_mixed9 = ['a', '1', 'b', '2', 'c', '3', 'd', '4', 'e', '5', 'f', '6', 'g', '7', 'h', '8', 'i', '9', 'j', '0', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_mixed10 =['a', '1', 'b', '2', 'c', '3', 'd', '4', 'e', '5', 'f', '6', 'g', '7', 'h', '8', 'i', '9', 'j', '0', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#creating random choices for mixed method
computer_random = random.choice(random_mixed1)
computer_random1 = random.choice(random_mixed2)
computer_random2 = random.choice(random_mixed3)
computer_random3 = random.choice(random_mixed4)
computer_random4 = random.choice(random_mixed5)
computer_random5 = random.choice(random_mixed6)
computer_random6 = random.choice(random_mixed7)
computer_random7 = random.choice(random_mixed8)
computer_random8 = random.choice(random_mixed9)
computer_random9 = random.choice(random_mixed10)
#here comes the list for random words
random_words1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_words2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_words3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_words4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_words5 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_words6 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_words7 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_words8 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_words9 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_words10 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#random choices for only words option
computer_word1 = random.choice(random_words1)
computer_word2 = random.choice(random_words2)
computer_word3 = random.choice(random_words3)
computer_word4 = random.choice(random_words4)
computer_word5 = random.choice(random_words5)
computer_word6 = random.choice(random_words6)
computer_word7 = random.choice(random_words7)
computer_word8 = random.choice(random_words8)
computer_word9 = random.choice(random_words9)
computer_word10 = random.choice(random_words10)
# here comes the list for random numbers
random_numbers1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
random_numbers2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
random_numbers3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
random_numbers4 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
random_numbers5 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
random_numbers6 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
random_numbers7 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
random_numbers8 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
random_numbers9 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
random_numbers10 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# creating random choices for random numbers
computer_numbers = random.choice(random_mixed1)
computer_numbers1 = random.choice(random_numbers2)
computer_numbers2 = random.choice(random_numbers3)
computer_numbers3 = random.choice(random_numbers4)
computer_numbers4 = random.choice(random_numbers5)
computer_numbers5 = random.choice(random_numbers6)
computer_numbers6 = random.choice(random_numbers7)
computer_numbers7 = random.choice(random_numbers8)
computer_numbers8 = random.choice(random_numbers9)
computer_numbers9 = random.choice(random_numbers10)
#welcoming the user to the program, i mean here the program starts
print("Welcome to Random passoword creator")
print("Do you want to create a Random password ?")
user_input = input()
user_id = input("Username - ") 
if user_input == "y":
  print("\n Ok, so how many elements do you want in your password - 8, 9, 10")
  user_input2 = input()
  print("\n What your Password should be made of  \n like - characters(abcd), number(1234) or mixed(ab12) \n c for characters, n for numbers and m for mixed")
  number_word = input()
  #here comes the only word code ...
  if number_word == "c":
    if user_input2 == '8':
      #here i created a variable named final in which i can store the result password
      final = computer_word1 + computer_word2 + computer_word3 + computer_word4 + computer_word5 + computer_word6 + computer_word7 + computer_word8 
      print('Password = ', final, "\n Your username and password is saved in password.txt file , you can go check it out in case you forgot your password!!")
      password_saver = open('password.txt', 'a')
      password_saver.write('\n Date - ')
      password_saver.write(str(today))
      password_saver.write(' Time - ')
      password_saver.write(str(current_time))
      password_saver.write('\n')
      password_saver.write(user_id)
      password_saver.write(' - ')
      password_saver.write(final)
      password_saver.close()
      message('Random Password Generator', "Password Created!!!!!!")
      print("Type C to copy the text or N to exit")
      user_copy = input()
      if user_copy == "C" or "c":
        pyperclip.copy(final)
        spam = pyperclip.paste()
      else :
        quit()
      quit() # quit is better than break according to me...
    if user_input2 == '9':
      #here i created a variable named final in which i can store the result password
      final = computer_word1 + computer_word2 + computer_word3 + computer_word4 + computer_word5 + computer_word6 + computer_word7 + computer_word8 + computer_word9 
      print('Password = ', final, "\n Your username and password is saved in password.txt file , you can go check it out in case you forgot your password!!")
      password_saver = open('password.txt', 'a')
      password_saver.write('\n Date - ')
      password_saver.write(str(today))
      password_saver.write(' Time - ')
      password_saver.write(str(current_time))
      password_saver.write('\n')
      password_saver.write(user_id)
      password_saver.write(' - ')
      password_saver.write(final)
      password_saver.close()
      message('Random Password Generator', "Password Created!!!!!!")
      print("Type C to copy the text or N to exit")
      user_copy = input()
      if user_copy == "C" or "c":
        pyperclip.copy(final)
        spam = pyperclip.paste()
      else :
        quit()
      quit()
    if user_input2 == '10':
      #here i created a variable named final in which i can store the result password
      final = computer_word1 + computer_word2 + computer_word3 + computer_word4 + computer_word5 + computer_word6 + computer_word7 + computer_word8 + computer_word9 + computer_word10
      print('Password = ', final, "\n Your username and password is saved in password.txt file , you can go check it out in case you forgot your password!!")
      password_saver = open('password.txt', 'a')
      password_saver.write('\n Date - ')
      password_saver.write(str(today))
      password_saver.write(' Time - ')
      password_saver.write(str(current_time))
      password_saver.write('\n')
      password_saver.write(user_id)
      password_saver.write(' - ')
      password_saver.write(final)
      password_saver.close()
      message('Random Password Generator', "Password Created!!!!!!")
      print("Type C to copy the text or N to exit")
      user_copy = input()
      if user_copy == "C" or "c":
        pyperclip.copy(final)
        spam = pyperclip.paste()
      else :
        quit()
      quit()
  # here comes the number only password code
  if number_word == "n":
    #here we tell the program that if user types 8 give him 8 elements result
    if user_input2 == '8':
      #here i created a variable named final in which i can store the result password
      final = computer_numbers1 + computer_numbers2 + computer_numbers3 + computer_numbers4 + computer_numbers5 + computer_numbers6 + computer_numbers7 + computer_numbers8 
      print('Password = ', final, "\n Your username and password is saved in password.txt file , you can go check it out in case you forgot your password!!")
      password_saver = open('password.txt', 'a')
      password_saver.write('\n Date - ')
      password_saver.write(str(today))
      password_saver.write(' Time - ')
      password_saver.write(str(current_time))
      password_saver.write('\n')
      password_saver.write(user_id)
      password_saver.write(' - ')
      password_saver.write(final)
      password_saver.close()
      message('Random Password Generator', "Password Created!!!!!!")
      print("Type C to copy the text or N to exit")
      user_copy = input()
      if user_copy == "C" or "c":
        pyperclip.copy(final)
        spam = pyperclip.paste()
      else :
        quit()
      quit()
    #here we tell the program that if user types 9 give him 9 elements result
    elif user_input2 == '9':
      #here i created a variable named final in which i can store the result password
       final = computer_numbers1 + computer_numbers2 + computer_numbers3 + computer_numbers4 + computer_numbers5 + computer_numbers6 + computer_numbers7 + computer_numbers8 + computer_numbers9
       print('Password = ', final, "\n Your username and password is saved in password.txt file , you can go check it out in case you forgot your password!!")
       password_saver = open('password.txt', 'a')
       password_saver.write('\n Date - ')
       password_saver.write(str(today))
       password_saver.write(' Time - ')
       password_saver.write(str(current_time))
       password_saver.write('\n')
       password_saver.write(user_id)
       password_saver.write(' - ')
       password_saver.write(final)
       password_saver.close()
       message('Random Password Generator', "Password Created!!!!!!")
       print("Type C to copy the text or N to exit")
       user_copy = input()
       if user_copy == "C" or "c":
          pyperclip.copy(final)
          spam = pyperclip.paste()
       else :
           quit()
       quit()
    #here we tell the program that if user types 10 give him 10 elements result
    elif user_input2 == '10':
      #here i created a variable named final in which i can store the result password
      final = computer_numbers1 + computer_numbers2 + computer_numbers3 + computer_numbers4 + computer_numbers5 + computer_numbers6 + computer_numbers7 + computer_numbers8 + computer_numbers9 +computer_numbers
      print('Password = ', final, "\n Your username and password is saved in password.txt file , you can go check it out in case you forgot your password!!")
      password_saver = open('password.txt', 'a')
      password_saver.write('\n Date - ')
      password_saver.write(str(today))
      password_saver.write(' Time - ')
      password_saver.write(str(current_time))
      password_saver.write('\n')
      password_saver.write(user_id)
      password_saver.write(' - ')
      password_saver.write(final)
      password_saver.close()
      message('Random Password Generator', "Password Created!!!!!!")
      print("Type C to copy the text or N to exit")
      user_copy = input()
      if user_copy == "C" or "c":
          pyperclip.copy(final)
          spam = pyperclip.paste()
      else :
          quit()
      quit()
  #here comes the mixed password code
  if number_word == 'm':
      #here we tell the program that if user types 8 give him 8 elements result
      if user_input2 == "8":
        #here i created a variable named final in which i can store the result password
        final = computer_random1 + computer_random2 + computer_random3 + computer_random4 + computer_random5 + computer_random6 + computer_random7 + computer_random8 
        print('Password = ', final, "\n Your username and password is saved in password.txt file , you can go check it out in case you forgot your password!!")
        password_saver = open('password.txt', 'a')
        password_saver.write('\n Date - ')
        password_saver.write(str(today))
        password_saver.write(' Time - ')
        password_saver.write(str(current_time))
        password_saver.write('\n')
        password_saver.write(user_id)
        password_saver.write(' - ')
        password_saver.write(final)
        password_saver.close()
        message('Random Password Generator', "Password Created!!!!!!")
        print("Type C to copy the text or N to exit")
        user_copy = input()
        if user_copy == "C" or "c":
          pyperclip.copy(final)
          spam = pyperclip.paste()
        else :
            quit()
        quit()
      #here we tell the program that if user types 9 give him 9 elements result
      elif user_input2 == "9":
        #here i created a variable named final in which i can store the result password
        final = computer_random1 + computer_random2 + computer_random3 + computer_random4 + computer_random5 + computer_random6 + computer_random7 + computer_random8 + computer_random9
        print('Password = ', final, "\n Your username and password is saved in password.txt file , you can go check it out in case you forgot your password!!")
        password_saver = open('password.txt', 'a')
        password_saver.write('\n Date - ')
        password_saver.write(str(today))
        password_saver.write(' Time - ')
        password_saver.write(str(current_time))
        password_saver.write('\n')
        password_saver.write(user_id)
        password_saver.write(' - ')
        password_saver.write(final)
        password_saver.close()
        message('Random Password Generator', "Password Created!!!!!!")
        print("Type C to copy the text or N to exit")
        user_copy = input()
        if user_copy == "C" or "c":
          pyperclip.copy(final)
          spam = pyperclip.paste()
        else :
            quit()
        quit()
      #here we tell the program that if user types 10 give him 10 elements result
      elif user_input2 == "10":
        #here i created a variable named final in which i can store the result password
        final = computer_random + computer_random1 + computer_random2 + computer_random3 + computer_random4 + computer_random5 + computer_random6 + computer_random7 + computer_random8 + computer_random9
        print('Password = ', final, "\n Your username and password is saved in password.txt file , you can go check it out in case you forgot your password!!")
        password_saver = open('password.txt', 'a')
        password_saver.write('\n Date - ')
        password_saver.write(str(today))
        password_saver.write(' Time - ')
        password_saver.write(str(current_time))
        password_saver.write('\n')
        password_saver.write(user_id)
        password_saver.write(' - ')
        password_saver.write(final)
        password_saver.close()
        message('Random Password Generator', "Password Created!!!!!!")
        print("Type C to copy the text or N to exit")
        user_copy = input()
        if user_copy == "C" or "c":
          pyperclip.copy(final)
          spam = pyperclip.paste()
        else :
            quit()


        quit()
elif user_input == "n":
  print("goodbye")
else :
  print("wrong input ( you must type n for no and y for yes")

