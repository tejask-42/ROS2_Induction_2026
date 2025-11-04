import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class CounterNode(Node):
    def __init__(self):
        super().__init__('counter_node')
        self.counter = 0
        self.subscription = self.create_subscription(
            String,
            'time_topic',
            self.listener_callback,
            10
        )
        self.subscription

    def listener_callback(self, msg):
        self.counter += 1
        self.get_logger().info(f"Received message {self.counter}: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = CounterNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
