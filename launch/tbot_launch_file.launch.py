from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tbot',
            executable='servolisten.py',
            output='screen'),
    ])
