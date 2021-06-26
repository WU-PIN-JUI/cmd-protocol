# cmd-protocol
## 簡介
- **你可以直接在瀏覽器使用cmd指令！**

## 使用說明 - 建置


1. 下載code
2. 開啟cmd protocol.reg
3. 一路點選是、確定
4. 將protocol.exe放到C:\Windows\system32
- 或者使用指令進行
  >使用系統管理員 - cmd
  >```batch
  >cd cmd-protocol
  >xcopy protocol.exe C:\Windows\system32\protocol.exe
  >```

5. 恭喜完成！py原始碼，可刪除


## 使用說明 - 使用
1. 開啟你的瀏覽器
2. 在網址欄輸入cmd://(command)/
3. 點選「開啟protocol.exe」
4. 彈出視窗會提示輸入網址、指令
5. 選擇Y確認執行

## Bug

- [x] 代表已修正
- [ ] 代表未修正

- [x] 無法使用參數
- [ ] 無法輸入中文字
- [x] 無法使用\符號(有用到目錄的無法使用，將盡快修正)

## python原始程式
```python
import sys
import os

URL = sys.argv[1]
commands = URL.split('//')
command_tmp = commands[1]
t22 = command_tmp[len(command_tmp) - 1]
if t22 == "/":
    command_tmp2 = command_tmp[:-1]
else:
    command_tmp2 = command_tmp
command = command_tmp2.replace('%20', ' ')

print("     URL = " + URL)

print("     command = " + command)
a = 1
while a == 1:
    start = input("Are you sure you want to execute[Y/N]")
    if start=="Y":
        if URL=="cmd:///":
            os.system("cmd")
            exit()
        os.system("cmd /c " + command)
        exit()
    if start=="y":
        if URL=="cmd:///":
            os.system("cmd")
            exit()
        os.system("cmd /c " + command)
        exit()
    elif start=="N":
        exit()
    elif start=="n":
        exit()
    else:
        print("Wrong input")
```
