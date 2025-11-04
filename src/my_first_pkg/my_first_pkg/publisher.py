import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from datetime import datetime

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(String, 'time_topic', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)  # 1 Hz
        self.get_logger().info("Publisher Node has started.")

    def timer_callback(self):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        message = f"Hello World! Current time is: {current_time}"
        self.publisher_.publish(String(data=message))
        self.get_logger().info(f"Publishing: {message}")

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
