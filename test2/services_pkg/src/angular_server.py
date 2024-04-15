#!/usr/bin/env python
import rospy
from services_pkg.srv import angular_test, angular_testResponse
from geometry_msgs.msg import Twist

def my_callback(request):
    print("My_callback has been called")
    start_time = rospy.Time.now()
    turn = Twist()
    rate = rospy.Rate(10)  # 10 Hz

    while (rospy.Time.now().to_sec - start_time.to_sec < request.duration):
        if request.direction == "pozitiv": 
            turn.angular.x = 0.2
        elif request.direction == "negativ":
            turn.angular.x = -0.2

        pub.publish(turn)

    turn.linear.x = 0.0
    turn.angular.x = 0.0
    pub.publish(turn)

    response = angular_testResponse()
    response.success = True
    return response

rospy.init_node('service_server')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

my_service = rospy.Service('/angular_service', angular_test, my_callback)
rospy.spin()

