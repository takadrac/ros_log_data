#!/usr/bin/env python
# coding: UTF-8
import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher('chatter1', String, queue_size=10)
	rospy.init_node('talker1', anonymous=True)
	r = rospy.Rate(1)
	msg = String()
	while not rospy.is_shutdown():
		str = "hello world! my name is talker1."
		msg.data = str
		rospy.loginfo(msg)
		pub.publish(msg)
		r.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException: pass