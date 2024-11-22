#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
from mavros_msgs.msg import State
from nav_msgs.msg import Odometry


class DroneSimpleController:
    def __init__(self):
        rospy.init_node('odometry_node', anonymous=True)

        self.state = State()
        self.odom = Odometry()

        rospy.Subscriber('/mavros/state', State, self.state_cb)
        rospy.Subscriber('mavros/local_position/odom',Odometry, self.odom_cb)

        rate = rospy.Rate(20)


        while not rospy.is_shutdown():
            rospy.loginfo("x:%f, y:%f, z:%f, mode: %s ",
                          self.odom.pose.pose.position.x, 
                          self.odom.pose.pose.position.y, 
                          self.odom.pose.pose.position.z,
                          self.state.mode)
            rate.sleep()


    def state_cb(self, message):
        self.state = message
        


    def odom_cb(self, message):
        self.odom = message


if __name__ == '__main__':
    try:
        DroneSimpleController()
    except rospy.ROSInterruptException:
        pass









