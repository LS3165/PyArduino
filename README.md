# PyArduino
下載 main.py 與 PyArduino.py 並放入相同的路徑中(main.py 只是範例，若無需使用範例程式，則下載 PyArduino.py 即可)
## PyArduino.py
Arduino Object 中有以下功能與參數可使用
### 建構式(有三種類型)
```python
#第一種，無參數
# baudrate 預設為 9600，port 會從 COM1 至 COM18 依序去查看是否連接並連接第一個能連接的裝置
A = Arduino()

#第二種，填寫參數
# baudrate 設定為 4800，port 會從 COM1 至 COM18 依序去查看是否連接並連接第一個能連接的裝置
A = Arduino(4800)
# baudrate 設定為 4800，port 嘗試連接 COM3 的裝置
A = Arduino(4800,"COM3")

#第三種，指定參數
# baudrate 設定為 300，port 會從 COM1 至 COM18 依序去查看是否連接並連接第一個能連接的裝置
A = Arduino(baudrate=300)
# baudrate 預設為 9600，port 嘗試連接 COM3 的裝置
A = Arduino(COM="COM3")
# baudrate 設定為 300，port 嘗試連接 COM3 的裝置
A = Arduino(baudrate=300,COM="COM3")
```

### Object 中的參數
```python
#A.serial.baudrate 為當前連接裝置的 baudrate，type 為 int
print("baudrate :" + str(A.serial.baudrate))

#A.serial.port 為當前連接裝置的 port，type 為 str
print("port :" + A.serial.port)

#A.is_connected 為是否有連接上裝置，type 為 boolen
print("is_connected :" + str(A.is_connected))
```

### scan(有三種類型)
**進行掃描並連接

開始掃描後，會印出 "-----------start scan-----------"

結束掃描，則會印出 "------------end scan------------"

若成功發送，會印出 "connected" 以及 baudrate 和 port 的資訊

未成功連接，則會回傳 "unconnected"

```python
#第一種，無參數
# baudrate 預設為 9600，port 會從 COM1 至 COM18 依序去查看是否連接並連接第一個能連接的裝置
A.scan()

#第二種，填寫參數
# baudrate 設定為 4800，port 會從 COM1 至 COM18 依序去查看是否連接並連接第一個能連接的裝置
A.scan(4800)
# baudrate 設定為 4800，port 嘗試連接 COM3 的裝置
A.scan(4800,"COM3")

#第三種，指定參數
# baudrate 設定為 300，port 會從 COM1 至 COM18 依序去查看是否連接並連接第一個能連接的裝置
A.scan(baudrate=300)
# baudrate 預設為 9600，port 嘗試連接 COM3 的裝置
A.scan(COM="COM3")
# baudrate 設定為 300，port 嘗試連接 COM3 的裝置
A.scan(baudrate=300,COM="COM3")
```

### write
**傳送字串給已連接的 Arduino 裝置

若成功發送，會回傳 "Succeed to send message to Arduino"

未連接裝置，則會回傳 "unconnected"
```python
#傳送空字串(長度為0)
A.write()
#傳送 aa4578 此字串
A.write("aa4578")
```

### read
**一定時間內接收從 Arduino 中發送的訊息

若成功接收，會回傳接收到的字串

未連接裝置，會回傳 "unconnected"

時間內皆未收到資料，則回傳 "TLE"
```python
#嘗試在 30 秒內(時間會有些微的誤差，例如 30.0014564)接收資料
print(A.read())
#嘗試在 10 秒內(時間會有些微的誤差，例如 10.0014564)接收資料
print(A.read(10))
```
