#!/usr/bin/env python3
"""
Python node to implement a random autonomous motion of Turtlebot3 using move_base package

Subscriber:
topic : /odom Message Type : nav_msgs/Odometry

Client:

topic : move_base Message Type : move_base_msgs/MoveBaseAction
"""



import rospy
import actionlib
from actionlib_msgs.msg import GoalStatus
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from nav_msgs.msg import Odometry, OccupancyGrid, MapMetaData
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import random




class MovetoGoal:
    """
    Send random goal directions using move_base by subscribing to /odom topic
    """

    def __init__(self):
        """
        Implement SimpleActionClient to constantly send goals
        """

        rospy.init_node("navigation")
        self.odometry = rospy.Subscriber("/odom", Odometry, self.odom_callback)
        self.client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        self.client.wait_for_server()
        
        while not rospy.is_shutdown():
            self.random_x = random.uniform(-1, 1)
            self.random_y = random.uniform(-1, 1)
            self.goal = MoveBaseGoal()
            self.goal.target_pose.header.frame_id = "map"
            self.goal.target_pose.header.stamp = rospy.Time.now()
            self.goal.target_pose.pose.position.x = self.x + self.random_x
            self.goal.target_pose.pose.position.y = self.y + self.random_y
            self.goal.target_pose.pose.orientation.w = 1
            self.client.send_goal(self.goal)
            self.client.wait_for_result()
            self.client.get_result()

            if(self.client.get_state() == GoalStatus.SUCCEEDED):
                rospy.loginfo("Robot moves to the goal")
            else:
                rospy.loginfo("Robot fails to move to the goal")


    def odom_callback(self, data):
        """
        function gives position of the robot relative to the map coordinates
        """

        self.x = data.pose.pose.position.x
        self.y = data.pose.pose.position.y

    


if __name__ == "__main__":

    n = MovetoGoal()
    rospy.spin()