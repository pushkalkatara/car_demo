project(prius_spawn)

cmake_minimum_required(VERSION 2.8.3)

find_package(catkin REQUIRED COMPONENTS visualstates
  rospy
  sensor_msgs
  geometry_msgs
  prius_msgs
)

catkin_package()
include_directories(${catkin_INCLUDE_DIRS})
install(PROGRAMS prius_spawn.py DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
