#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Point
from std_msgs.msg import ColorRGBA
from visualization_msgs.msg import Marker

if __name__ == '__main__':
    rospy.init_node('visualize', anonymous=True)
    publisher = rospy.Publisher('visualization_marker', Marker, queue_size=10000)
    rate = rospy.Rate(3) # 30hz
    while not rospy.is_shutdown():
        marker = Marker()
        marker.header.frame_id = "/my_frame"
        marker.id = 0
        marker.type = marker.TRIANGLE_LIST
        marker.action = marker.ADD
        marker.pose.orientation.x = 0.0;
        marker.pose.orientation.y = 0.0;
        marker.pose.orientation.z = 0.0;
        marker.pose.orientation.w = 1.0;
        marker.pose.position.x = 0.0
        marker.pose.position.y = 0.0
        marker.pose.position.z = 0.0
        marker.scale.x = 1.0
        marker.scale.y = 1.0
        marker.scale.z = 1.0

        temp1 = Point()
        temp1.x = 0.0
        temp1.y = 0.0
        temp1.z = 0.0
        marker.points.append(temp1)
        temp2 = Point()
        temp2.x = 1.0
        temp2.y = 0.0
        temp2.z = 0.0
        marker.points.append(temp2)
        temp3 = Point()
        temp3.x = 0.0
        temp3.y = 1.0
        temp3.z = 0.0
        marker.points.append(temp3)
        scan_color = ColorRGBA()
        scan_color.a = 1.0
        scan_color.r = 0.0
        scan_color.g = 1.0
        scan_color.b = 0.0
        marker.colors.append(scan_color)
        marker.colors.append(scan_color)
        marker.colors.append(scan_color)

        temp4 = Point()
        temp4.x = 0.0
        temp4.y = 0.0
        temp4.z = 1.0
        marker.points.append(temp4)
        temp5 = Point()
        temp5.x = 1.0
        temp5.y = 0.0
        temp5.z = 1.0
        marker.points.append(temp5)
        temp6 = Point()
        temp6.x = 0.0
        temp6.y = 1.0
        temp6.z = 1.0
        marker.points.append(temp6)
        scan_color = ColorRGBA()
        scan_color.a = 1.0
        scan_color.r = 1.0
        scan_color.g = 0.0
        scan_color.b = 0.0
        marker.colors.append(scan_color)
        marker.colors.append(scan_color)
        marker.colors.append(scan_color)

        # print(marker.points[1])
        # marker.color = scan_color
        publisher.publish(marker)
        rate.sleep()

    
  
