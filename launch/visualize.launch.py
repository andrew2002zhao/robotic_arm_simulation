# import nodes and launch descriptions
import os

from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

import xacro

# this launch file should publish the robot description then start rviz

def generate_launch_description():
    # get the paths of the robot description
    # /ros2_ws/my_arm_description/urdf/my_arm_description.xacro
    package_path = os.path.join(
            get_package_share_directory('my_arm_description'))
   
   
    xacro_file = os.path.join(package_path, 'urdf', 'my_arm_description.xacro')
    # return the file as a file object
    print(xacro_file)
    doc = xacro.parse(open(xacro_file)) 
    xacro.process_doc(doc)
    params = {'robot_description': doc.toxml()}

    nodes = []
    


    # joint_state_publisher = Node(
    #     package= "joint_state_publisher_gui",
    #     executable= "joint_state_publisher_gui",
    #     output='screen',
    #     name='joint_state_publisher_node',
    #     parameters=[{'use_sim_time': True}]
    # )

    # # define robot state publisher node
    robot_state_publisher = Node(
        package= "robot_state_publisher",
        executable="robot_state_publisher",
        name='robot_state_publisher_node',
        output="screen",
        emulate_tty="true",
        parameters=[params],
    )

    # # define rviz node
    rviz = Node(
            package='rviz2',
            executable='rviz2',
            output='screen',
            name='rviz',
            parameters=[{'use_sim_time': True}]
            )
            

    return LaunchDescription([
        # the nodes to start
       
        rviz,
        robot_state_publisher
        
    ])

