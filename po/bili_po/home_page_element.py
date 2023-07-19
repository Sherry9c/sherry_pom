class HomePageElement:
    # 不唯一，都能用
    jump_to_login_bt=('xpath', '//button[text()="Log in"]')
    login_by_phone_email=('xpath', '//button/div[text()="Log in with Phone/Email "]')
    logout_bt = ('xpath', '//a/span[text()="Log Out"]')

    user_img = ('xpath', '//a/span[@class="bstar-header-avatar"]/img')
    profile_bt = ('xpath', '//div[@class="bstar-header-user-content__list"]/a/span[text()="My Profile"]')
    creator_bt = ('xpath', '//div[@class="bstar-header-user-content__list"]/a/span[text()="Creator Center"]')
    login_list=('xpath','//div[@class="login-main"]')