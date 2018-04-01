from selenium import webdriver
import os

driver = webdriver.Firefox()
driver.get('https://www.douban.com/')
driver.implicitly_wait(10)
driver.find_element_by_id('form_email').clear()
driver.find_element_by_id('form_email').send_keys('805416615@qq.com')
driver.find_element_by_id('form_password').clear()
driver.find_element_by_id('form_password').send_keys('qaz.1233')
driver.find_element_by_class_name('bn-submit').click()
print(driver.page_source.replace(u'\xa9', u''))
if os.path.isfile('index.html'):
    os.remove('index.html')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(driver.page_source)
f.close()