import rclpy
from rclpy.node import Node
from gpiozero import Servo
from time import sleep

from std_msgs.msg import Float32

servo = Servo(25)

class ServoListen(Node):

    def __init__(self):
        super().__init__('servo_listen')
        self.subscription = self.create_subscription(
            Float32,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        servo.value = msg.data
        


def main(args=None):
    rclpy.init(args=args)

    servo_listen = ServoListen()

    rclpy.spin(servo_listen)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    servo_listen.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()