# Demo of Prius in ROS/GAZEBO

This is a simulation of a Prius in [gazebo 9](http://gazebosim.org) with sensor data being published using [ROS kinetic](http://wiki.ros.org/kinetic/Installation)
The car's throttle, brake, steering, and gear shifting are controlled by publishing a ROS message.
A ROS node allows driving with a gamepad or joystick.

# Requirements

This demo has been tested on Ubuntu Xenial (16.04)

* Gazebo 9
* ROS-Kinetic

# Steps to build

* Add the packages to ROS Directory.
* catkin_make

