#!/usr/bin/env python
# coding: UTF-8
import rospy
#from std_msgs.msg import String
from basic_lecture.msg import Msg

def talk():
    pub = rospy.Publisher('input_data', Msg, queue_size=100)
    #print('*** Publisher ***')
    r = rospy.Rate(5)
    x = 0
    y = 2
    msg = Msg()
    while not rospy.is_shutdown():
        msg.x = x
        msg.y = y
        pub.publish(msg)
        print('publish x=%d y=%d'%(msg.x, msg.y))
        x += 1
        y += 1
        r.sleep()

def main():
    rospy.init_node('talker_num', anonymous=True)
    try:
        talk()
    except rospy.ROSInterruptException: pass

if __name__ == '__main__':
    main()