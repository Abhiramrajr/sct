import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define antecedents and consequent
dirtiness = ctrl.Antecedent(np.arange(0, 11, 1), 'dirtiness')
washing_time = ctrl.Consequent(np.arange(0, 61, 1), 'washing_time')

# Define membership functions for antecedents
dirtiness['low'] = fuzz.trimf(dirtiness.universe, [0, 0, 5])
dirtiness['medium'] = fuzz.trimf(dirtiness.universe, [0, 5, 10])
dirtiness['high'] = fuzz.trimf(dirtiness.universe, [5, 10, 10])

# Define membership functions for consequent
washing_time['short'] = fuzz.trimf(washing_time.universe, [0, 0, 30])
washing_time['medium'] = fuzz.trimf(washing_time.universe, [15, 30, 45])
washing_time['long'] = fuzz.trimf(washing_time.universe, [30, 60, 60])

# Define fuzzy rules
rule1 = ctrl.Rule(dirtiness['low'], washing_time['short'])
rule2 = ctrl.Rule(dirtiness['medium'], washing_time['medium'])
rule3 = ctrl.Rule(dirtiness['high'], washing_time['long'])

# Create control system
washing_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
washing_machine = ctrl.ControlSystemSimulation(washing_ctrl)

# Set input values for antecedents
washing_machine.input['dirtiness'] = 8.7  # Example value for dirtiness

# Compute the result
washing_machine.compute()

# Output the result
print(f"Washing Time: {washing_machine.output['washing_time']} minutes")
