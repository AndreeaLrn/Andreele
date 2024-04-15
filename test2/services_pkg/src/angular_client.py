#! /usr/bin/python3
import rospy
from services_pkg.srv import angular_test, angular_testResponse

# Initialise a ROS node with the name service_client
rospy.init_node('service_client')

# Wait for the service /move_direction to be running
rospy.wait_for_service('/angular_service')

# Create the connection to the service
angular_service = rospy.ServiceProxy('/angular_service', angular_test)

# Create an object of type CustomServMessRequest
angular_request = angular_testResponse()
angular_request.direction = 'angular'

# Send the request to the service
result = angular_service(angular_request)

# Print the result given by the service called
print("Service call was successful:", result.success)
