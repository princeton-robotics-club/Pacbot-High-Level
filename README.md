# Princeton_Robotics_Club_PacBot

software for Princeton Robotics Club team in the 2022 Harvard PacBot competition

(make sure you have python installed if you want to run any of this code!)

Side note: Some of these instructions may only work on Windows. There are equivalent instructions for MacOS/Linux

To run the PacBot game code as a gym environment (which is the standard interface used in ML RL), first clone the repository to your computer with the following instructions. Using your terminal, navigate to your project directory and execute:

`git clone https://github.com/princeton-robotics-club/Pacbot-High-Level.git`

Next, cd into the repository:

`cd Pacbot-High-Level`

Optional: Activate a virtual environment. The purpose of this is to avoid installing packages globally and have the correct
versions of packages specific to your project. If you have multiple python projects on your computer, this is a godsend.
The following commands create a virtual environment called 'env':

```
python -m venv env
```

In order to activate the environment:

Windows -

```
env\Scripts\activate
```

Mac/Linux -

```
source env/bin/activate
```

Next, cd into the newly cloned git repository folder and install all package dependencies defined in requirements.txt:

`pip install -r requirements.txt`

A demo usage of the gym environment is in gym_simulator/run_high_level.py and can be run with:

`python run_high_level.py`

This will run whatever policy is being used in the run_high_level script.

To add pauses to make the simulation easier to watch, you can use the following command:

`python run_high_level.py --s`

The demo takes the following inputs:

q = quit

space = pause/unpause

If you run:

`python run_gym.py`

You can pretty much play our simulator's version of pacman. You can use WASD to move the pacman, q to quit, and any other key to make the pacman stay still.
