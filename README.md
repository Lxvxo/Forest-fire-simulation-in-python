# Forest Fire Spread Simulation

## Introduction
This project simulates the spread of forest fires using cellular automata. The simulation is based on a probabilistic model of fire spread and incorporates various parameters such as wind speed, m!
oisture level, and terrain type.

[fire](https://github.com/Lxvxo/Forest-fire-simulation-in-python/assets/113984090/5bf85547-8843-4328-8e5f-cc58f00bafd8)

## Requirements
- Python 3.x
- NumPy
- Matplotlib

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/forest-fire-simulation.git
    ```
2. Navigate to the project directory:
    ```bash
    cd forest-fire-simulation
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To run the simulation, execute the following command:
```bash
python simulation.py
```

You can customize the simulation parameters by editing the simulation.py file.

## Parameters
N: Number of iterations for the simulation.
n: Size of the grid (n x n).
p: Probability of a cell being a tree.
f: Number of initial fire sources.
t: Time interval between iterations (in seconds).

## Output
The simulation will display the progression of the forest fire spread in a graphical interface using Matplotlib. Each cell in the grid represents a portion of the forest, with different colors indicating different states (e.g., green for trees, red for fire, gray for ashes).
