@echo off
pytest TestCases/test_login.py -v --html=Reports/report.html --self-contained-html
pytest TestCases/test_leave.py -v --html=Reports/report.html --self-contained-html
pytest TestCases/test_logout.py -v --html=Reports/report.html --self-contained-html