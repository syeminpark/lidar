import serial
import time


line = 50    # 멀고 가깝고 기준
maxDist = 130  # 센서 벗어나는 거리

testCounter = 1
closeCounter = 1
farCounter = 1

send = True  # 유니티 인풋 default=False
reset = False
ser = serial.Serial("COM7", 115200)


# def checkUnity():
#     if():
#         send = True
#     else:
#         send = False


def getTFminiData():
    while True:
        # time.sleep(0.1)
        count = ser.in_waiting
        if count > 8:
            recv = ser.read(9)
            ser.reset_input_buffer()

            if recv[0] == 0x59 and recv[1] == 0x59:  # python3
                distance = recv[2] + recv[3] * 256
                strength = recv[4] + recv[5] * 256
                # print(distance)

                if(distance < maxDist):
                    if(distance > line):
                        global closeCounter
                        closeCounter += 1
                    else:
                        global farCounter
                        farCounter += 1

                # 테스트용. 차후에 지우셈

                global testCounter
                testCounter += 1
                if(testCounter > 500):
                    break

                # 대체물
                 # checkUnity()
                # if(send==False):
                    # break

                # print('(', distance, ',', strength, ')')
                ser.reset_input_buffer()


while __name__ == '__main__':
    try:
        if ser.is_open == False:

            ser.open()

        if(send == True):

            getTFminiData()
            reset = False
            send = False

        elif(send == False and reset == False):
            if(closeCounter > farCounter):
                result = "FAR"
            else:
                result = "CLOSE"
            reset = True
            send = True  # 지우셈
            print(result)  # 지우셈
            testCounter = 1
            closeCounter = 1
            farCounter = 1

    except KeyboardInterrupt:   # Ctrl+C
        if ser != None:
            ser.close()
