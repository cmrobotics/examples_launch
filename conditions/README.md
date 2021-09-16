# Using Conditions
## Introduction
Conditions are another powerful side of the `launch` framework. By design, they are supported by all the actions. When creating an action, there is always the option to set the keyword argument `condition` so that the action is only executed if the condition is fulfilled. Like substitutions, conditions are only resolved after parsing the launch file.

## Running the If Condition
To showcase the `IfCondition`, one of the most used conditions, consider running
```
ros2 launch examples_launch if_condition.launch.py show_message:=0
```
and play around with the `show_message` argument. You can also change the message by setting the `message` argument.
