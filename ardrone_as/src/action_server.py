#!/usr/bin/env python

import rospy
import actionlib
from ardrone_as.msg import actionAction, actionFeedback, actionResult
from geometry_msgs.msg import PoseStamped

class actionServer:
    def _init_(self):
        self.server = actionlib.SimpleActionServer('action', actionAction, self.execute, False)
        self.server.start()
        self.pose_subscriber = rospy.Subscriber('/pose_topic', PoseStamped, self.pose_callback)
        self.current_orientation_y = 0.0

    def pose_callback(self, msg):
        self.current_orientation_y = msg.pose.orientation.y

    def execute(self, goal):
        rate = rospy.Rate(1) # 1 Hz
        orientations = []
        start_time = rospy.Time.now()

        while (rospy.Time.now() - start_time).to_sec() < goal.duration:
            if self.server.is_preempt_requested():
                self.server.set_preempted()
                break
            feedback = actionFeedback()
            feedback.orientation_y = self.current_orientation_y
            self.server.publish_feedback(feedback)
            orientations.append(self.current_orientation_y)
            rate.sleep()

        result = Action2Result()
        result.orientations = orientations
        self.server.set_succeeded(result)

if _name_ == '_main_':
    rospy.init_node('action_server')
    server = actionServer()
    rospy.spin()
