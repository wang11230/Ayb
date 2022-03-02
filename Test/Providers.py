# !/usr/bin/python
# -*-coding:utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains  # 引入actionchains类
from selenium.webdriver.common.keys import Keys  # 引入keys模块
from selenium.webdriver.support.select import Select  # 引入Select区分大小写
import os  # 调用AutoIt

driver = webdriver.Chrome()
# 调用登陆函数
import providers_Login

sleep(2)

providers_Login.Login().user_login(driver)
sleep(2)
# 显式等待，使用is_displayed()方法来判断元素是否可见。for循环5次，每次循环判断元素的is_displayed()的状态是否
# 为true，如果是true，则break跳出循环，否则sleep(1)后继续循环判断，知道5次循环结束后，打印超时信息。
for i in range(5):
    try:
        el = driver.find_element_by_link_text('商家中心')
        if el.is_displayed():
            break
    except:
        pass
    sleep(1)
else:
    print('等待超时')
    driver.close()

# 获取当前窗口句柄
search_windows = driver.current_window_handle
driver.find_element_by_link_text('商家中心').click()
# 获得当前所有窗口句柄
all_handles = driver.window_handles

for handle in all_handles:
    if handle != search_windows:
        driver.switch_to.window(handle)
# 跳转到商家中心页面进行以下操作
sleep(2)
driver.find_element_by_link_text('管理').click()
driver.find_element_by_link_text('基础档案管理').click()
driver.find_element_by_link_text('添加档案').click()
sleep(1)
Select(driver.find_element_by_id('providers_rst')).select_by_index('1')
sleep(2)
driver.find_element_by_id('providers_rst_1').send_keys(u'测试')
driver.find_element_by_xpath(
    '//*[@id="page-wrapper"]/div[2]/div/div[2]/div/div/div/form/div[2]/div[1]/div[2]/div[1]/div/div/label[1]/input').click()
driver.find_element_by_id('providers_rst_2').send_keys('15333512317')
Select(driver.find_element_by_id('providers_rst_3')).select_by_value('string:山西省')
Select(driver.find_element_by_id('providers_rst_4')).select_by_index('1')
driver.find_element_by_id('providers_rst_7').send_keys('513436200012177661')
driver.find_element_by_id('providers_rst_8').click()
sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/button').click()
sleep(2)
driver.find_element_by_id('providers_rst_9').send_keys(u'太原市')
driver.find_element_by_xpath(
    '//*[@id="page-wrapper"]/div[2]/div/div[2]/div/div/div/form/div[2]/div[1]/div[2]/div[10]/div/div/label[1]/input').click()
sleep(1)
js = "document.getElementById('validStartTime').removeAttribute('readonly')"  # 时间控件，无法直接输入。原生js，移除属性
driver.execute_script(js)
driver.find_element_by_id('validStartTime').send_keys('2019-12-06')  # 写入日期
Select(driver.find_element_by_id('providers_rst_12')).select_by_index('1')
Select(driver.find_element_by_id('providers_rst_13')).select_by_index('6')
Select(driver.find_element_by_id('providers_rst_14')).select_by_index('1')
driver.find_element_by_id('providers_rst_15').send_keys(u'身体健康')
Select(driver.find_element_by_id('providers_rst_16')).select_by_index('4')
# 上传图片 借助第三方AutoIt实现图片上传
driver.find_element_by_id('providers_rst_5').click()  # 上传头像
sleep(3)
os.system('D:\\update.exe')  # 调用AutoIt上传程序
sleep(3)
driver.find_element_by_id('providers_rst_6').click()
sleep(2)
driver.find_element_by_id('providers_rst_10').click()
sleep(2)
os.system('D:\\update.exe')
sleep(2)
driver.find_element_by_id('providers_rst_11').click()  # 上传身份证
sleep(5)
# driver.find_element_by_id('providers_rst_10').send_keys('D:\\test.jpg')
target = driver.find_element_by_id('providers_rst_16')  # 网页滚动到指定元素
driver.execute_script('arguments[0].scrollIntoView();', target)
sleep(2)
Select(driver.find_element_by_id('providers_rst_20')).select_by_index(3)
driver.find_element_by_id('providers_rst_21').send_keys(u'王大锤')
driver.find_element_by_id('providers_rst_22').send_keys('15333512316')
driver.find_element_by_id('providers_rst_23').send_keys(u'太原市北大街')
target = driver.find_element_by_id('providers_rst_21')  # 网页滚动到指定元素
driver.execute_script('arguments[0].scrollIntoView();', target)
sleep(2)
Select(driver.find_element_by_id('providers_rst_24')).select_by_index('1')
Select(driver.find_element_by_id('providers_rst_25')).select_by_value('string:taiyuan')
sleep(2)
Select(driver.find_element_by_id('providers_rst_27')).select_by_value('string:BPN_AYB_TY')
sleep(2)
double_click = driver.find_element_by_id('providers_rst_28')
ActionChains(driver).double_click(double_click).perform()
sleep(1)
driver.find_element_by_xpath('//*[@id="providers_rst_28"]/input[1]').send_keys(u'太原市迎泽区人民政府')
sleep(2)
driver.find_element_by_xpath('//*[@id="providers_rst_28"]/input[1]').send_keys(Keys.ENTER)
sleep(3)
driver.find_element_by_id('providers_rst_29').send_keys(u'Python自动输入')
sleep(3)
# driver.find_element_by_id('vm.queryEntity.baseRecord.branchID').click()
driver.find_element_by_xpath(
    '//*[@id="page-wrapper"]/div[2]/div/div[2]/div/div/div/form/div[2]/div[4]/div[2]/div[7]/div[2]/choose-store/div/div').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="providers_rst_31"]').click()
sleep(3)
js = 'window.scrollTo(0,750);'
driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[2]/div/div[2]/div/div/div/form/div[3]/button').click()
js = 'window.scrollTo(0,750);'  # 网页按照尺寸滚动
driver.execute_script(js)
all_handles = driver.window_handles
driver.switch_to.window(all_handles[0])
sleep(2)
driver.find_element_by_link_text('客户中心').click()
sleep(3)
driver.quit()
