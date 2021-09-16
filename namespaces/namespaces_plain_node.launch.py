import launch
import launch.launch_description_sources
import launch_ros.actions


def generate_launch_description():
    # Declare arguments for the namespace stuff with their respective configurations
    namespace_arg = launch.actions.DeclareLaunchArgument(
        'namespace',
        default_value="",
        description='Name of the namespace.'
    )
    namespace_conf = launch.substitutions.LaunchConfiguration(namespace_arg.name)

    # Declare nodes without explicitly setting the namespace
    node = launch_ros.actions.Node(
        package='examples_launch',
        name = 'arbitrary_name',
        executable = 'simple_publisher',
        parameters = [
            {"message_content": "Hello my friend..."}
        ],
    )

    node_other = launch_ros.actions.Node(
        package='examples_launch',
        name = 'other_name',
        executable = 'simple_publisher',
        parameters = [
            {"message_content": "Hello my friend..."}
        ],
    )

    # Group all the nodes that should belong to a namespace if one is given
    group_nodes = launch.actions.GroupAction([
        # This action will push the namespace if the configuration value is not empty
        launch_ros.actions.PushRosNamespace(
            condition=launch.conditions.LaunchConfigurationNotEquals(
                launch_configuration_name=namespace_arg.name,
                expected_value=""
            ), 
            namespace=namespace_conf
        ),
        # This action will launch the ROS node
        node
    ])

    return launch.LaunchDescription([
        namespace_arg,
        group_nodes,
        node_other
    ])
