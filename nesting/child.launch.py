import launch
import launch.launch_description_sources


def generate_launch_description():
    # Declare arguments
    message_arg = launch.actions.DeclareLaunchArgument(
        'message',
        default_value='Hello world from the child',
        description='Message to show in the terminal'
    )
    message_no_default_arg = launch.actions.DeclareLaunchArgument(
        'message_without_default',
        description='Message to show in the terminal. This one does not have a default value.'
    )

    # Declare launch configuration substitutions
    message_conf = launch.substitutions.LaunchConfiguration(message_arg.name)
    message_no_default_conf = launch.substitutions.LaunchConfiguration(message_no_default_arg.name)

    return launch.LaunchDescription([
        message_arg,
        message_no_default_arg,
        launch.actions.LogInfo(msg=message_conf),
        launch.actions.LogInfo(msg=message_no_default_conf),
    ])
