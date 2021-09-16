# Examples Launch

## Introduction
This package hosts a collection of launch files that provide examples of how to do some things using the launch mechanism.

Note that the `launch` framework is detached from ROS2. It is a framework to orchestrate the launch of processes. It so happens that it is developed by the ROS2 team. Therefore, they use it in ROS2 and they also provide a separate Python package, called `launch_ros`, for wrapping `ROS2` functionality such as running nodes.

## Basics
As a simplification, the `launch` framework can be understood in two parts.
* `launch.actions` -- A set of actions telling what needs to be executed. Listed below are common examples. For the full list of native actions check https://github.com/ros2/launch/tree/master/launch/launch/actions.
  * `DeclareLaunchArgument` Arguments for the launch file.
  * `ExecuteProcess` A process.
  * `SetEnvironmentVariable` Setting an environment variable
* `launch.substitutions` -- A set of rules that are resolved in runtime after parsing the launch file(s). They are substitutions in the sense that their actual value can be a combination of many substitutions and it is only known (resolved) after all the substitutions are known. Listed below are common examples. For the full list of native actions check https://github.com/ros2/launch/tree/master/launch/launch/substitutions.
  * `LaunchConfiguration` -- A substitution that will access the value of a launch configuration. The only native actions that create launch configurations are the `DeclareLaunchArgument`, `AnonName`, and `SetLaunchConfiguration` actions. Since `DeclareLaunchArgument` is the most common, `LaunchConfiguration` is most commonly used to access the value of an argument defined exposed by the former.
  * `Command` -- A substitution that resolves the output of a command and writes it to a string.

## Nesting Launch Files
See the documentation under [the nesting directory](nesting/).
