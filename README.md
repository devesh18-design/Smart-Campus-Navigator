# Smart-Campus-Navigator

**Smart Campus Navigator (A* Pathfinding)**

An intelligent, graph-based navigation system designed for university campuses. This project uses the A* Search Algorithm to find optimal walking paths, accounting for real-world factors like stairs, terrain quality, and accessibility.

**Overview **

Navigating large, developing campuses can be a challenge. Standard mapping tools often lack the granular detail of internal walking paths or fails to distinguish between a flat walkway and a steep staircase.
Smart Campus Navigator transforms a physical campus layout into a digital State-Space Search Graph. By applying a cost-sensitive search, it provides users with the most efficient route based on their specific needs (e.g., avoiding stairs for heavy luggage or seeking them out for athletic training).

**AI Concepts Applied**

Graph Theory: Campus landmarks are represented as Nodes, and walkways are Weighted Edges.
Informed Search (A*): Utilizes the evaluation function f(n) = g(n) + h(n).
Admissible Heuristic: Employs Euclidean Distance to ensure the path found is always mathematically optimal.
Cost Functions: Dynamically adjusts edge weights based on "Surface Factors" (e.g., a 1.5x multiplier for stairs).

**Tech Stack**

Language: Python 3.xGraph Library: NetworkX (Robust graph manipulation and pathfinding)

Visualization: Matplotlib (Spatial plotting and UI)

Math: Python math module for heuristic calculations.

**Campus Map NodesThe system currently maps 16 key locations including:**

Administrative: Main Gate, Academic Block, Central Office, Library.

Student Life: Canteen, Shopping Complex, Auditorium, Gym.

Residential: Hostels 1, 2, 4, and 8.

Recreational: Sports Ground, Lab Complex, Medical Center.

**Results**

The algorithm generates a visual map where:

Gray Circles: Represent campus landmarks.

Black Lines: Represent standard flat paths.

Orange/Green Overlay: Highlights the calculated optimal route.

Distance Calculation: Provides the total weighted distance in meters in the window title.

**How to Run the Project**

Follow these steps to set up the environment and execute the navigator on your local machine.

1. Prerequisites

Ensure you have Python 3.7 or higher installed. You can check your version by running:
python --version

2. Clone the Repository

Download the project files to your local system:
git clone https://github.com/devesh18-design/Smart-Campus-Navigator
cd smart-campus-navigator

3. Install Required Libraries

This project relies on NetworkX for graph logic and Matplotlib for the GUI. Install them via pip:
pip install networkx matplotlib

4. Execute the Script

Run the main Python file to launch the visual navigator:
https://github.com/devesh18-design/Smart-Campus-Navigator/blob/main/Smart%20university%20navigator.py

5. Interacting with the OutputThe Map Window: A window titled "Smart University Campus Navigator by Devesh Katneshwarkar" will appear.

6. The Visualization:

Orange Nodes: Your calculated path.

Light Green Edges: The specific route chosen by the A* algorithm.

Gray Nodes: Other available campus landmarks.

Console Output: The terminal will print the step-by-step route
