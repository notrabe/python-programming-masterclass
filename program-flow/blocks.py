name = input('please enter your name: ')
age = int(input('how old are you, {0}? '.format(name)))
print(age)

if age >= 18:
    print('You are old enough to vote.')
    print('Please put an X in the box.')
elif age == 900:
    print('Sorry Yoda, you die in Return of the Jedi.')
else:
    print('Please come back in {0} years'.format(18 - age))