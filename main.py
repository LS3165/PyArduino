from PyArduino import Arduino
A = Arduino()
# A = Arduino(300)
# A = Arduino(4800,"COM3")
# A = Arduino(baudrate=4800)
# A = Arduino(COM="COM3")
# A = Arduino(baudrate=4800,COM="COM3")
A.scan()
# A.scan(300)
# A.scan(4800,"COM3")
# A.scan(baudrate=4800)
# A.scan(COM="COM3")
# A.scan(baudrate=9600,COM="COM3")
print("baudrate :" + str(A.serial.baudrate))
print("port :" + A.serial.port)
print("is_connected :" + str(A.is_connected))
print(A.write("Hello World"))
print("read from Arduino :" + A.read())
print(A.write("4578"))
print("read from Arduino :" + A.read())

A.scan(COM="COM18")
print(A.write("Hello World"))
print("read from Arduino :" + A.read())
print(A.write("4578"))
print("read from Arduino :" + A.read())