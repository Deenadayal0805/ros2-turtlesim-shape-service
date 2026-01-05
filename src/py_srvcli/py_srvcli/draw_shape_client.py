import rclpy
from rclpy.node import Node
from tutorial_interfaces.srv import DrawShape

class DrawShapeClient(Node):

    def __init__(self):
        super().__init__('draw_shape_client')

        self.client = self.create_client(DrawShape, 'draw_shape')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')

        self.menu()

    def menu(self):
        print("\n--- Shape Drawing Menu ---")
        print("\n1. Square")
        print("\n2. Circle")
        print("\n3. Rectangle")
        print("\n4. Triangle")

        size_2 = 0.0

        shape_map = { 1:'square', 2:'circle' , 3:'rectangle' , 4:'triangle'}

        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            size = float(input("Enter side length: "))

        elif choice == 2:
            size = float(input("Enter radius: "))   

        elif choice == 3:
            size = float(input("Enter length): "))
            size_2 = float(input("Enter breadth: ")) 

        elif choice == 4:
            size = float(input("Enter side length: "))

        else :
            print('Invalid choice!!')
            return

        request = DrawShape.Request()
        request.shape = shape_map[choice]
        request.size = size
        request.size_2 = size_2

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