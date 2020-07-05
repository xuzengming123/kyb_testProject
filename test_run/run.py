from BSTestRunner import BSTestRunner
import unittest,time,logging,sys
path = 'E:\kyb_testProject'
sys.path.append(path)

#指定测试用例和测试报告的路径
test_dir = '../test_case'
report_dir = '../reports'

#加载测试用例
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py')

#运行用例并生成测试报告
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_name = report_dir+'/'+now+' test_report.html'
with open(report_name,'wb') as f:
    runner = BSTestRunner(stream=f,title='Kyb Test Report',description='kyb Android app test report')
    logging.info('start run test case...')
    runner.run(discover)