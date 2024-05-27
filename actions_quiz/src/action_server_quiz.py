#! /usr/bin/env python
import rospy
import actionlib
from actions_quiz.msg import nameAction, nameResult, nameFeedback
from geometry_msgs.msg import TwistStamped

class QuizServer(object):
	_feedback = nameFeedback()
	_result = nameResult()
	
	def __init__(self):
		self._as = actionlib.SimpleActionServer('quiz_as', nameAction, self.goal_callback, False)
		self._as.start()
		
	#---	
		
	def convert(self, duration):
		twist = TwistStamped()
		twist.twist.linear.y = duration * 0.1	
		return twist
		
	def goal_callback(self, goal):
		r = rospy.Rate(1)
		succes = True
		
		self._feedback.distance = []
		
		rospy.loginfo("'quiz_as': Executing... " % (goal.duration, self._feedback.distance[0], self._feedback.distance[1]))
		
		quizDuration = goal.duration
		for i in range (1, quizDuration):
		
			if self._as.is_preempt_requested():
				rospy.loginfo('The goal had been canceled')
				self._as.set_preempted()
				succes = Fail
				break
			
			self._feedback.distance.append(self_feedback.distance[i] + self._feedback.distance[i-1])
			self._as.publish_feedback(self._feedback)
			
			r.sleep()
			
		if succes:
			self._result.succes = self._feedback.distance
			rospy.loginfo('Succes without slight inconveniences . . . ' )
			self._as.set_succeeded(self._result)
			
if __name__ == '__main__':
	rospy.init_node('quizServer_sendAJUTOARE')
	_as = QuizServer()
	rospy.spin()
		
		
