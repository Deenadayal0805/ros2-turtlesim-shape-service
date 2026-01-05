from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    server_node = Node(
        package='py_srvcli',
        executable='draw_shape_server',
        name='draw_shape_server',
        output='screen'
    )
    # client_node = Node(
    #     package='py_srvcli',
    #     executable='draw_shape_client',
    #     name='draw_shape_client',
    #     output='screen'
    # )
    
    turtlesim_node = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtlesim_node',
        output='screen'
    )

    return LaunchDescription([
        server_node,
        # client_node,
        turtlesim_node
    ])