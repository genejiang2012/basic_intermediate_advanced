# # -*-coding:utf-8-*-
# # Time:2017/7/1-0:18
# # Author:YangYangJun
# from selenium import webdriver
# from email.mime.multipart import MIMEMultipart
# import baseinfo
# from email.mime.text import MIMEText
# from email.header import Header
# from HTMLTestRunner import HTMLTestRunner
# import os
# import time
# import unittest
# import smtplib
# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf8')
#
#
# def get_NewReport(testreport):
#     # 获取testreport 目录下的文件返回一个list
#     dirs = os.listdir(testreport)
#     # 对文件list 进行排序 进行增序排列
#     dirs.sort()
#     # 获取序列最后一个元素，即最大的一个元素。
#     newreportname = dirs[-1]
#     print('The new report name: {0}'.format(newreportname))
#     file_new = os.path.join(testreport, newreportname)
#     print file_new
#     return file_new
#
#
# def get_Result(filename):
#     driver = webdriver.Firefox()
#     driver.maximize_window()
#     # 得到测试报告路径
#     result_url = "file_concept://%s" % filename
#     driver.get(result_url)
#     time.sleep(5)
#
#     result = driver.find_element_by_xpath("html/body/div[1]/p[3]").text
#
#     result = result.split(':')
#     print result
#     driver.quit()
#     return result[-1]
#
#
# def send_Mail(file_new, result):
#     f = open(file_new, 'rb')
#     # 读取测试报告正文
#     mail_body = f.read()
#     f.close()
#     try:
#         smtp = smtplib.SMTP(baseinfo.Smtp_Server, 25)
#         sender = baseinfo.Smtp_Sender
#         password = baseinfo.Smtp_Sender_Password
#         receiver = baseinfo.Smtp_Receiver
#         smtp.login(sender, password)
#         msg = MIMEMultipart()
#         # 编写html类型的邮件正文，MIMEtext()用于定义邮件正文
#         # 发送正文
#         text = MIMEText(mail_body, 'html', 'utf-8')
#         # 定义邮件正文标题
#         text['Subject'] = Header('XXXXUI自动化测试报告', 'utf-8')
#         msg.attach(text)
#         # 发送附件
#         # Header()用于定义邮件主题，主题加上时间，是为了防止主题重复，主题重复，发送太过频繁，邮件会发送不出去。
#         msg['Subject'] = Header(
#             '[执行结果：' + result + ']' + 'XXXXUI自动化测试报告' + now, 'utf-8')
#         msg_file = MIMEText(mail_body, 'html', 'utf-8')
#         msg_file['Content-Type'] = 'application/octet-stream'
#         msg_file["Content-Disposition"] = 'attachment; filename="TestReport.html"'
#         msg.attach(msg_file)
#         # 定义发件人，如果不写，发件人为空
#         msg['From'] = sender
#         # 定义收件人，如果不写，收件人为空
#         msg['To'] = ",".join(receiver)
#         tmp = smtp.sendmail(sender, receiver, msg.as_string())
#         print tmp
#         smtp.quit()
#         return True
#     except smtplib.SMTPException as e:
#         print(str(e))
#         return False
#
#
# if __name__ == '__main__':
#     # test_dir = os.path.join(os.getcwd(),'test_case')
#     # print(test_dir)
#     # report_dir = os.path.join(os.getcwd(),'test_report')
#     # 测试用例路径
#     test_dir = baseinfo.test_dir
#     # est_dir = os.path.join(os.getcwd(),'test_case')
#
#     # print(test_dir)
#     # report_dir = os.path.join(os.getcwd(),'test_report')
#     # 测试报告存放路径
#     report_dir = baseinfo.test_report
#
#     test_discover = unittest.defaultTestLoader.discover(
#         test_dir, pattern='test*.py')
#     now = time.strftime("%Y-%m-%d-%H_%M_%S")
#     filename = report_dir + 'result-' + now + '.html'
#     print filename
#     fp = open(filename, 'wb')
#     runner = HTMLTestRunner(
#         stream=fp, title='XXXXUI自动化测试报告', description='用例执行情况')
#     runner.run(test_discover)
#     fp.close()
#     # 其实根本不需要这里获取最新报告，filename就是最新的报告了，可以直接使用了
#     #new_report = get_NewReport(report_dir)
#     result = get_Result(filename)
#
#     mail = send_Mail(filename, result)
#
#     print mail
#     if mail:
#         print(u"邮件发送成功！")
#     else:
#         print(u"邮件发送失败！")
