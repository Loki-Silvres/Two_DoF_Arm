#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

if __name__ == "__main__":
    rospy.init_node("two_dof_arm_controller")
    first_motor_pub = rospy.Publisher("/first_joint_controller/command", Float64, queue_size=10)
    second_motor_pub = rospy.Publisher("/second_joint_controller/command", Float64, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        inp1,inp2 = input("Enter angle (in radians) for first and second motors: ").split()
        print(inp1)
        inp1 = float(inp1)
        inp2 = float(inp2)
        msg1 = Float64()
        msg1.data = inp1
        msg2 = Float64()
        msg2.data = inp2

        first_motor_pub.publish(msg1)
        second_motor_pub.publish(msg2)
        rate.sleep()