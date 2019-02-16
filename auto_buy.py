#python3.6.5
#coding:utf-8

'''
@time:2019-02-16 16:50
@author: 李铭

程序利用自动测试工具模拟用户下单操作，完成商品的抢购
仅作为学习过程中的实践，无商业用途
'''

from selenium import webdriver
import datetime
import time

#创建浏览器对象
driver = webdriver.Chrome()
#窗口最大化显示
driver.maximize_window()

def login(url,mall):
    '''
    登陆函数
    
    url:商品的链接
    mall：商城类别
    '''
    driver.get(url)
    driver.implicitly_wait(10)
    time.sleep(2)
    #淘宝和天猫的登陆链接文字不同
    if mall=='1':
        #找到并点击淘宝的登陆按钮
        driver.find_element_by_link_text("亲，请登录").click()
    else:
        #找到并点击天猫的登陆按钮
        driver.find_element_by_link_text("请登录").click()
    print("请在30秒内完成登录")
    #用户扫码登陆
    time.sleep(30)
    
def buy(buy_time,mall):
    '''
    购买函数
    
    buy_time:购买时间
    mall:商城类别
    
    获取页面元素的方法有很多，获取得快速准确又是程序的关键
    在写代码的时候运行测试了很多次，css_selector的方式表现最佳
    '''
    if mall=='1':
        #"立即购买"的css_selector
        btn_buy='#J_juValid > div.tb-btn-buy > a'
        #"立即下单"的css_selector
        btn_order='#submitOrder_1 > div.wrapper > a'
    else:
        btn_buy='#J_LinkBuy'
        btn_order='#submitOrder_1 > div > a'
        
    while True:
        #现在时间大于预设时间则开售抢购
        if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')>buy_time:
            try:
                #找到“立即购买”，点击
                if driver.find_element_by_css_selector(btn_buy):
                    driver.find_element_by_css_selector(btn_buy).click()
                    break
                time.sleep(0.1)
            except:
                time.sleep(0.3)
    
    while True:
        try:
            #找到“立即下单”，点击，
            if driver.find_element_by_css_selector(btn_order):
                driver.find_element_by_css_selector(btn_order).click()
                #下单成功，跳转至支付页面
                print("购买成功")
                break
        except:
            time.sleep(0.5)
            
    

if __name__ == "__main__":
    url=input("请输入商品链接:")
    mall=input("请选择商城（淘宝 1  天猫 2  输入数字即可）： ")
    bt=input("请输入开售时间【2019-02-15（空格）12:55:50】")
    login(url,mall)
    buy(bt,mall)
        
    