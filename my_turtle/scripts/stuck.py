#!/usr/bin/python
# coding: UTF-8

import rospy
import random
import time
from move_base_msgs.msg import MoveBaseActionGoal
from move_base_msgs.msg import MoveBaseActionFeedback
from geometry_msgs.msg import Twist


class RobotController:
    def __init__(self):
        rospy.init_node('topic_publisher')
        self.start_time = None
        self.stop_time = None
        self.stop_duration = 10.0 
        self.cur_pos_x = 0.0
        self.cur_pos_y = 0.0
        self.flag = 0
        self.twi = Twist()
        self.number = [0, 1, 2, 3, 4, 5, 6, 7]
        self.goal_x = [2.0, 2.0, 0.5, -0.5, -2.0, -2.0, -0.5, 0.5]
        self.goal_y = [-0.5, 0.5, 2.0, 2.0, 0.5, -0.5, -2.0, -2.0]
        self.goal_value_x = None
        self.goal_value_y = None
        self.pub = rospy.Publisher('/move_base/goal', MoveBaseActionGoal, queue_size=1)
        self.sub = rospy.Subscriber('/move_base/feedback', MoveBaseActionFeedback, self.cheking)
        self.sub = rospy.Subscriber('/cmd_vel', Twist, self.callback)     
        
        
        while not rospy.is_shutdown():
            self.flag = 1
            num = random.choice(self.number)

            while self.flag == 1:
                self.publish_target(num)
                time.sleep(5)
                print(self.flag)
          # stuck   
            if self.flag == 2:
                self.stuck()
            elif self.flag == 0:
                pass


    def publish_target(self, num):
        self.goal_value_x = self.goal_x[num]
        self.goal_value_y = self.goal_y[num]
        target = MoveBaseActionGoal()
        target.goal.target_pose.header.frame_id = "map"
        target.goal.target_pose.pose.position.x = self.goal_x[num]
        target.goal.target_pose.pose.position.y = self.goal_y[num]
        target.goal.target_pose.pose.orientation.w = 0.8
        target.header.stamp = rospy.Time.now()
        target.goal.target_pose.header.stamp = rospy.Time.now()
        self.pub.publish(target)

    def cheking(self,msg):
        self.cur_pos_x = msg.feedback.base_position.pose.position.x 
        self.cur_pos_y = msg.feedback.base_position.pose.position.y 

    def callback(self, msg):
        lin_x = msg.linear.x
        lin_y = msg.linear.y
        lin_z = msg.linear.z
        ang_x = msg.angular.x
        ang_y = msg.angular.y
        ang_z = msg.angular.z

        if lin_x == 0 and lin_y == 0 and lin_z == 0 and ang_x == 0 and ang_y == 0 and ang_z == 0:
            current_time = rospy.Time.now() 
            #print(self.cur_pos_x)
            #print(self.goal_value_x)
            if abs(self.cur_pos_x - self.goal_value_x) >= 0.5 or abs(self.cur_pos_y - self.goal_value_y) >= 0.5:
                self.flag = 2 # stuck posibility 
                self.start_time = rospy.Time.now() 
            else:
                self.flag = 0 # goal 
        else:
            self.flag = 1
    
    def stuck(self):
        while self.flag == 2:
            current_time  = rospy.Time.now()
            if (current_time - self.start_time).to_sec() > self.stop_duration:
                self.recover()

    def recover(self):
        self.twi.linear.x = -0.2
        self.pub.publish(self.twi)
        time.sleep(3)
        stop_cmd = Twist()
        self.pub.publish(stop_cmd)

        # to create new goal
        self.flag = 1
       

if __name__ == '__main__':
    controller = RobotController()
    rospy.spin()
