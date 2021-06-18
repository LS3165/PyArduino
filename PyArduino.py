import serial
import time
class Arduino:
    def __init__(self,baudrate=9600,COM='COMMMM'):
        self.serial = serial.Serial()
        # 初始化參數
        self.is_connected = False
        self.serial.baudrate = baudrate
        # 掃描並連接
        self.scan(baudrate,COM)
    def scan(self,baudrate=9600,COM='COMMMM'):
        print("-----------start scan-----------")
        self.is_connected = False
        # 將要掃描的 port 存至 COM 中
        if COM == 'COMMMM':
            COM = ['COM1','COM2','COM3','COM4','COM5','COM6','COM7','COM8','COM9','COM10','COM11','COM12','COM13','COM14','COM15','COM16','COM17','COM18']
        else:
            COM = [COM]
        # 初始化 baudrate
        self.serial.baudrate = baudrate
        for com in COM:
            try :
                # 設定要連接的 port 並嘗試連接
                self.serial.port = com
                self.serial.open()
                if self.serial.isOpen()==True:
                    self.is_connected = True
                    # 連接成功則離開迴圈
                    break
            except:
                pass
        if self.is_connected == True:
            # 印出裝置資訊
            print("connected")
            print("baudrate : " + str(self.serial.baudrate))
            print("COM : " +  self.serial.port)
        else:
            # 印出連接失敗
            print("unconnected")
        print("------------end scan------------")
    def write(self,str=''):
        # 沒有連接的裝置則直接回傳 "unconnected"
        if self.is_connected == False:
            return "unconnected"
        self.serial.write(bytes(str + '\n', encoding="utf-8"))
        # 傳送完畢就回傳 "Succeed to send message to Arduino"
        return "Succeed to send message to Arduino"
    def read(self,T=30):
        # 沒有連接的裝置則直接回傳 "unconnected"
        if self.is_connected == False:
            return "unconnected"
        # 先記錄當前時間
        now_T = time.time()
        while time.time() - now_T < T:
            # 在一定時間內都一直去嘗試接收資料
            if self.serial.in_waiting:
                data = self.serial.readline()
                data = data.decode()
                # 成功接手資料則回傳
                return data.split('\n')[0]
        # 超過時間後皆無資料，回傳 "TLE"
        return "TLE"