# Welcome_MSG
### Send welcome message to player

# welcome_msg.json

```
{
    "setting": {                          
        "StartDate": "1988-01-01",        // If don't change will cause error message in text 
        "Tell_Say": {                     // msg visiable range
            "0": "Say",                   // Say = All Player
            "1": "Tell"                   // Tell = The Plyer who join
        }
    },
    "text": {
        "0": "欢迎$PlayerName$进入服务器", // $PlayerName$ $Days$ can be change the place
        "1": "今天是开服的第$Days$天"
    }
}
```
