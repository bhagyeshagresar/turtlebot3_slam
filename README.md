# ME495-Homework 3

# Name : Bhagyesh Agresar

# turtlebot_slam Package

The package uses `slam_toolbox` to do autonomous realtime localization and mapping. There are 3 launchfiles in the package:

* `start_slam.launch` - use this launch file to map the surrounding environment in Gazebo or in real world.
* `nav_stack.launch` - use the `amcl` to localize the robot. Use the map created by `start_slam.launch`. 2D Nav Goals can be used
to move the robot in the map.
* `slam_stack.launch` - use the `slam_toolbox` particulartly `move_base` to set goals and `online_async.launch` to map the enviroment 
inorder to perform SLAM. In this case the Turtlebot will simulaneously map the enviroment as the robot drives in the environment. Use 2D
Nav Goals to move the robot in Gazebo or in real world.
* `explorer.launch`- uses a Random Exploration to autonomously move in real world. The robot performs mapping and localisation with the help
 of `slam_stack.launch` launchfile.


 # Instructions on the use of the package
 
 * Compile the workspace using `catkin_make`
 * Source the setup script of the workspace using `source devel/setup.bash`.
 * For all the launchfiles the default argument for simulation is set to true.
 * For all launchfiles run `roslaunch turtlebot launch_file_name.launch`

 # Video Demonstration of turtlebot following map made in Gazebo and Real world

 * Demonstration of nav_stack in Gazebo:
    https://drive.google.com/file/d/1McEcqYkdPR-eoeKzFbDeVBIgXyMVtWT3/view?usp=sharing

 * Demonstration of nav_stack in realworld rviz demonstration:
    https://drive.google.com/file/d/1ANmfJM-xBPJHuNN8SXs6zE3UAvmbVYSI/view?usp=sharing
    
 * Demonstration of nav_stack in realworld demonstration:
    https://drive.google.com/file/d/1eSjtOePhbBcFK9N9-k7wPQSpWyG9O2dI/view?usp=sharing

 * Demonstration of slam_stack in Gazebo:
    https://drive.google.com/file/d/1DOaA-zpw5RjrVRQA1nvEhJwAkKZ0Cryw/view?usp=sharing

 * Demonstration of slam_stack in Realworld Rviz Demonstration:
    https://drive.google.com/file/d/1O4fPofLGc8_NKEGtvIUg85ReBAeRmXe_/view?usp=sharing

 * Demonstration of slam_stack in Realworld:
    https://drive.google.com/file/d/1f5pOgjkgRAxOHEUFZ6HdZ23RPA79MUm_/view?usp=sharing

 * Demonstration of explorer.launch in Gazebo:
    https://drive.google.com/file/d/15XRNfk9EshZSfaxxNje_f1WToO2gy_zD/view?usp=sharing

 * Demonstration of explorer.launch in Realworld Rviz Demonstration:
    https://drive.google.com/file/d/1mlv5h0uLsqM0arzJ-WSVoAoD0-M_VKz5/view?usp=sharing

 * Demonstration of explorer.launch in realworld:
    https://drive.google.com/file/d/1eoPJ-Lr6S5jNuT_WOOEyIQJwPVEsR5sT/view?usp=sharing
