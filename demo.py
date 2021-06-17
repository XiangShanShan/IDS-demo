#!/usr/bin/env python

import sys
import os
#import wget
import json
import time
#import process
import configparser


CONFIG_INI_URL = 'https://github.com/XiangShanShan/IDS-demo/blob/main/config.ini'
YAML_URL='https://github.com/XiangShanShan/IDS-demo/blob/main/wondersoft.yaml'
RULES_URL='https://github.com/XiangShanShan/IDS-demo/blob/main/rules/wondersoft.rules'

CONFIG_STAMP = 0
ARGVS=''


#当前文件位置
exec_dir = os.path.dirname(__file__)
config_ini_dir = os.path.join(exec_dir,"config.ini")




def init_check():
#
# 1. check all file,while missing download default 'config.ini'
#
# 1.1 config.ini
	if os.path.exists(config_ini_dir):
		pass
	else:
		print("missing config.ini,downlaod from \n",)
		wget.download(CONFIG_INI_URL,out=config_ini_dir)
		if os.path.exists(config_ini_dir):
			print('download faild')
			exit()	
		print(f"donwload config.ini successful, save as {config_ini_dir}" )
	
	try:
		config=ConfigParser()
		config.read('config.ini',encoding='UTF-8')
	except:
		print('config.ini misconfigured, please check again')	
		exit()

	print('---load config.ini successful,check yaml and rules next ---')

	#time stamp for content modifying
	CONFIG_STAMP = os.stat(config_ini_dir)

	# 1.2 wondersoft.yaml  
	yaml_dir=config.get('default','yaml')
	if os.path.exists(yaml_dir):
		print('default yaml ',yaml_dir)
	else:
		print('missing yaml')
		wget.download(YAML_URL,out=yaml_dir)
		if os.path.exists(yaml_dir):
			print('yaml init successful')
		else:
			print('missing yaml, program exiting')
			exit()

	# print(config.get('init','interface'))
	# wondersoft_yaml_default_dir = "/etc/wondersoft/wondersoft.yaml"
	
	# 1.3 test.rules
	rules_dir = config.get('default','rules')
	if os.path.exists(rules_default_dir):
		print('default yaml ',yaml)
	else:
		print('missing rules')
		wget.download(RULES_URL,out=rules)
		if os.path.exists(rules_dir)
			print('rules init successful')
		else:
			print('missing rules,program exiting')
			exit()
	return True



#	
# 2. argvs check
#

def argvs_check():
	try:
		config=ConfigParser()
		config.read('config.ini',encoding='UTF-8')
	except:
		print('config.ini misconfigured, please check again')	
		return False
	
	return True










#
# 3.suricata control 
#
def init_changed():
	

def is_running(procname):
	if os.system('pidof ' + procname):
		return True
	return False


# Termiat Process by name
def kill(processname):
	os.system(f'kill -9 $(pidof -s { processname })' )

# Start suricata with argvs
def start(procname):
	os.system(procname + ARGVS )


# exec()
def exec(procname):
	try:
		config=ConfigParser()
		config.read('config.ini',encoding='UTF-8')
	except:
		print('config.ini misconfigured, please check again')	
		exit()
	action=config.get('options','action')
	if action=='stop' && is_running(procname):
		kill(procname)
	else:
		print(f"stop program failed cause none {procname} found")
	if action=='start' && (! is_running(procname)):
		start(procname)



def main():
	init_check()
	while true:

		# config.ini modified
		if CONFIG_STAMP != os.stat(CONFIG_INI_URL).st_mtime:
			print('config.ini changed')
			exec('suricata')
			continue
		else:
			time.sleep(10)


if __name__ == '__main__':
	main()