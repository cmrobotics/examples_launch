from ament_index_python.packages import get_package_share_directory
import launch
import launch.launch_description_sources
import launch_ros.actions


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
    config_file_conf = launch.substitutions.LaunchConfiguration(config_file_arg.name)

    # Declare nodes
    node = launch_ros.actions.Node(
        package='examples_launch',
        name = 'arbitrary_name',
        executable = 'simple_publisher',
        parameters = [config_file_conf]
    )

    return launch.LaunchDescription([
        config_file_arg,
        node
    ])
