print('------------------------welcome State Bank of India------------------------')
print('\n')
create = int(input('to create new account type 1 and press enter '))
if create == 1:
    print("------------ fill the account creation form ------------")
else:
    print('thanks for visiting,checkout our other option from your near branch.....')
    exit()
name,mobile,dob,aadhar= input('enter your full name: '),int(input('enter your mobile number: ')),input('enter your birthdate (in dd mm yyyy)'),input('enter last four digit of aadhar card number: ')
print('\n')
print('     congratulation your account will be created with 1000 rupees ')
print('name:                          ',name)
print('mobile number:                 ',mobile)
print('date of birth:                 ',dob)
print('aadhar number:                 ',aadhar)
print('branch ifsc code :              SBIN0050869')
print('city:                           rajkot')


print('\n')

balance = 1000
deposite = int(input(" to deposite money press 1 for withdraw money press 2 "))
if deposite == 1:
    a = int(input("enter amount for deposite: "))
    balance = a + balance
    print('deposite sucessfully ')
    print('your currunt balance is',balance)
if deposite == 2:
    a = int(input("enter amount for withdraw: "))
    balance = balance-a
    if balance >=500:
        print('withdraw successfully ')
        print('your currunt balance is',balance)
    else:
        print('you are not eligible for withdraw money because minimum amount of account is 500 rupees')
        balance = balance+a
        print('your corrunt balance is',balance)
