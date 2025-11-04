# ROS2 Learning Repository

A comprehensive ROS2 demonstration project showcasing three fundamental concepts: **simple publisher-subscriber communication**, **custom message type implementation**, and **client-service architecture**. This repository is designed as a learning resource for understanding ROS2 communication patterns.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/tejask-42/ROS2_Induction_2026.git
cd ROS2_Induction_2026
```

### 2. Install Dependencies

```bash
sudo apt-get update
sudo apt-get install -y python3-rosdep
rosdep install --from-paths src --ignore-src -r -y
```

### 3. Build the Workspace

```bash
colcon build
```

The build process will:
- Generate Python interfaces from message and service definitions
- Compile all three packages
- Create the install directory

### 4. Source the Setup Script

```bash
source install/setup.bash
```

**Note:** You need to source this script in every new terminal before running ROS2 commands.

## Demo 1: Simple Publisher-Subscriber

This demonstrates basic ROS2 communication using standard message types (String messages).

### Run the Demo

In a terminal, execute:

```bash
ros2 launch my_first_pkg launch.py
```

This will start both the publisher and subscriber nodes simultaneously.


## Demo 2: Custom Message Type Implementation

This demonstrates how to define and use custom message types in ROS2. 

### Run the Demo

Open two terminals and execute the following commands:

**Terminal 1 - Start the Talker (Publisher):**

```bash
ros2 run pubsub talker
```

**Terminal 2 - Start the Listener (Subscriber):**

```bash
ros2 run pubsub listener
```

## Demo 3: Client-Service Implementation

This demonstrates the request-response communication pattern using custom service definitions. 

### Run the Demo

Open three terminals:

**Terminal 1 - Start the Service Server:**

```bash
ros2 run pubsub server
```

**Terminal 2 - Start the Service Client:**

```bash
ros2 run pubsub client 2 3 1
```

## Troubleshooting

### Build Fails

```bash
# Clean build
colcon build --symlink-install --packages-select tutorial_interfaces pubsub my_first_pkg

# Check dependencies
rosdep check --all
```

### "Source not found" Error

Ensure you've sourced the setup script:
```bash
source install/setup.bash
```

### Service/Node Not Found

Verify the node is running:
```bash
ros2 node list
ros2 topic list
ros2 service list
```

### Permission Errors

```bash
sudo chown -R $USER:$USER ~/ros2_ws
```

---
