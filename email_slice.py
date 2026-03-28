while True:

    email = input('enter your email here: ')

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
    
    print('do you want to enter another email? (yes/no) (y/n)')
    answer = input().lower()
    
    if answer != 'yes' and answer != 'y':
        break
        