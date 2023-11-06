from datetime import datetime
import random
from mcdreforged.api.all import *

default_config = {
	"setting": {
		"StartDate": "1988-01-01",
	},
	"text": {
		"0": ["ToAll","欢迎$PlayerName$进入服务器","欢迎$PlayerName$~"],
		"1": ["ToPlayer","今天是开服的第$Days$天","今天是开服的第$Days$天"],
	},
	"ErrorMessage": "配置错了，通知一下腐竹吧"
}

def sendMsg(server: ServerInterface,text: str,player: str,num: str):

	if player == "Test_Player":
		server.broadcast(text)
	elif config["text"][num][0] == "ToPlayer":
		server.say(text)
	elif config["text"][num][0] == "ToAll":
		server.tell(player,text)
	else:
		server.say(config["ErrorMessage"])

def get_the_days():

	days = datetime.now() - datetime.strptime(config['setting']['StartDate'],'%Y-%m-%d')
	return str(days.days)

def decodeMsg(server: ServerInterface,player: str):

	date = get_the_days()
	randomNumber = int(random.randint(2,len(config["text"]['0'])))

	for k in range(0,len(config["text"])):

		text = config["text"][str(k)][randomNumber-1]

		text = text.replace('$PlayerName$',player)		
		text = text.replace('$Days$',date)

		sendMsg(server,text,player,str(k))

def on_player_joined(server: PluginServerInterface,player: str,info: Info):

	decodeMsg(server,player)

def on_load(server: PluginServerInterface, old):

	global config
	global comm

	config = server.load_config_simple("config.json",default_config)
	comm = "!!joinMsg"

	server.register_help_message(comm,"展示欢迎消息")
	server.register_command(
		Literal(comm)
		.runs(lambda src: decodeMsg(server,"Test_Player"))
	)