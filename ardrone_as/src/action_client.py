#!/usr/bin/env python

import rospy
import actionlib
from ardrone_as.msg import MoveInCircleAction, MoveInCircleGoal

def move_robot():
    rospy.init_node('move_in_circle_client')
    client = actionlib.SimpleActionClient('move_in_circle', MoveInCircleAction)
    client.wait_for_server()

    # Setăm obiectivul acțiunii
    goal = MoveInCircleGoal()
    goal.nr_sec = 10  # Numărul de secunde pentru care să se execute acțiunea
    goal.linear_speed = 1.0  # Viteza liniară
    goal.angular_speed = 0.5  # Viteza unghiulară pentru a muta robotul în cerc

    client.send_goal(goal)
    client.wait_for_result()

    # Rezultatul acțiunii
    result = client.get_result()
    rospy.loginfo('Final twist: %s' % result.final_twist)

if __name__ == '__main__':
    try:
        move_robot()
    except rospy.ROSInterruptException:
        pass

