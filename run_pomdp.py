#!/usr/bin/env python
__author__ = 'patrickemami'

import sys
from pomdpy.solvers import Solver
from pomdpy.examples.rock_problem import RockModel
from pomdpy.examples.tiger_problem import TigerModel
from log import init_logger

SAMPLE_PROBLEM = sys.argv[1]

if __name__ == '__main__':

    init_logger()

    if SAMPLE_PROBLEM == "1":
        simulator = RockModel("Rock Problem")
        simulator.draw_env()
        my_solver = Solver(simulator)
        my_solver.discounted_return()
        my_solver.logger.info("Map: " + simulator.rock_config["map_file"])
    elif SAMPLE_PROBLEM == "2":
        simulator = TigerModel("Tiger Problem")
        my_solver = Solver(simulator)
        my_solver.discounted_return()
    else:
        print "Unable to execute unknown sample problem " + SAMPLE_PROBLEM


