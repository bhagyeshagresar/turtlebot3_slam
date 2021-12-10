#!/usr/bin/env python3


import rospy
import actionlib





class MovetoGoal:
    rospy.init_node("navigation")
    self.client = actionlib.SimpleActionClinet("go_to_goal", MoveBaseActionGoal)
