from robot import Robot 


def solve_maze():

    my_robot = Robot()

    response_code = ''

    # Keep going until the robot is finished
    while response_code != "FINISHED":

        # Look around to see if there is a space then move into that space.
        look_code = my_robot.look_around()
 
        # Encourage them to print feedback from their robot 
        if look_code == 'PATH_UP':
            print("MOVING UP")
            response_code = my_robot.move_up()
        elif look_code == 'PATH_RIGHT':
            print("MOVING RIGHT")
            response_code = my_robot.move_right()
        elif look_code == 'PATH_LEFT':
            print("MOVING_LEFT")
            response_code = my_robot.move_left()
        elif look_code == 'PATH_DOWN':
            print("MOVING_DOWN")
            response_code = my_robot.move_down()
    
    print("FINISHED")

        
solve_maze()

        


