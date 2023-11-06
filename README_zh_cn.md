# Welcome_MSG
[English](./README.md)
### 发送欢迎消息
### Ver1.2.0 -> 随机发送欢迎信息

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
#### · "text" 下每一项的数量需相同。
#### · 保留词有且仅有 \$PlayerName$ 与 \$Days$。