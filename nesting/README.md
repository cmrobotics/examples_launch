# Nesting Launch Files

## Introduction
This directory hosts files that show how to nest launches.

## Running
There are two launch files, namely `toplevel.launch.py` and `child.launch.py`. The former calls the latter and passes arguments to it. This is also a good example to show that the configuration value extracted through `LaunchConfiguration` is local to the launch file. Both launch files declare the same arguments, `message` and `message_without_default`.

The top-level launch file passes the value of its `message` configuration forward to an argument of the same name defined in the child launch file. However, it chooses to pass a hard-coded string to the child's `argument_without_default` argument.
```Python
launch_child = launch.actions.IncludeLaunchDescription(
    launch.launch_description_sources.PythonLaunchDescriptionSource(path_to_child_launch_file),
    launch_arguments={
        message_arg.name: message_conf,
        message_no_default_arg.name: "This was set in the top level"
    }.items()
)
```

Both launch files, `toplevel.launch.py` and `child.launch.py`, have actions to output the value of their `message` and `message_without_default` configurations (written by the `message` and `message_without_default` arguments) to the terminal. By running,
```
ros2 launch examples_launch toplevel.launch.py  message_without_default:="Value from the terminal"
```
you can verify that while `message` is the same for both launch files, `message_without_default` is not, showing that configuration values are local to launch files.
