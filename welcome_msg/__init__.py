from datetime import datetime
from mcdreforged.api.all import *

default_config = {
    "StartDate": "1988-01-01",
    "N": 8,
    "NameColor": "§d",
    "DateColor": "§d",
    "1": "§f欢迎 ",
    "2": "*PlayerName*",
    "3": " §f进入服务器",
    "4": "*Send*",
    "5": "§f这是开服的第 ",
    "6": "*StartDate*",
    "7": " §f天",
    "8": "*Send*"
}

global text

def sendOut(server: ServerInterface,PlayerName):
	global text
	if PlayerName != '***Test***':
		server.broadcast(text)
		text = ''
	else:
		server.tell(PlayerName,text)
		text = ''

def sendMsg(server: ServerInterface,PlayerName):
	global text
	text = ''
	for i in range(1,int(config['N'])+1):
		k = str(i)
		if config[k] == '*Send*':
			sendOut(server,text)
		elif config[k] == '*StartDate*':
			if config['StartDate'] != '1988-01-01':
				StartDate = config['StartDate']
			else:
				StartDate = '(NULL)'
			if StartDate == '(NULL)':
				text += config['DateColor']
				text += StartDate
			else:
				end = datetime.now()
				start = datetime.strptime(StartDate,'%Y-%m-%d')
				dif = end-start
				text += config['DateColor']
				text += str(dif.days)
		elif config[k] == '*PlayerName*':
			text += config['NameColor']
			text += PlayerName
		else:
			text += config[k]

def on_player_joined(server: PluginServerInterface,player,info):
	sendMsg(server,player)

def on_load(server: PluginServerInterface, old):
	global config
	config = server.load_config_simple('welcome_msg.json',default_config)
	server.register_help_message('!!joinMsg','展示欢迎消息')
	server.register_command(
		Literal('!!joinMsg')
		.runs(lambda src: sendMsg( src.get_server() , '***Test***' ))
	)