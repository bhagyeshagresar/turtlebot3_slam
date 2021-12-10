#!/usr/bin/env python3


import rospy
import actionlib
from actionlib_msgs.msg import GoalStatus
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from nav_msgs.msg import Odometry, OccupancyGrid, MapMetaData
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import random




class MovetoGoal:

    def __init__(self):

        rospy.init_node("navigation")
        self.odometry = rospy.Subscriber("/odom", Odometry, self.odom_callback)
        # self.laser = rospy.Subscriber("/scan", LaserScan, self.laser_callback)
        # self.map = rospy.Subscriber("/map", MapMetaData, self.map_callback)
        self.client = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        self.client.wait_for_server()
        
        while not rospy.is_shutdown():
            self.random_x = random.random()
            self.random_y = random.random()
            self.goal = MoveBaseGoal()
            #goal should be position and orientation specified in rviz    
            self.goal.target_pose.header.frame_id = "map"
            self.goal.target_pose.header.stamp = rospy.Time.now()
            self.goal.target_pose.pose.position.x = self.x + self.random_x
            self.goal.target_pose.pose.position.y = self.y + self.random_y
            self.goal.target_pose.pose.orientation.w = 1
            self.client.send_goal(self.goal)
            self.client.wait_for_result()
            self.client.get_result()

            if(self.client.get_state() == GoalStatus.SUCCEEDED):
                rospy.loginfo("Hooray, the base moved 1 meter forward")
            else:
                rospy.loginfo("The base failed to move forward 1 meter for some reason")


    def odom_callback(self, data):

        self.x = data.pose.pose.position.x
        self.y = data.pose.pose.position.y

    # def map_callback(self, data):

    # def laser_callback(self, data):



    # def random_direction(self):
    #     while not rospy.is_shutdown():
    #         random_x = random.random()
    #         random_y = random.random()
    #         self.goal = MoveBaseGoal()
    #         #goal should be position and orientation specified in rviz
    #         self.goal.target_pose.pose.position.x = self.x + random_x
    #         self.goal.target_pose.pose.position.y = self.y + random_y
    #         self.goal.target_pose.pose.orientation.w = 1




    


if __name__ == "__main__":

    n = MovetoGoal()
    # n.random_direction()
    rospy.spin()