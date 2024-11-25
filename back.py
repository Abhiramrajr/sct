import numpy as np
def initialize_network(input_size,hidden_size,output_size):
    np.random.seed(42) #Forreproducibility
    network={
        'W1':np.random.randn(input_size,hidden_size),
        'b1':np.zeros((1,hidden_size)),
        'W2':np.random.randn(hidden_size,output_size),
        'b2':np.zeros((1,output_size))
    }
    return network

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return x * (1-x)
def forward_propagation(network,X):
    Z1 = np.dot(X,network['W1'])+network['b1']
    A1 = sigmoid(Z1)
    Z2 = np.dot(A1,network['W2']) +network['b2']
    A2 = sigmoid(Z2)
    cache={
        'Z1':Z1,
        'A1':A1,
        'Z2':Z2,
        'A2':A2
    }
    return A2,cache
def train_network(network,X,Y,epochs,learning_rate):
    for epoch in range(epochs):
    #Forwardpass
        A2,cache = forward_propagation(network,X)
        #Computetheerror
        error=Y-A2
        #Updateweightsandbiasesfortheoutputlayer
        dZ2=error * sigmoid_derivative(A2)
        dW2=np.dot(cache['A1'].T,dZ2)
        db2=np.sum(dZ2,axis=0,keepdims=True)
        network['W2']+=learning_rate * dW2
        network['b2']+=learning_rate * db2
    #Updateweightsandbiasesforthehiddenlayer
        dA1 = np.dot(dZ2,network['W2'].T)
        dZ1 = dA1 * sigmoid_derivative(cache['A1'])
        dW1 = np.dot(X.T,dZ1)
        db1 = np.sum(dZ1,axis=0,keepdims=True)
        network['W1'] += learning_rate * dW1
        network['b1'] += learning_rate * db1
        if epoch % 1000 == 0:
            loss=np.mean(error**2)
    print(f'Epoch{epoch}, Loss:{loss}')
def predict(network,X):
    A2,_=forward_propagation(network,X)
    predictions=(A2>0.5).astype(int)
    return predictions
X=np.array([[0,0],
    [0,1],
    [1,0],
    [1,1]])
Y=np.array([[0],
    [1],
    [1],
    [0]])
 
 #Initializethenetwork
network = initialize_network(input_size=2,hidden_size=2,output_size=1)
 #Trainthenetwork
 
train_network(network,X,Y,epochs=10000,learning_rate=0.1)
 #Makepredictions
predictions = predict(network,X)
print("Predictions:")
print(predictions)