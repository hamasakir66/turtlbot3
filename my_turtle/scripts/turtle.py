#!/usr/bin/python
# coding: UTF-8

import rospy
import random
import time
from move_base_msgs.msg import MoveBaseActionGoal
from geometry_msgs.msg import Twist

class RobotController:
    def __init__(self):
        rospy.init_node('topic_publisher')
        self.pub = rospy.Publisher('/move_base/goal', MoveBaseActionGoal, queue_size=1)
        self.sub = rospy.Subscriber('/cmd_vel', Twist, self.callback)
        self.flag = 0

        self.twi = Twist()
        self.number = [0, 1, 2, 3, 4, 5, 6, 7]
        self.goal_x = [2.0, 2.0, 0.5, -0.5, -2.0, -2.0, -0.5, 0.5]
        self.goal_y = [-0.5, 0.5, 2.0, 2.0, 0.5, -0.5, -2.0, -2.0]

        while not rospy.is_shutdown():
            self.flag = 1
            num = random.choice(self.number)
            
            while self.flag == 1:
                self.publish_target(num)
                time.sleep(5)
                print(self.flag)

    def publish_target(self, num):
        target = MoveBaseActionGoal()
        target.goal.target_pose.header.frame_id = "map"
        target.goal.target_pose.pose.position.x = self.goal_x[num]
        target.goal.target_pose.pose.position.y = self.goal_y[num]
        target.goal.target_pose.pose.orientation.w = 0.8
        target.header.stamp = rospy.Time.now()
        target.goal.target_pose.header.stamp = rospy.Time.now()
        self.pub.publish(target)

    def callback(self, msg):
        lin_x = msg.linear.x
        lin_y = msg.linear.y
        lin_z = msg.linear.z
        ang_x = msg.angular.x
        ang_y = msg.angular.y
        ang_z = msg.angular.z

        if lin_x == 0 and lin_y == 0 and lin_z == 0 and ang_x == 0 and ang_y == 0 and ang_z == 0:
            self.flag = 0
        else:
            self.flag = 1

if __name__ == '__main__':
    controller = RobotController()
    rospy.spin()
