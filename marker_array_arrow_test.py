#!/usr/bin/env python
import rospy
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
from geometry_msgs.msg import Point

if __name__ == '__main__':
    rospy.init_node('visualize', anonymous=True)
    print('start visualization node')

    publisher = rospy.Publisher('visualization_marker_array', MarkerArray, queue_size=10000)
    rate = rospy.Rate(3) # 30hz
    while not rospy.is_shutdown():
        markerArray = []
        marker = Marker()
        marker.header.frame_id = "/my_frame"
        marker.id = 0
        marker.type = marker.ARROW
        marker.action = marker.ADD
        marker.scale.x = 0.1
        marker.scale.y = 0.2
        marker.scale.z = 0.1
        marker.color.a = 1.0
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        marker.pose.orientation.x = 0.0;
        marker.pose.orientation.y = 0.0;
        marker.pose.orientation.z = 0.0;
        marker.pose.orientation.w = 1.0;
        temp1 = Point()
        temp1.x = 0.0
        temp1.y = 0.0
        temp1.z = 0.0
        marker.points.append(temp1)
        temp2 = Point()
        temp2.x = 0.0
        temp2.y = 0.0
        temp2.z = 1.0
        marker.points.append(temp2)
        markerArray.append(marker)
        msg = MarkerArray(markers=markerArray)
        publisher.publish(msg)
        rate.sleep()

    
  
