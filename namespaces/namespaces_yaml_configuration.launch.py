from ament_index_python.packages import get_package_share_directory
import launch
import launch.launch_description_sources
import launch_ros.actions
import nav2_common.launch


def generate_launch_description():
    # Declare substitutions
    default_path_to_config_file = launch.substitutions.PathJoinSubstitution(
        substitutions=[
            get_package_share_directory('examples_launch'),
            './config_files/config.yaml'
        ]
    )

    # Declare arguments with their respective configurations
    config_file_arg = launch.actions.DeclareLaunchArgument(
        'file_path',
        default_value=default_path_to_config_file,
        description='Full path to the configuration file used when loading the node.'
    )
    namespace_arg = launch.actions.DeclareLaunchArgument(
        'namespace',
        default_value="",
        description='Name of the namespace.'
    )
    #
    config_file_conf = launch.substitutions.LaunchConfiguration(config_file_arg.name)
    namespace_conf = launch.substitutions.LaunchConfiguration(namespace_arg.name)

    # Create a substitution to parse the YAML file before feeding it to the node so
    # that we can change the namespace (if needed). The keyword argument convert_types
    # is set to try just because it is common practice.
    parsed_config_file = nav2_common.launch.RewrittenYaml(
        source_file=config_file_conf,
        param_rewrites={},
        root_key=namespace_conf,
        convert_types=True
    )

    # Declare nodes without explicitly setting the namespace
    node = launch_ros.actions.Node(
        package='examples_launch',
        name = 'arbitrary_name',
        executable = 'simple_publisher',
        parameters = [parsed_config_file],
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
        config_file_arg,
        namespace_arg,
        group_nodes
    ])
