# Using Namespaces
## Introduction
This directory hosts files that show how to define and use namespaces.

## Running Without a Configuration File
An elegant way of setting the namespace of not only one but multiple nodes, is to use a `PushRosNamespace` action inside a `GroupAction` action. The `GroupAction` is not mandatory, but it isolates the namespace so that nodes defined outside the group are not impacted. To see that, run
```
ros2 launch examples_launch namespaces_plain_node.launch.py namespace:="serena"
```
and verify that two nodes appear, `serena.arbitrary_name` and `other_name`, the first one nested in the namespace `serena` and the second one without a namespace. To check the the conditional namespace rule works, run the launch file without setting the `namespace` argument
```
ros2 launch examples_launch namespaces_plain_node.launch.py
```
and verify that two nodes appear, `arbitrary_name` and `other_name`.

## Running With a Configuration File
When using a configuration file, one must take care of changing the root key in the configuration file in case it does not match the selected namespace. Since, in this example, there is no namespace pre-configured in the `config.yaml` file, we set one by making use of the `RewrittenYaml` substitution provided by the `nav2_common` package. This example combines what you have learned in the `namespaces_plain_node.launch.py` and `configurable.launch.py` examples. To run it, use
```
ros2 launch examples_launch namespaces_yaml_configuration.launch.py" namespace:="serena"
```
and remember that you can ommit the `namespace` argument as well as use the `file_path` argument to choose the configuration file.
