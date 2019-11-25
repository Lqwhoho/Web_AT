# coding=utf-8
from selenium import webdriver
import unittest
import time
from selenium.webdriver.chrome.options import Options


class Youdao(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
        # cls.driver = webdriver.Firefox()  # 不开启静默模式
        # options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        # cls.driver = webdriver.Chrome(options=options)    # 开启静默模式


    @classmethod
    def tearDownClass(cls):
        pass

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        self.imgs = []
        self.addCleanup(self.cleanup)
        # self.driver = webdriver.Chrome()  # 不开启静默模式
        
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 无界面
        chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错问题
        chrome_options.add_argument('--disable-gpu')   # 禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动。chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
        self.driver = webdriver.Chrome('chromedriver',options=chrome_options)
        
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.youdao.com"
        self.verificationErrors = []
        self.accept_next_alter = True
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def cleanup(self):
        pass

    # 有道搜索用例
    def test_youdao_search(self):
        u"""中译英：成功"""
        driver = self.driver
        driver.get(self.base_url + "/")

        driver.find_element_by_id("translateContent").send_keys(u"成功")
        self.add_img()
        driver.find_element_by_xpath("/html/body/div[5]/div/form/button").click()
        time.sleep(5)
        self.add_img()

        try:
            driver.find_element_by_xpath("/html/body/div[7]/i/a[1]").click()
            self.add_img()
        except:
            print('没有广告弹窗')
            pass
      

if __name__ == "__main__":
    unittest.main()

