import time

import pytest

from common.file_handler import path_create

if __name__ == '__main__':
    report_dir = path_create('E:/result/report/')
    allure_dir=path_create(report_dir+'/allure')
    report_name = f'{report_dir}{time.strftime("%Y-%m-%d-%H%M%S")}.html'

    #### byhy ####
    # pytest.main(['-v','-s','./byhy_cases/test_sign.py'])
    # pytest.main(['-v', '-s', './byhy_cases/'])

    # pytest.main(['-s', '-v', f'--html={report_name}', './byhy_cases/test_sign.py'])
    # pytest.main(['-s', '-v', f'--html={report_name}', './byhy_cases/test_customer.py'])

    pytest.main(['-s', '-v', f'--html={report_name}', './qingflow/test_index.py'])

    # 暂时不看
    # pytest.main(['-s', '-v', f'alluredir {allure_dir}', './qingflow/test_index.py'])
