#!/usr/bin/env python3


import rospy
import actionlib
from actionlib_msgs.msg import GoalStatus
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from nav_msgs.msg import Odometry, OccupancyGrid, MapMetaData
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan



class MovetoGoal:
    def __init__(self):
        rospy.init_node("navigation_test")
        

    
