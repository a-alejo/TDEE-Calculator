# User demographic
print('Please enter your information! '
      '\n------------------------------')
Weight = int(input('\nEnter your weight in pounds: '))
Height = int(input('Enter your height in inches: '))
Age = int(input('Enter your age in years: '))
isMale = input('Are you male? (y/n): ')

if isMale == 'y':
    isMale = True
elif isMale == 'n':
    isMale = False
else:
    print('Error')
    quit()

# Male BMR Formula
if isMale:
    BMR = 66 + (6.23 * Weight) + (12.7 * Height) - (6.8 * Age)
# using else for Female BMR Formula
else:
    BMR = 665 + (4.35 * Weight) + (4.7 * Height) - (4.7 * Age)

BMR = round(BMR, 2)
print('\nYour BMR is ' + str(BMR) + ' (The amount of calories you burn at rest)')


activity_level = int(input('------------------------------'
                           '\n\nNow lets calculate your TDEE! Please select one:'
                           '\nEnter 1 - If you rarely exercise'
                           '\nEnter 2 - If you exercise on 1 to 3 days per week'
                           '\nEnter 3 - If you exercise on 3 to 5 days per week'
                           '\nEnter 4 - If you exercise 6 to 7 days per week'
                           '\nEnter 5 - If you exercise every day and have a physical job or if you often exercise '
                           'twice a day'
                           '\n\nWhat is your activity level?: '))
if activity_level == 1:
    activity_level = round((BMR * 1.2), 2)
    print('\nYour TDEE is ' + str(activity_level) + ' (The amount of calories you burn each day including physical '
                                                    'activity)')
if activity_level == 2:
    activity_level = round((BMR * 1.375), 2)
    print('\nYour TDEE is ' + str(activity_level) + ' (The amount of calories you burn each day including physical '
                                                    'activity)')
if activity_level == 3:
    activity_level = round((BMR * 1.55), 2)
    print('\nYour TDEE is ' + str(activity_level) + ' (The amount of calories you burn each day including physical '
                                                    'activity)')
if activity_level == 4:
    activity_level = round((BMR * 1.725), 2)
    print('\nYour TDEE is ' + str(activity_level) + ' (The amount of calories you burn each day including physical '
                                                    'activity)')
if activity_level == 5:
    activity_level = round((BMR * 1.9), 2)
    print('\nYour TDEE is ' + str(activity_level) + ' (The amount of calories you burn each day including physical '
                                                    'activity)')

print(('******************************'
       '\n\nSo to achieve "weight loss" you need to eat less than ' +
       str(activity_level) + ' calories per day.'
                             '\nHow fast you lose it depends on how much your deficit is every day. '
                             '\nMost dietitians recommend eating a deficit of anywhere between 500-1,'
                             '000 calories a day.'
                             '\n\nThank you!'
                             '\n\n******************************'))


'''str.format() 
Test Male = 170, 71, 43, y = 1,734.4 calories - option 3
    if the man exercises 3 days a week, 
    his daily caloric requirement is 1,734.4 x 1.55, = 2,688.3 calories.
Test Female = 130, 63, 36, n = 1,357.4 calories
    if the woman in the example exercises 6 days a week, 
    her daily caloric requirement is 1,357.4 x 1.725 = 2,342.5 calories.
'''
