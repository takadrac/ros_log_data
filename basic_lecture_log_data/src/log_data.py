#!/usr/bin/env python
# coding: UTF-8
import rospy
import std_msgs
import basic_lecture
from std_msgs.msg import String
from basic_lecture.msg import Msg
import numpy as np
import csv


a = [0, 0, 0]
b = []

def callback_str(data):
	#print(type(data))
	#rospy.loginfo(rospy.get_caller_id()+"I heard %s", data.data)
	
	#print(rospy.get_caller_id()+"I heard %s", data.data)
	return data.data

def callback_num(msg):
	#print('subscribe x=%d y=%d'%(msg.x, msg.y))
	#print(type(msg))
	x, y = msg.x*10, msg.y*10
	'''
	pub = rospy.Publisher('output_data', Msg, queue_size=100)
	r = rospy.Rate(1)
	msg = Msg()
	#while not rospy.is_shutdown():
	msg.x = x
	msg.y = y
	pub.publish(msg)
	print('output x=%d y=%d'%(msg.x, msg.y))
	r.sleep()
	'''
	return x, y

def callback(msg, id):
	c = ()
	if type(msg) == std_msgs.msg._String.String:
		val = callback_str(msg)
		#str_ = msg.data
	elif type(msg) == basic_lecture.msg._Msg.Msg:
		val = callback_num(msg)
		#x, y = msg.x, msg.y
	#print(id, val)
	a[id] = val
	print(a)
	c = tuple(a)
	b.append(c)
	if rospy.is_shutdown():
		print(b)
		#np.save('test.npy', b)

def sub():
	rospy.init_node("data_logger", anonymous=True)
	rospy.Subscriber("chatter", String, callback, callback_args=0)
	rospy.Subscriber("chatter1", String, callback, callback_args=1)
	rospy.Subscriber("input_data", Msg, callback, callback_args=2)
	#print(rospy.Subscriber("input_data", Msg, callback_num))
	rospy.spin()

def logger():
	pub = rospy.Publisher('log_msgs', Msg, queue_size=10)
	r = rospy.Rate(10)
	while not rospy.is_shutdown():
		str = ""
		rospy.loginfo(str)
		pub.publish(str)
		r.sleep()


if __name__ == '__main__':
	sub()
	print(b)
	with open('test.csv','wb') as fout:
		writer = csv.writer(fout, delimiter=',') 
		writer.writerows(b)