from base.base_page import BasePage


class OrderPage(BasePage):
    customer_name = '医院'
    add_order_btn = ('xpath', '//button[text()="添加" and "订单"]')
    new_order_name_box = ('xpath', '//div[text()="订单名称"]/input')
    customer_select = ('xpath', f'//div[text()="客户"]/select')
    customer_tag = ('xpath', '//div[text()="客户"]/span')
    medicine_select = ('xpath', f'//div[text()="药品（数量）："]/select')
    medicine_tag = ('xpath', f'//div[text()="药品（数量）："]/div/span[contains(@style,"inline-block")]')
    medicine_count = ('xpath', '')

    def add_order(self, order_info):
        self._click(self.add_order_btn)
        self._input(self.new_order_name_box, txt=order_info['order_name'])
        self._select_option_by_text(self.customer_select, txt=order_info['customer_name'])
        assert self.check_tag(self.customer_tag) == order_info['customer_name']
        for medicine in order_info['medicines']:
            self._select_option_by_text(self.customer_select, txt=order_info['customer_name'])

    def check_tag(self, tag):
        txt = self._get_text(tag)
        return txt if txt else False
