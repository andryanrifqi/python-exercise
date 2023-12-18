"""Functions for implementing the rules of the classic arcade game Pac-Man."""
def eat_ghost(power_pellet_active, touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.
 
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can the ghost be eaten?
    """
    can_eat_ghost = bool(power_pellet_active and touching_ghost)
    return can_eat_ghost
def score(touching_power_pellet, touching_dot):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.
 
    :param touching_power_pellet: bool - is the player touching a power pellet?
    :param touching_dot: bool - is the player touching a dot?
    :return: bool - has the player scored or not?
    """
    if touching_power_pellet==True or touching_dot==True:
        pac_man_scored = True
    else:
        pac_man_scored = False
    return pac_man_scored
def lose(power_pellet_active, touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.
 
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """
    if power_pellet_active==False and touching_ghost==True:
        pac_man_loses = True
    else:
        pac_man_loses = False
    return pac_man_loses
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Trigger the victory event when all dots have been eaten.
 
    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    """
    if has_eaten_all_dots==True:
        if power_pellet_active==False and touching_ghost==True:
            pac_man_win = False
        else:
            pac_man_win = True
    else:
        pac_man_win = False
    return pac_man_win