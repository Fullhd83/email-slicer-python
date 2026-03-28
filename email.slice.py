email = input('enter your email here: ')

#just testing the email for validity, not checking for all the rules of email validation

if email.count('@') != 1:
    
    print('invalid email')

elif " " in email:
    print('email should not have a space')


else:
    separated_email = email.split('@')
    username = separated_email[0]
    domain = separated_email[1]
    
    if username == '' or domain == '':
        print('email should have a username and domain')
    
    else:

        print(f'username: {username}')
        print(f'domain: {domain}')