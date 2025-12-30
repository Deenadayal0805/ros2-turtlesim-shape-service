import rclpy
from rclpy.node import Node
from tutorial_interfaces.srv import DrawShape

class DrawShapeClient(Node):

    def __init__(self):
        super().__init__('draw_shape_client')

        self.client = self.create_client(DrawShape, 'draw_shape')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')

        self.send_request()

    def send_request(self):
        request = DrawShape.Request()
        request.shape = 'square'
        request.size = 2.0

        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result():
            self.get_logger().info(future.result().message)


def main():
    rclpy.init()
    node = DrawShapeClient()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
