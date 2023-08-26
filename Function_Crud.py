# # CRUD ...
mydict={}
trash1={}
while True:
    def create():
        mobile= int(input('enter your mobile number:- '))
        if len(str(mobile)) == 10:
            name= input('enter your name:- ')
            email= input('enter your email:- ')
            if '@gmail.com' in email:
                password = input('create password:- ')
                if '@' in password:
                    data={'Name':name,'Email':email,'Password':password}
                    mydict[mobile]=data
                    print('account created successfully..')
                else:
                    print('create a strong password')
            else:
                print('invalid gmail')
        else:
            print('wrong number')
    def read():
        mobile= int(input('enter your mobile:- '))
        if len(str(mobile))==10:
            if mobile in mydict:
                print(mydict[mobile])
            else:
                print('data does not exist..')
        else:
            print('it is not a 10 digit number..')
    def update():
        mobile= int(input('enter registered mobile number:- '))
        if len(str(mobile))==10:
            if mobile in mydict:
                print(' 1)mobile\n 2)name\n 3)email\n 4)password')
                option= int(input('choose an option to update:- '))
                if option==1:
                    new_mobile=int(input('enter new mobile number:- '))
                    if len(str(new_mobile))==10:
                        old_num= mydict[mobile]
                        mydict[new_mobile]=old_num
                        del old_num
                        print('number changed successfully..')
                    else:
                        print('it is not a 10 digit number..')
                elif option==2:
                    new_name= input('enter new name:- ')
                    mydict[mobile]['Name']=new_name
                    print('name changed successfully..')
                elif option==3:
                    new_email= input('enter new email:- ')
                    mydict[mobile]['Email']=new_email
                    print('email changed successfully..')
                elif option==4:
                    new_password= input('enter new password:- ')
                    mydict[mobile]['Password']=new_password
                    print('password changed successfully..')
                else:
                    print('wrong option to update..')
            else:
                print('data does not exist..')
        else:
            print('it is not a 10 digit number..')
    def delete():
        mobile= int(input('enter registered number:- '))
        if len(str(mobile))==10:
            if mobile in mydict:
                a= mydict[mobile]
                trash1[mobile]=a
                # print(trash1)
                del mydict[mobile]
                print('data deleted successfully..')
            else:
                print('data does not exist..')
        else:
            print('it is not a 10 digit number..')
    def trash():
        mobile=int(input('enter registered mobile number:- '))
        if mobile in trash1:
            print(trash1[mobile])
        else:
            print('data dismatch..')
    def restore():
        mobile= int(input('enter regestered number:- '))
        if mobile in trash1:
            mydict[mobile]=trash1[mobile]
            print('data restored successfully..')
            print(mydict[mobile])
            print(mydict)
        else:
            print('data is not available..')
    print(' 1)create\n 2)read\n 3)update\n 4)delete\n 5)trash\n 6)restore')
    choice= int(input('enter an option:- '))
    if choice==1:
        create()
    elif choice==2:
        read()
    elif choice==3:
        update()
    elif choice==4:
        delete()
    elif choice==5:
        trash()
    elif choice==6:
        restore()
    else:
        print('wrong option')

