import sys
import random
import pdb

# sys.argv

# first = int(sys.argv[1])
# second = int(sys.argv[2])   


def check_guess(guess,random_num):
      try:
        if(guess >=0 and guess<=10):
            if(guess == random_num):
                    print('Your guess is correct')
                    return True
            
            elif(guess > random_num):
                    print('guess_num is grater than random_num')
                    print('keep guessing')
            elif(guess < random_num):
                    print('guess_num is lesser than random_num')
                    print('keep guessing')
            else:
                print(f'your number is greater than 10 ')
                return False;
      except TypeError as err:
            return err;            
   


if(__name__=='__main__'):
    random_num = random.randint(1,10)


    while True:
        try:
                guess_num = int(input('enter your num : '))
                if(check_guess(guess_num,random_num)):
                    break
            
        except ValueError:
                print('please enter a number')