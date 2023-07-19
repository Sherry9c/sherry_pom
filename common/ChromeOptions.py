from selenium import webdriver


def options():

    options = webdriver.ChromeOptions()

    # 页面加载策略
    # ''' 设置为none时，Selenium WebDriver只等待HTML初始页面被下载
    #     设置为eager时，Selenium WebDriver等待直到初始的HTML文档完全加载和解析完毕（DOMContentLoaded事件触发），并忽略加载样式表、图像和子框架。
    #     默认为normal，将使Selenium WebDriver等待整个页面被加载。
    # '''
    options.page_load_strategy = 'eager'

    # 浏览器最大化
    options.add_argument('start-maximized')
    # 指定位置启动浏览器
    # options.add_argument('window-position=2500,200')
    # 设置窗体的启动大小
    # options.add_argument('window-size=1200,800')

    # 去掉浏览器提示自动化黄条:没什么用处(附加去掉控制台多余日志信息)
    options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])

    # 无头模式：不在桌面实现浏览器的运行，作为后台静默运行，虽然看不到，但是一切照旧。偶尔场景会有异常，但很少
    # options.add_argument('--headless')

    # 读取本地缓存的操作：webdriver启动的时候默认是不会加载本地缓存数据的。有时候想要绕过验证码或者登录流程，可以通过加载本地缓存来实现
    # 调用本地缓存一定要先关闭所有的浏览器，不然会报错。
    options.add_argument(r'--user-data-dir=E:\Study\python\repos\User Data')
    # 去掉账号密码弹出框
    prefs = dict()
    prefs['credentials_enable_service'] = False
    prefs['profile.password_manager_enable'] = False
    # 缺少了一行代码，用于调用这个字典
    options.add_experimental_option('prefs', prefs)
