import rospy
import adafruit_bno055
from std_msgs.msg import 

from busio import I2C
from board import SDA, SCL

imui2c = I2C(SCL, SDA)

imu = adafruit_bno055.BNO055_I2C(imui2c)

def t():
        pub = rospy.Publisher('IMU_Data', ,queue_size = 10)
    


if __name__ == '__main__':
        talker()
