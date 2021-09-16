import launch


def generate_launch_description():
    # Declare arguments
    message_arg = launch.actions.DeclareLaunchArgument(
        'message',
        default_value='This is my message...',
        description='Message to show in the terminal'
    )
    show_message_arg = launch.actions.DeclareLaunchArgument(
        'show_message',
        default_value="1",
        description='Set to 1, true, or True to show the message.'
    )

    # Declare launch configuration substitutions
    message_conf = launch.substitutions.LaunchConfiguration(message_arg.name)
    show_message_conf = launch.substitutions.LaunchConfiguration(show_message_arg.name)

    return launch.LaunchDescription([
        message_arg,
        show_message_arg,
        launch.actions.LogInfo(
            msg=message_conf,
            condition=launch.conditions.IfCondition(predicate_expression=show_message_conf)
        ),
    ])
