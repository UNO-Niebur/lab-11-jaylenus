# StopLightSim.py
# Name: Jaylen Atsou
# Date: April 15, 2026
# Assignment: Lab 11

import simpy

# Global variable to track light state
greenLight = True


def stopLight(env):
    """Simulates a traffic light that cycles between green, yellow, and red."""
    global greenLight

    while True:
        print("Green at time", env.now)
        greenLight = True
        yield env.timeout(30)

        print("Yellow at time", env.now)
        yield env.timeout(2)

        print("Red at time", env.now)
        greenLight = False
        yield env.timeout(20)


def car(env, car_id):
    """Simulates a car arriving and waiting for the light."""
    global greenLight
    
    print("Car", car_id, "arrived at", env.now)

    # Make the car wait while the light is red
    while not greenLight:
        print("Car", car_id, "waiting at", env.now)
        yield env.timeout(1)

    yield env.timeout(1)
    print("Car", car_id, "departed at", env.now)


def carArrival(env):
    """Creates cars at regular intervals."""
    
    car_id = 0

    while True:
        car_id += 1
        print("Creating Car", car_id)

        # Start a new car process
        env.process(car(env, car_id))

        yield env.timeout(5)


def main():
    env = simpy.Environment()

    # Start processes
    env.process(stopLight(env))
    
    # Start the carArrival process
    env.process(carArrival(env))

    # Run simulation
    env.run(until=100)

    print("Simulation complete")


if __name__ == "__main__":
    main()