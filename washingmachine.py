import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define the fuzzy variables
dirtiness = ctrl.Antecedent(np.arange(0, 11, 1), 'dirtiness')
strain_type = ctrl.Antecedent(np.arange(0, 11, 1), 'strain_type')
washing_time = ctrl.Consequent(np.arange(0, 61, 1), 'washing_time')

# Define membership functions
dirtiness['low'] = fuzz.trimf(dirtiness.universe, [0, 0, 5])
dirtiness['medium'] = fuzz.trimf(dirtiness.universe, [0, 5, 10])
dirtiness['high'] = fuzz.trimf(dirtiness.universe, [5, 10, 10])

strain_type['low'] = fuzz.trimf(strain_type.universe, [0, 0, 5])
strain_type['medium'] = fuzz.trimf(strain_type.universe, [0, 5, 10])
strain_type['high'] = fuzz.trimf(strain_type.universe, [5, 10, 10])

washing_time['short'] = fuzz.trimf(washing_time.universe, [0, 0, 30])
washing_time['medium'] = fuzz.trimf(washing_time.universe, [0, 30, 60])
washing_time['long'] = fuzz.trimf(washing_time.universe, [30, 60, 60])

# Define rules
rule1 = ctrl.Rule(dirtiness['low'] & strain_type['low'], washing_time['short'])
rule2 = ctrl.Rule(dirtiness['medium'] & strain_type['medium'], washing_time['medium'])
rule3 = ctrl.Rule(dirtiness['high'] & strain_type['high'], washing_time['long'])

# Control system
washing_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
washing_machine = ctrl.ControlSystemSimulation(washing_ctrl)

if __name__ == "__main__":
    # Assign values to antecedents
    washing_machine.input['dirtiness'] = 7.5  # Example dirtiness level
    washing_machine.input['strain_type'] = 6  # Example strain type level
    
    # Perform the computation
    washing_machine.compute()
    
    # Output the result
    print("Washing Time : ", washing_machine.output['washing_time'])
    
    # View the result
    washing_time.view(sim=washing_machine)
