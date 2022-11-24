#include "math.h"

struct Position;

const double PI2 = 3.1415 * 2;
const Position GOAL = {40, 40};


struct Position{
    double x;
    double y;
}


void aiming_algorithm(double rx, double ry, double rangle){
    // find angle to goal
    double dx, dy;
    dx = GOAL.x - rx;
    dy = GOAL.y - ry;

    // now find angle
    angle = tanh(dy / dx);

    // spin towards desired angle
    // fix this
    rangle = rangle - round(rangle / PI2) * PI2;
    // now angle is in range of -pi and pi

    // spin towards angle
    turn(angle - rangle);

    // shoot :D
    // check error
    shoot();

}



void turn(int angle) // in rad
{   
    // assume it works
}

void shoot()
{
    // assume it works
}




