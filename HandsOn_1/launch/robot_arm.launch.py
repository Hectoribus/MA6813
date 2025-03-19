import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    urdf_file = os.path.join(os.getcwd(), "/home/chetor/Desktop/NTU_PhD/Courses/Sem2/MA6813/HandsOn_1/robot_arm.urdf")

    return LaunchDescription([
        DeclareLaunchArgument('robot_description', default_value=urdf_file, description="Robot URDF"),
        
        # Start the robot_state_publisher node to publish the state of the robot
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': LaunchConfiguration('robot_description')}]
        ),
        Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2",
            output="screen",
        )
    ])
