country = input('請問你是哪國人: ')
if country != '台灣' and country != '美國':
    print('你只能輸入台灣或美國喔!!')
age = input('請問你幾歲: ')
age = int(age)
if country == '台灣':
    if age >= 18:
        print('你可以考駕照了')
    else:
        print('你還不能考駕照喔')
elif country == '美國':
    if age >= 16:
          print('你可以考駕照了')
    else:
        print('你還不能考駕照喔')                
