#!/usr/bin/env python
# coding: UTF-8
import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher('chatter', String, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	r = rospy.Rate(2)
	while not rospy.is_shutdown():
		str = "hello world! %s"%rospy.get_time()
		rospy.loginfo(str)
		pub.publish(str)
		r.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException: pass