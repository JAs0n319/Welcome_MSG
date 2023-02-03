# Welcome_MSG
[English](./README.md)
[中文](./README_zh_cn.md)
### 发送欢迎消息

# welcome_msg.json

```
{
    "setting": {                          
        "StartDate": "1988-01-01",        // 开服日期 如果不更改会导致消息中含有报错消息
        "Tell_Say": {                     // 消息可见范围设置
            "0": "Say",                   // Say = 全部玩家
            "1": "Tell"                   // Tell = 加入的玩家
        }
    },
    "text": {
        "0": "欢迎$PlayerName$进入服务器", // $PlayerName$ $Days$ 这两个可以任意更改位置
        "1": "今天是开服的第$Days$天"
    }
}
```
