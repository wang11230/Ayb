# !/usr/bin/python
# -*-coding:utf-8 -*-
while True:
    day = 1 #上班天数
    day_time = 1 #每日乘坐次数
    car_money = 0
    choose_car = int(input('请选择交通方式：1.公交 2.地铁:'))
    if choose_car == 1:
        print('==感谢您选择了公交出行==')
        card_style = int(input('请选择交通卡种类：1.普通卡 2.学生卡 ：'))
        if card_style == 1:
            car_length = int(input('请输入乘坐距离：'))
            print('开始计算总费用，请稍等...')
            if car_length <= 10:
                car_money = 2 * 0.5
                print('您的总费用为%.2f元，欢迎下次继续乘坐'%car_money)
            if car_length >10:
                i = 1
                n = int((car_length-10)/5)
                if (car_length-10)%5 == 0:
                    car_money = (3 + i * (n-1))*0.5
                    print('您的总费用为%.2f元，欢迎下次继续乘坐' % car_money)
                else:
                    car_money = (3 + i * n) * 0.5
                    print('您的总费用为%.2f元，欢迎下次继续乘坐' % car_money)
        if card_style == 2:
            car_length = int(input('请输入乘坐距离：'))
            print('开始计算总费用，请稍等...')
            if car_length <= 10:
                car_money = 2 * 0.25
                print('您的总费用为%.2f元，欢迎下次继续乘坐' % car_money)
            if car_length > 10:
                i = 1
                n = int((car_length - 10) / 5)
                if (car_length - 10) % 5 == 0:
                    car_money = (3 + i * (n - 1)) * 0.25
                    print('您的总费用为%.2f元，欢迎下次继续乘坐' % car_money)
                else:
                    car_money = (3 + i * n) * 0.25
                    print('您的总费用为%.2f元，欢迎下次继续乘坐' % car_money)
    if choose_car == 2:
        print('==感谢您选择了地铁出行==')
        ditie_length = int(input('请输入乘坐距离：'))
        dayC = int(input('请输入本月乘坐次数总和：'))
        print('开始计算总费用，请稍等...')
        if ditie_length <= 6:
            ditie_money = 3*dayC
            print('您的总费用为%.2f元，优惠信息计算中' %ditie_money)
        if ditie_length > 6 and ditie_length <=12:
            ditie_money = 4*dayC
            print('您的总费用为%.2f元，优惠信息计算中' %ditie_money)
        if ditie_length > 12 and ditie_length <=22:
            ditie_money = 5*dayC
            print('您的总费用为%.2f元，优惠信息计算中' %ditie_money)
        if ditie_length > 22 and ditie_length <=32:
            ditie_money = 6*dayC
            print('您的总费用为%.2f元，优惠信息计算中' %ditie_money)
        if ditie_length > 32:
            i = 1
            n = int((ditie_length - 32)/20)
            if (ditie_length - 32)%20==0:
                ditie_money = 7*dayC + (i * (n-1))*dayC
                print('您的总费用为%.2f元，优惠信息计算中' %ditie_money)
            else:
                ditie_money = 7*dayC + (i * n)*dayC
                print('您的总费用为%.2f元，优惠信息计算中' %ditie_money)

        if ditie_money >= 100 and ditie_money < 150:
            money = (ditie_money - 100)*0.2
            print('本月已优惠%s'%money)
            print('本月实际花费%s'%(ditie_money-money))
        if ditie_money >= 150 and ditie_money < 400:
            money = (ditie_money - 150)*0.5 + (149-100)*0.2
            print('本月已优惠%s'%money)
            print('本月实际花费%s'%(ditie_money-money))
        if ditie_money > 400:
            money = (149-100)*0.2+(399-150)*0.5#计算总共优惠信息
            print('本月已优惠%s' % money)
            print('本月实际花费%s' % (ditie_money - money))

