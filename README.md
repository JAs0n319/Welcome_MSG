# Welcome_MSG
[中文](./README_zh_cn.md)
### Send welcome message to player
### Ver1.2.0 -> Random sending welcomemessage

## welcome_msg.json

```
{
	"setting": {
		"StartDate": "1988-01-01",
	},
	"text": {
		"0": ["ToAll","欢迎$PlayerName$进入服务器","欢迎$PlayerName$~"],
		"1": ["ToPlayer","今天是开服的第$Days$天","今天是开服的第$Days$天"],
	},
	"ErrorMessage": "配置错了，通知一下腐竹吧"
}
```
#### · Number of any term of "text" must be same.
#### · Reserved word are \$PlayerName$ and \$Days$, Don't use it.