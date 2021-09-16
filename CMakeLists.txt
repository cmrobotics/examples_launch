cmake_minimum_required(VERSION 3.5)
project(examples_launch)

# Find dependencies
find_package(ament_cmake REQUIRED)

# Install the directories that go into the share folder
install(DIRECTORY
  nesting config
  DESTINATION share/${PROJECT_NAME}/
)

# Call ament so that it does its automated things
ament_package()
