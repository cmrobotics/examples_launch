from ament_index_python.packages import get_package_share_directory

import launch
import launch.launch_description_sources


def generate_launch_description():
    # Declare arguments
    message_arg = launch.actions.DeclareLaunchArgument(
        'message',
        default_value='Hello world from the parent',
        description='Message to show in the terminal'
    )
    message_no_default_arg = launch.actions.DeclareLaunchArgument(
        'message_without_default',
        description='Message to show in the terminal. This one does not have a default value.'
    )

    # Declare launch configuration substitutions
    message_conf = launch.substitutions.LaunchConfiguration(message_arg.name)
    message_no_default_conf = launch.substitutions.LaunchConfiguration(message_no_default_arg.name)

    # It is preferable to use launch.substitutions.PathJoinSubstitution instead
    # of os.path.join since part of the path might come from a LaunchConfiguration.
    # If everything is known in advance, before the substitutions are resolved,
    # then PathJointSubstitution will work just like os.path.join.
    path_to_child_launch_file = launch.substitutions.PathJoinSubstitution(
        substitutions=[
            get_package_share_directory('examples_launch'),
            './nesting/child.launch.py'
        ]
    )

    launch_child = launch.actions.IncludeLaunchDescription(
        launch.launch_description_sources.PythonLaunchDescriptionSource(path_to_child_launch_file),
        launch_arguments={
            message_arg.name: message_conf,
            message_no_default_arg.name: "This was set in the top level"
        }.items()
    )

    return launch.LaunchDescription([
        message_arg,
        message_no_default_arg,
        launch.actions.LogInfo(msg=message_conf),
        launch.actions.LogInfo(msg=message_no_default_conf),
        launch_child
    ])
