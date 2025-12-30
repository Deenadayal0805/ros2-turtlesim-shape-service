import rclpy
from rclpy.node import Node
from tutorial_interfaces.srv import DrawShape
from geometry_msgs.msg import Twist

class DrawShapeServer(Node):

    def __init__(self):
        super().__init__('draw_shape_server')

        self.srv = self.create_service(
            DrawShape,
            'draw_shape',
            self.draw_shape_callback
        )

        self.publisher = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        self.get_logger().info('Draw Shape Service Server Ready')

    def draw_shape_callback(self, request, response):
        shape = request.shape.lower()
        size = request.size

        if shape == 'square':
            self.draw_square(size)
            response.success = True
            response.message = 'Square drawn'
        else:
            response.success = False
            response.message = 'Unsupported shape'

        return response

    def draw_square(self, size):
        msg = Twist()

        for _ in range(4):
            msg.linear.x = size
            msg.angular.z = 0.0
            self.publisher.publish(msg)
            rclpy.spin_once(self, timeout_sec=1)

            msg.linear.x = 0.0
            msg.angular.z = 1.57
            self.publisher.publish(msg)
            rclpy.spin_once(self, timeout_sec=1)


def main():
    rclpy.init()
    node = DrawShapeServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
