# kyb_testProject
app:测试包管理
baseView:该模块封装了一个类baseView，该类封装最基本的方法，比如：初始化driver__init__(self,driver)\find_element(s)\get_window_size()\swipe()
common:封装公共方法类：Common该类给业务模块进行继承调用其中的方法，比如：driver驱动封装\测试用例执行前后操作配置，封装为StartEnd类
businessView:存放业务逻辑模块
config:用于存放配置文件
data:数据文件,用于数据驱动
logs:日志文件
reports:测试报告文件
screenshots:存放截图文件
test_case:存放测试类的模块
test_run:执行自动化测试用例
