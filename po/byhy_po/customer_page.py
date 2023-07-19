from base.base_page import BasePage


class CustomerPage(BasePage):

    url = BasePage.url + 'mgr/#/customers'
    index = 1
    add_customer_btn = ('xpath', '//button[contains(text(),"添加")]')
    new_name_box = ('xpath', '//div[text()="客户名"]/input')
    new_phonenum_box = ('xpath', '//div[text()="联系电话"]/input')
    new_address_box = ('xpath', '//div[text()="地址"]/textarea')
    create_btn = ('xpath', '//button[text()="创建"]')
    cancel_btn = ('xpath', '//button[text()="取消"]')

    search_box = ('xpath', '//input[@placeholder="请输入关键词搜索"]')
    search_btn = ('id', 'btn_search_exams')

    index_btn_list = ('xpath', '//ul[@class="pagination"]/li')

    search_result_item_list = ('xpath', '//div[@class="search-result-item"]')
    customer_name_list = ('xpath', f'//span[text()="客户名："]/following-sibling::span[1][{index}]')
    customer_name_1 = ('xpath', f'//span[text()="客户名："]/following-sibling::span[1][1]')

    customer_phonenum_list = ('xpath', f'//span[text()="联系电话："]/following-sibling::span[1][{index}]')
    customer_address_list = ('xpath', f'//span[text()="地址："]/following-sibling::span[1][{index}]')
    edit_btn_list = ('xpath', f'//div[@class="search-result-item-actionbar"]/div/label[text()="编辑"][{index}]')
    del_btn_list = ('xpath', f'//div[@class="search-result-item-actionbar"]/div/label[text()="删除"][{index}]')

    # name必须为2-20个字符，phonenum必须为8-11字符 格式不正确时，界面有弹窗提示
    def add_customer(self, customer_info):
        self._open(self.url)
        self._click(self.add_customer_btn)
        self._input(self.new_name_box, txt=customer_info['name'])
        self._input(self.new_phonenum_box, txt=customer_info['phonenum'])
        self._input(self.new_address_box, txt=customer_info['address'])
        self._click(self.create_btn)

        result = dict()
        # 判断是否出现弹窗
        result['pop-up'] = self.check_pop_up()
        # 判断添加成功
        #  添加成功后，列表第一个就是添加的项
        if self.check_first_name() == customer_info['name']:
            result['flag'] = 1
        else:
            result['flag'] = 0
        return result

    def cancel_add_customer(self, input_info=True, customer_info=None):
        self._open(self.url)
        self._click(self.add_customer_btn)
        if input_info:
            self._input(self.new_name_box, txt=customer_info['name'])
            self._input(self.new_phonenum_box, txt=customer_info['phonenum'])
            self._input(self.new_address_box, txt=customer_info['address'])
        self._click(self.cancel_btn)
        return

    def search(self, content):
        self._open(self.url)
        self._input(self.search_box, txt=content)
        self._click(self.search_btn)
        name_list = self.list_search_result('name')
        for name in name_list:
            if content not in name:
                return False
        return True

    # 目前只检查了第一页的结果
    def list_search_result(self, key):
        result_list = list()
        item_count = len(self._find_all(self.customer_name_list))
        for index in range(item_count):
            if key == 'name':
                result_list.append(self._get_text(self.customer_name_list))
            if key == 'phonenum':
                result_list.append(self._get_text(self.customer_phonenum_list))
            if key == 'address':
                result_list.append(self._get_text(self.customer_address_list))
        return result_list

    # 检查第一个结果
    def check_first_name(self):
        return self._get_text(self.customer_name_1)

    # 检查弹窗提示
    def check_pop_up(self):
        if self._switch_to_alert():
            message = self._alert_txt()
            self._alert_accept()
            return message
        else:
            return False
