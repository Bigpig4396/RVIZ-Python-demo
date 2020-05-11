#!/usr/bin/env python
import rospy
from gazebo_msgs.msg import ContactsState
from using_markers.msg import MyContact
import math
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
import random

if __name__ == '__main__':
    rospy.init_node('visualize', anonymous=True)
    print('start visualization node')

    publisher = rospy.Publisher('visualization_marker_array', MarkerArray, queue_size=10000)
    rate = rospy.Rate(3) # 30hz
    while not rospy.is_shutdown():
        markerArray = []
        for i in range(20):
            marker = Marker()
            marker.header.frame_id = "/my_frame"
            marker.id = i
            marker.type = marker.SPHERE
            marker.action = marker.ADD
            marker.scale.x = 0.2
            marker.scale.y = 0.2
            marker.scale.z = 0.2
            marker.color.a = 1.0
            marker.color.r = 0.0
            marker.color.g = 1.0
            marker.color.b = 0.0
            marker.pose.orientation.x = 0.0;
            marker.pose.orientation.y = 0.0;
            marker.pose.orientation.z = 0.0;
            marker.pose.orientation.w = 1.0;
            pos_x = random.random()
            pos_y = random.random()
            pos_z = random.random()
            print('marker at', pos_x, pos_y, pos_z)
            marker.pose.position.x = pos_x
            marker.pose.position.y = pos_y
            marker.pose.position.z = pos_z
            markerArray.append(marker)
        msg = MarkerArray(markers=markerArray)
        publisher.publish(msg)
        rate.sleep()

    
  
