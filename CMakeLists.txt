cmake_minimum_required(VERSION 3.5)
project(examples_launch)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rclcpp REQUIRED)

# Create the simple publisher node
add_executable(simple_publisher src/simple_publisher_node.cpp)
ament_target_dependencies(simple_publisher std_msgs rclcpp)

# Install the targets
install(TARGETS simple_publisher
  DESTINATION lib/${PROJECT_NAME})

# Install the directories that go into the share folder
install(DIRECTORY
  nesting config_files
  DESTINATION share/${PROJECT_NAME}/
)

# Call ament so that it does its automated things
ament_package()
