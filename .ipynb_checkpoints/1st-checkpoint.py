import tensorflow as tf
from tensorflow.keras import layers, models

def create_mlp(input_size, hidden_sizes, output_size) :
    model = models.Sequential()
    model.add(layers.InputLayer(input_shape=(input_size, ))
    for hidden_size in hidden_sizes :
        model.add(layers.Dense(hidden_size, activation='relu')
    model.add(layers.Dense(output_size, activation='softmax'))
    return model
                  
if _name_ == "_main_" :
    input_size = 10
    hidden_sizes = [64,32]
    output_size = 2
    mlp_model = create_mlp(input_size, hidden_sizes, output_size)
    mlp_model.summary()