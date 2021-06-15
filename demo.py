#!/usr/bin/env python
import sys
import os
# import wget
from configparser import ConfigParser


#
# 1. check all file,while missing download default 'config.ini'
#

CONFIG_INI_URL = 'https://github.com/XiangShanShan/IDS-demo/blob/main/config.ini'
YAML_URL='https://github.com/XiangShanShan/IDS-demo/blob/main/wondersoft.yaml'
RULES_URL='https://github.com/XiangShanShan/IDS-demo/blob/main/rules/wondersoft.rules'



# 1.1 config.ini

exec_dir = os.path.dirname(__file__)
config_ini_dir = os.path.exists(os.path.join(exec_dir,"config.ini"))

'''
if config_ini_dir:
	print("find")
else:
	print("missing config.ini,downlaod from \n",)
	wget.download(url,out=config_ini_dir)
	if config_ini_dir:
		print('download faild')
	else:
		print(f"donwload config.ini successful, save as {config_ini_dir}" )

'''

if config_ini_dir:
	config=ConfigParser()
	config.read('config.ini',encoding='UTF-8')
	

	# 1.2 wondersoft.yaml  
	yaml=config.get('init','yaml')
	if yaml && os.path.exists(yaml):
		print('default yaml ',yaml)
	else:
		print('missing yaml')
		wget.download(YAML_URL,out=yaml)

	# print(config.get('init','interface'))
# wondersoft_yaml_default_dir = "/etc/wondersoft/wondersoft.yaml"
	# 1.3 test.rules
	wondersoft_rules_default_dir = "/etc/wondersoft/rules"
	rules = config.get('init','rules')
	if rules && os.path.exists(yaml):
		print('default yaml ',yaml)
	else:
		print('missing yaml')
		wget.download(rules,out=rules)



#
# 2.start suricata 
#