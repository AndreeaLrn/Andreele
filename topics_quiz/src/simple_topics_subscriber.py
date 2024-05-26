#! /usr/bin/env python

import rospy
import time
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):
    global turn
    print(msg.ranges[0])
    # Check if the distance to the wall is less than 1 meter
    if msg.ranges[0] < 1.0:
        # Stop the robot
        turn.linear.x = 0
        turn.angular.z = 0
        pub.publish(turn)
        time.sleep(0.5)  # Make sure the robot has stopped
        
        # Turn left
        turn.angular.z = 0.5  # Positive value for left turn
        pub.publish(turn)
        time.sleep(2)  # Turn for 2 seconds
        
        # Move forward a little after turning
        turn.linear.x = 0.2
        turn.angular.z = 0  # Stop turning
        pub.publish(turn)
        time.sleep(2)  # Move forward for 2 seconds
        
        # Turn around to face the opposite direction
        turn.linear.x = 0
        turn.angular.z = 0.5
        pub.publish(turn)
        time.sleep(4)  # Adjust this time based on the robot's turning speed to complete a 180 degree turn
        
        # Reset the turn command to stop the robot
        turn.linear.x = 0
        turn.angular.z = 0
        pub.publish(turn)

# Initialize ROS node
rospy.init_node('scan_listener')

# Create a publisher and subscriber
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub = rospy.Subscriber('/scan', LaserScan, callback)

# Set the rate of the loop
rate = rospy.Rate(2)  # 2Hz

turn = Twist()

rospy.spin()

