#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped

def publish_initial_pose():
    rospy.init_node('initial_pose_publisher')
    pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size=10)

    pose_msg = PoseWithCovarianceStamped()
    pose_msg.header.frame_id = "map"
    pose_msg.pose.pose.position.x = -2.0
    pose_msg.pose.pose.position.y = -0.5
    pose_msg.pose.pose.position.z = 0.0
    pose_msg.pose.pose.orientation.x = 0.0
    pose_msg.pose.pose.orientation.y = 0.0
    pose_msg.pose.pose.orientation.z = 0.0
    pose_msg.pose.pose.orientation.w = 1.0

    rospy.sleep(1)
    pub.publish(pose_msg)

if __name__ == '__main__':
    try:
        publish_initial_pose()
    except rospy.ROSInterruptException:
        pass
