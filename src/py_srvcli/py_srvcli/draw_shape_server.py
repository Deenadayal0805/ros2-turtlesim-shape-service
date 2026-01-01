import rclpy
from rclpy.node import Node
from tutorial_interfaces.srv import DrawShape
from geometry_msgs.msg import Twist
from rclpy.executors import MultiThreadedExecutor
import time
import math

class DrawShapeServer(Node):

    def __init__(self):
        super().__init__('draw_shape_server')

        self.srv = self.create_service(DrawShape,'draw_shape',self.draw_shape_callback)

        self.pub = self.create_publisher(Twist,'/turtle1/cmd_vel',10)

        self.get_logger().info('Draw Shape Service Server Ready')


    def draw(self,linear,angular,duration):
        msg = Twist()
        msg.linear.x = float(linear)
        msg.angular.z = float(angular)       

        end_time = time.time() + duration
        while time.time() < end_time:
            self.pub.publish(msg)
            time.sleep(0.1)

    def draw_shape_callback(self, request, response):
        shape = request.shape.lower()
        size = request.size

        if shape == 'square':

            for i in range (4): 
                self.draw(size,0.0,1)
                self.draw(0.0,math.pi/2,1)
            response.success = True
            response.message = 'Square drawn'
        else:
            response.success = False
            response.message = 'Unsupported shape'

        return response

    # def draw_square(self, size):
    #     msg = Twist()

    #     for _ in range(4):
    #         msg.linear.x = size
    #         msg.angular.z = 0.0
    #         self.publisher.publish(msg)
    #         rclpy.spin_once(self, timeout_sec=1)

    #         msg.linear.x = 0.0
    #         msg.angular.z = 1.57
    #         self.publisher.publish(msg)
    #         rclpy.spin_once(self, timeout_sec=1)


def main():
    rclpy.init()
    node = DrawShapeServer()
    executor = MultiThreadedExecutor()
    executor.add_node(node)
    try:
        executor.spin()
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()