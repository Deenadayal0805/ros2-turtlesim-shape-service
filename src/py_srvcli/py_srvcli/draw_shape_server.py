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

        self.get_logger().info('Draw Shape Service Server Ready v1.2')


    def draw(self,linear,angular,duration):
        msg = Twist()
        msg.linear.x = float(linear)
        msg.angular.z = float(angular)       

        end_time = time.time() + duration
        while time.time() < end_time:
            self.pub.publish(msg)
            time.sleep(0.1)

    def draw_square(self, size):
        for _ in range(4):
            self.draw(size, 0.0, 1)
            self.draw(0.0, math.pi / 2, 1)

    def draw_rectangle(self, length, width):
        for _ in range(2):
            self.draw(length, 0.0, 1)
            self.draw(0.0, math.pi / 2, 1)
            self.draw(width, 0.0, 1)
            self.draw(0.0, math.pi / 2, 1)

    def draw_circle(self, radius):
        linear_speed = radius
        angular_speed = 1.0
        duration = (2 * math.pi) / angular_speed
        self.draw(linear_speed, angular_speed, duration)

    def draw_triangle(self, size):
        for _ in range(3):
            self.draw(size, 0.0, 1)
            self.draw(0.0, 2 * math.pi / 3, 1)    

    def draw_shape_callback(self, request, response):
        shape = request.shape.lower()
        size = request.size
        size_2 = request.size_2

        if shape == 'square':
            self.draw_square(size)
            # response.success = True
            response.message = 'Square drawn'

        elif shape == 'rectangle':
            self.draw_rectangle(size , size_2)
            response.message = 'rectangle drawn'

        elif shape == 'circle':
            self.draw_circle(size)
            response.message = 'circle drawn'

        elif shape == 'triangle' :
            self.draw_triangle(size)
            response.message = 'triangle drawn'
        else:
            response.success = False
            response.message = 'Unsupported shape'


        return response

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