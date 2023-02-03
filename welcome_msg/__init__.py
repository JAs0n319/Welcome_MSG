from datetime import datetime
from mcdreforged.api.all import *

default_config = {
	'setting': {
		'StartDate': '1988-01-01',
		'Tell_Say': {
			'0': 'Say',
			'1': 'Tell'
		}
	},
	'text': {
		'0': '欢迎$PlayerName$进入服务器',
		'1': '今天是开服的第$Days$天'
	}
}

def sendMsg(server: ServerInterface,text: str,player: str,num: str):
	if player == 'Test_Player':
		server.broadcast(text)
	else:
		if config['setting']['Tell_Say'][num] == 'Say':
			server.say(text)
		elif config['setting']['Tell_Say'][num] == 'Tell':
			server.tell(player,text)
		else:
			server.say('配置文件错误,请联系管理员修改配置文件')

def get_the_days():

	if config['setting']['StartDate'] != '1988-01-01':
		days = datetime.now() - datetime.strptime(config['setting']['StartDate'],'%Y-%m-%d')
		return str(days.days)

	else:
		return '(没有找到有效日期)'

def decodeMsg(server: ServerInterface,player: str):

	for k in range(0,len(config['text'])):
		text = config['text'][str(k)]

		if text.find('$PlayerName$') != -1:
			text = text.replace('$PlayerName$',player)
		if text.find('$Days$') != -1:
			text = text.replace('$Days$',get_the_days())

		sendMsg(server,text,player,str(k))

def on_player_joined(server: PluginServerInterface,player: str,info: Info):
	decodeMsg(server,player)

def on_load(server: PluginServerInterface, old):

	global config
	global comm

	config = server.load_config_simple('config.json',default_config)
	comm = '!!joinMsg'

	server.register_help_message(comm,'展示欢迎消息')
	server.register_command(
		Literal(comm)
		.runs(lambda src: decodeMsg(server,'Test_Player'))
	)