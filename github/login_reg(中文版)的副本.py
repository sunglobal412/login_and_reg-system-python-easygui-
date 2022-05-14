import easygui as g

#参数定义
userL = 0
userR = 0
flag = 0
register = []

#全局定义

#方法定义
def reg_is_login(user,pwd):
    global flag
    if register[0] == user:
        print('user:ok')
        if register[1] == pwd:
            flag = 5
            print('pwd:ok')
        else:
            g.msgbox(title='错误',msg='用户名或密码错误(请注意登录次数)')
            print('pwd:no')
    else:
        g.msgbox(title='错误',msg='用户名或密码错误(请注意登录次数)')
        print('user:no')

#执行代码
while flag < 4:
    a = g.buttonbox(title='[TEST]',msg='欢迎来到[TEST]',choices=('登录','注册','版本','退出'),image='img/1.png')
    if a == '登录':
        if register != []:
            userL = g.enterbox(title='登录',msg='请输入用户名')
            pwdL = g.passwordbox(title='登录',msg='请输入密码')
            reg_is_login(userL,pwdL)
            flag += 1
            print(flag)
        else:
            g.msgbox(title='错误',msg='您尚未注册，请注册！')
    elif a == '注册':
        userR = g.enterbox(title='注册',msg='请输入你想要的用户名')
        pwdR = g.passwordbox(title='注册',msg='请输入注册密码')
        register = [userR,pwdR]
        print(register)
    elif a == '版本':
        g.msgbox(title='版本',msg='版本:0.11.3 , 版本号:A92JS7J10.11.3HOA')
    elif a == '退出':
        flag = 8
    else:
        g.msgbox(title='错误',msg='选择错误，请重新选择!')

if flag == 4:
    g.msgbox(title='错误',msg='给你的登录次数已经过了！')
    print(flag)
elif flag == 6:
    g.msgbox(title='成功',msg='您已登陆成功！')
else:
    g.msgbox(title='退出',msg='您已成功退出！')
