# 银行操作
# 开户,查询,存款,转账,改密,锁卡,解卡,补卡,销户

from cards import Card
from users import User
import random
import pickle
import os


class Bank:
    def __init__(self):
        pass
        self.users = []  # 当前银行系统的所有用户
        self.file_path = 'users.txt'  # 本地文件路径
        # 启动银行系统后, 立刻获取users.txt文件中之前保存的所有用户
        self.__get_users()
        print('=> 原来的所有用户: ', self.users)

    # 保存用户对象到文件中
    def __save_users(self):
        # 写入文件
        fp = open('self.file_path', 'wb')
        pickle.dump(self.users, fp)
        fp.close()
        print('=> 当前所有用户: ', self.users)

    # 每次运行项目后都要重新获取user.txt文件中的所有用户
    def __get_users(self):
        # 读取文件
        if os.path.exists('self.file_path'):
            fp = open('self.file_path', 'rb')
            self.users = pickle.load(fp)
            fp.close()

    # -------------------------- 分割线------------------------------
    # 开户
    def create_user(self):
        pass
        # 1.创建卡
        # 卡号
        cardid = self.__creat_cardid()
        print('=> 成功创建卡号: ', cardid)
        # 卡密码
        passwd = self.__set_password()
        if not passwd:
            return
        # 卡余额
        money = float(input('请您输入要预存的金额:'))
        # 创建卡对象
        card = Card(cardid, passwd, money)
        print('=> 创建卡成功: ', card)

        # 2.创建用户
        name = input('请输入您的真实姓名:')
        idcard = input('请输入您的身份证号码:')
        phone = input('请输入您的手机号码:')
        # 创建用户对象
        user = User(name, phone, idcard, card)
        print('=> 创建用户成功: ', user)

        # 3.将新用户存储
        # 将新用户加入到银行系统中
        self.users.append(user)
        # 存储
        self.__save_users()

    # -------------------------- 分割线------------------------------

    # 创建随机,唯一卡号
    def __creat_cardid(self):
        while True:
            # 生成随机卡号
            cardid = '8888'
            for i in range(4):
                cardid += str(random.randint(0, 9))

            # 如果有一个用户的卡号和cardid相同,则break继续执行while,否则返回cardid
            for user in self.users:
                if user.card.cardid == cardid:
                    break
                else:
                    return cardid

    # -------------------------- 分割线------------------------------

    # 设置密码
    def __set_password(self):
        # 允许输错3次
        for i in range(3):
            passwd = input('请您输入密码:')
            passwd2 = input('请再输入一次:')
            # 验证两次密码是否一致
            if passwd == passwd2:
                return passwd
            print('=> 2次密码不一致,请重新输入...')
        else:
            print('您输入了3次错误密码.')
            return False

    # -------------------------- 分割线------------------------------

    # 查询
    def search_money(self):
        pass
        # 1.输入卡号
        user = self.__input_cardid()
        if not user:
            print('=> 卡号不存在.')
            return
        # 2.输入密码: 考虑允许输错3次,否组锁卡
        for i in range(3):
            passwd = input('请您输入密码:')
            if passwd != user.card.passwd:
                print('密码错误,请重新输入')
            if passwd == user.card.passwd:
                break
        else:
            print('您输入了3次错误密码.已锁卡')
            user.card.islock = True
        self.__save_users()

        # 密码只能输入一次
        # passwd = input('请输入银行卡密码:')
        # if passwd != user.card.passwd:
        #     print('密码错误.')
        #     return

        # 3.显示余额
        print('当前余额:', user.card.money)

    # 输入卡号
    def __input_cardid(self):
        cardid = input('请输入要查询的银行卡号:')
        # 如果卡号存在就返回所在的用户对象,否则默认返回None
        for user in self.users:
            if user.card.cardid == cardid:
                return user

    # -------------------------- 分割线------------------------------

    # 存款
    def save_money(self):
        pass
        # 1.输入卡号
        user = self.__input_cardid()
        if not user:
            print('=> 卡号不存在.')
            return
        # 2.输入密码: 考虑允许输错3次,否组锁卡
        for i in range(3):
            passwd = input('请您输入密码:')
            if passwd != user.card.passwd:
                print('密码错误,请重新输入')
            if passwd == user.card.passwd:
                break
        else:
            print('您输入了3次错误密码.已锁卡')
            user.card.islock = True
        self.__save_users()

        # 密码只能输入一次
        # passwd = input('请输入银行卡密码:')
        # if passwd != user.card.passwd:
        #     print('密码错误.')
        #     return

        # 判断是否锁卡,锁卡不能存款
        if not user.card.islock:
        # 3.输入存款金额,并将对应user.card.money+=100
            deposit_money = float(input('请输入存款金额:'))
            user.card.money += deposit_money
            print('存款成功')
        else:
            print('您的卡已被锁,请解锁再进行操作')
        # 4.self.__save_users()
        self.__save_users()

    # -------------------------- 分割线------------------------------

    # 取款
    def get_money(self):
        pass
        # 1.输入卡号
        user = self.__input_cardid()
        if not user:
            print('=> 卡号不存在.')
            return
        # 2.输入密码: 考虑允许输错3次,否组锁卡
        for i in range(3):
            passwd = input('请您输入密码:')
            if passwd != user.card.passwd:
                print('密码错误,请重新输入')
            if passwd == user.card.passwd:
                break
        else:
            print('您输入了3次错误密码.已锁卡')
            user.card.islock = True
        self.__save_users()

        # 密码只能输入一次
        # passwd = input('请输入银行卡密码:')
        # if passwd != user.card.passwd:
        #     print('密码错误.')
        #     return

        # 判断是否锁卡,锁卡不能取款
        if not user.card.islock:
        # 3.输入取款金额,并将对应user.card.money-=100,判断是否足够-100
            withdrawal_money = float(input('请输入取款金额:'))
            if user.card.money < withdrawal_money:
                print('余额不足')
                return
            user.card.money -= withdrawal_money
            print('取款成功,请注意查收')
        else:
            print('您的卡已被锁,请解锁再进行操作')
        # 4.self.__save_users()
        self.__save_users()

    # -------------------------- 分割线------------------------------

    # 转账
    def transform_money(self):
        pass
        # 1.输入转出的卡号和对方的卡号
        print('下面请输入转出的卡号:')
        user_out = self.__input_cardid()
        if not user_out:
            print('=> 卡号不存在.')
            return
        print('下面请输入转入的卡号:')
        user_in = self.__input_cardid()
        if not user_in:
            print('=> 卡号不存在.')
            return
        # 2.输入转出的密码
        for i in range(3):
            passwd = input('请您输入密码:')
            if passwd != user_out.card.passwd:
                print('密码错误,请重新输入')
            if passwd == user_out.card.passwd:
                break
        else:
            print('您输入了3次错误密码.已锁卡')
            user_out.card.islock = True
        self.__save_users()

        # 密码只能输入一次
        # passwd = input('请输入银行卡密码:')
        # if passwd != user_out.card.passwd:
        #     print('密码错误.')
        #     return

        # 判断是否锁卡,锁卡不能转账
        if not user_out.card.islock:
        # 3.输入转账金额,并+=100 -=100,判断是否足够-100
            withdrawal_money = float(input('请输入转账金额:'))
            if user_out.card.money < withdrawal_money:
                print('余额不足')
                return
            user_out.card.money -= withdrawal_money
            user_in.card.money += withdrawal_money
            print('转账成功,请注意查收')
        else:
            print('您的卡已被锁,请解锁再进行交易')
        # 4.self.__save_users()
        self.__save_users()

    # -------------------------- 分割线------------------------------

    # 改密
    def modify_password(self):
        pass
        # 1.输入卡号
        user = self.__input_cardid()
        if not user:
            print('=> 卡号不存在.')
            return
        # 2.输入身份证
        idcard = input('请输入您的身份证号:')
        if idcard != user.idcard:
            print('=> 身份证号不存在.')
            return
        # 3.输入旧密码,再输入新密码
        passwd_old = input('请输入旧密码:')
        if passwd_old != user.card.passwd:
            return
        passwd_new = input('请输入新密码:')
        user.card.passwd = passwd_new
        # 4.self.__save
        self.__save_users()

    # -------------------------- 分割线------------------------------

    # 锁卡
    def lock_password(self):
        pass
        # 1.输入卡号
        user = self.__input_cardid()
        if not user:
            print('=> 卡号不存在.')
            return
        # 2.输入密码
        passwd = input('请输入银行卡密码:')
        if passwd != user.card.passwd:
            print('密码错误.')
            return
        # 3.锁卡 user.card.islock = True
        user.card.islock = True
        print('锁卡成功')
        # 4. self.__save
        self.__save_users()

    # -------------------------- 分割线------------------------------

    # 解锁
    def unlock_password(self):
        pass
        # 1.输入卡号
        user = self.__input_cardid()
        if not user:
            print('=> 卡号不存在.')
            return
        # 2.输入密码
        passwd = input('请输入银行卡密码:')
        if passwd != user.card.passwd:
            print('密码错误.')
            return
        # 3.锁卡 user.card.islock = False
        user.card.islock = False
        print('解锁成功')
        # 4. self.__save
        self.__save_users()

    # -------------------------- 分割线------------------------------

    # 补卡
    def makeup_card(self):
        pass
        user = self.__input_cardid()
        if not user:
            print('=> 卡号不存在.')
            return
        # 1.输入身份证
        idcard = input('请输入您的身份证号:')
        if idcard != user.idcard:
            print('=> 身份证号不存在.')
            return
        # 2.创建新卡,并替换旧卡: user.caed = card
        cardid = self.__creat_cardid()
        print('=> 成功创建卡号: ', cardid)
        passwd = self.__set_password()
        if not passwd:
            return
        user.card.cardid = cardid
        user.card.passwd = passwd

        # 3.
        self.__save_users()

    # -------------------------- 分割线------------------------------

    # 销户
    def delete_user(self):
        pass
        print('您正在进行销户,请谨慎...')
        # 1.输入卡号
        user = self.__input_cardid()
        cardid = user.card.cardid
        if not user:
            print('=> 卡号不存在.')
            return
        # 2.输入密码
        passwd = input('请输入银行卡密码:')
        if passwd != user.card.passwd:
            print('密码错误.')
            return
        # 3.输入身份证号
        idcard = input('请输入您的身份证号:')
        if idcard != user.idcard:
            print('=> 身份证号不存在.')
            return
        # 4.删除用户信息
        for user0 in self.users:
            if user0.card.cardid == cardid:
            # if user == user0:
                self.users.remove(user0)
                print('销户成功')

        self.__save_users()

