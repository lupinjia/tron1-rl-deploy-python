import os
import sys
import argparse
import limxsdk.robot.Robot as Robot
import limxsdk.robot.RobotType as RobotType
import controllers

if __name__ == '__main__':
    # Get the robot type from the environment variable
    robot_type = os.getenv("ROBOT_TYPE")
    
    # Check if the ROBOT_TYPE environment variable is set, otherwise exit with an error
    if not robot_type:
        print("\033[31mError: Please set the ROBOT_TYPE using 'export ROBOT_TYPE=<robot_type>'.\033[0m")
        sys.exit(1)
    # get rl type
    rl_type = os.getenv("RL_TYPE")
    if not rl_type:
        print("\033[31mError: Please set the RL_TYPE using 'export RL_TYPE=isaacgym/isaaclab'.\033[0m")
        sys.exit(1)
    if rl_type != "isaacgym" and rl_type != "isaaclab":
        print("\033[31mError: RL_TYPE {} is not supported, choose between 'isaacgym' and 'isaaclab'.\033[0m".format(rl_type))
        sys.exit(1)

    # Create a Robot instance of the specified type
    robot = Robot(RobotType.PointFoot)
    
    # Add argument parser for command-line arguments
    parser = argparse.ArgumentParser(description='TRON1 Robot Controller')
    parser.add_argument('--robot_ip', type=str, default='127.0.0.1', help='IP address of the robot')
    parser.add_argument('--type', type=str, default='default', help='Type of controller to use')
    parser.add_argument('--config', type=str, default='params.yaml', help='Configuration filename')
    parser.add_argument('--use_usb_joy', action='store_true', default=False, help='Use USB joystick for command input')
    args = parser.parse_args()

    # Default IP address for the robot
    robot_ip = args.robot_ip

    # Initialize the robot with the provided IP address
    if not robot.init(robot_ip):
        sys.exit()

    # Determine if the simulation is running
    start_controller = robot_ip == "127.0.0.1"

    # Get controller type
    controller_type = args.type
    # Get config filename
    config_filename = args.config
    
    # Create and run the controller
    if robot_type.startswith("PF"):
      if controller_type == "default":
        controller = controllers.PointfootController(f'{os.path.dirname(os.path.abspath(__file__))}/controllers/model', robot, robot_type, rl_type, start_controller)
      elif controller_type == "ee":
        controller = controllers.PointfootEEController(f'{os.path.dirname(os.path.abspath(__file__))}/controllers/model', 
                                robot, robot_type, rl_type, start_controller, config_filename,
                                args.use_usb_joy)
      controller.run()
    elif robot_type.startswith("WF"):
      controller = controllers.WheelfootController(f'{os.path.dirname(os.path.abspath(__file__))}/controllers/model', robot, robot_type, rl_type, start_controller)
      controller.run()
    elif robot_type.startswith("SF"):
      controller = controllers.SolefootController(f'{os.path.dirname(os.path.abspath(__file__))}/controllers/model', robot, robot_type, rl_type, start_controller)
      controller.run()
    else:
      print(f"Error: unknow robot type '{robot_type}'")
