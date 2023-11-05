#!/usr/bin/python
# coding: UTF-8

import rospy
import random
import time
from move_base_msgs.msg import MoveBaseActionGoal
from geometry_msgs.msg import Twist

rospy.init_node('topic_publisher')

twi=Twist()

number=[0,1,2,3,4,5,6,7]
goal_x=[2.0,2.0,0.5,-0.5,-2.0,-2.0,-0.5,0.5]
goal_y=[-0.5,0.5,2.0,2.0,0.5,-0.5,-2.0,-2.0]

flag = 0

def callback(msg):
    global flag
    lin_x=msg.linear.x
    lin_y=msg.linear.y
    lin_z=msg.linear.z
    ang_x=msg.angular.x
    ang_y=msg.angular.y
    ang_z=msg.angular.z

    # print(lin_x)
    # print(lin_x)
    # print(lin_z)
    # print(ang_x)
    
    if lin_x==0 and lin_y==0 and lin_z==0 and ang_x==0 and ang_y==0 and ang_z==0:
        flag=0
        if lin_x==0 and lin_y==0 and lin_z==0 and ang_x==0 and ang_y==0 and ang_z==0:
            flag=0
    else:
        flag=1
   
    return flag
 

pub = rospy.Publisher('/move_base/goal', MoveBaseActionGoal, queue_size=1)


target=MoveBaseActionGoal()

while not rospy.is_shutdown():
    global flag
    flag=1
    num=random.choice(number)
    
    while flag ==1:
        target.goal.target_pose.header.frame_id = "map"
        target.goal.target_pose.pose.position.x = goal_x[num]
        target.goal.target_pose.pose.position.y = goal_y[num]
        target.goal.target_pose.pose.orientation.w = 0.8
        target.header.stamp = rospy.Time.now()
        target.goal.target_pose.header.stamp = rospy.Time.now()
        pub.publish(target)
        sub = rospy.Subscriber('/cmd_vel',Twist,callback)
        time.sleep(5)
        print(flag)



rospy.spin()
