# Using a Configuration File
## Introduction
This directory hosts file that show how to pass parameters with YAML files.

## Running
To pass a parameter through a YAML the name of the node and the key in the YAML file should match. In this example, we choose to use `arbitrary_name` on both sides to make the match. If the names do not match, then there is a little bit more work involved in parsing the file.

The launch file here will run a publisher node that will relay the message in the parameter named `message_content`. The value of the parameter is fetched from the `config.yaml` when running
```
ros2 launch examples_launch configurable.launch.py
```

You may use your own YAML file by providing the full path to it through the launch argument `file_path`, like so
```
ros2 launch examples_launch configurable.launch.py file_path:="/full/path/to/your_file.yaml"
```