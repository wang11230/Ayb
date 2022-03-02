# coding=utf-8
from selenium import webdriver
from time import sleep


class Login():
    def user_login(self, driver):
        # driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('http://abc.demo.ayibang.cn/#/system/login')
        sleep(1.5)
        driver.find_element_by_name('user').send_keys('wangpengyu')
        driver.find_element_by_xpath('//*[@id="logindiv"]/div[2]/form/div/div[3]/div[1]/input').send_keys('15333512317')
        driver.find_element_by_xpath('//*[@id="logindiv"]/div[2]/form/div/div[3]/div[2]/input').send_keys('888888')
        sleep(1)
        driver.find_element_by_xpath('//*[@id="logindiv"]/div[2]/form/div/div[3]/div[3]/div/button').submit()

    def user_logout(self, driver):
        driver.find_element_by_xpath('退出').click()
