import numpy as np

# initial values
INPUTS = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
LEARNING_RATE = 0.1


# step function (activation function)
def step_function(sum):
    if sum >= 0:
        return 1
    return -1


# calculateing output
def calculate_output(weights, instance, bias):
    sum = instance.dot(weights) + bias
    return step_function(sum)

# Adaline Algorithm
def adaline(outputs, weights, bias):
    total_error = 1
    counter = 0
    while total_error != 0 and counter < 10:

        total_error = 0
        counter += 1
        for i in range(len(outputs)):
            sum = INPUTS[i].dot(weights) + bias
            prediction = step_function(sum)

            total_error += outputs[i] - prediction
            error = outputs[i] - sum

            if outputs[i] != prediction:
                weights[0] = weights[0] + (LEARNING_RATE * error * INPUTS[i][0])
                weights[1] = weights[1] + (LEARNING_RATE * error * INPUTS[i][1])
                bias = bias + (LEARNING_RATE * error)
                print("Weight updated: " + str(weights[0]))
                print("Weight updated: " + str(weights[1]))
                print("Bias updated`: " + str(bias))
                print("----------------------------------------")

        print("Total error: " + str(total_error))
        print("----------------------------------------")

    return weights, bias

# Perceptron Algorithm
def perceptron(outputs, weights, bias):
    total_error = 1
    counter = 0
    while total_error != 0 and counter < 10:

        total_error = 0
        counter += 1
        for i in range(len(outputs)):
            sum = INPUTS[i].dot(weights)
            prediction = step_function(sum + bias)

            total_error += outputs[i] - prediction

            if outputs[i] != prediction:
                weights[0] = weights[0] + (LEARNING_RATE * outputs[i] * INPUTS[i][0])
                weights[1] = weights[1] + (LEARNING_RATE * outputs[i] * INPUTS[i][1])
                bias = bias + (LEARNING_RATE * outputs[i])
                print("Weight updated: " + str(weights[0]))
                print("Weight updated: " + str(weights[1]))
                print("Bias updated: " + str(bias))
                print("----------------------------------------")

        print("Total error: " + str(total_error))
        print("----------------------------------------")

    return weights, bias

# Hebb Algorithm
def hebb(outputs, weights, bias):
    for i in range(4):

        weights[0] = weights[0] + (INPUTS[i][0] * outputs[i])
        weights[1] = weights[1] + (INPUTS[i][1] * outputs[i])
        bias = bias + (1 * outputs[i])

        print("Weight updated: " + str(weights[0]))
        print("Weight updated: " + str(weights[1]))
        print("Bias updated: " + str(bias))
        print("----------------------------------------")

    return weights, bias


if __name__ == "__main__":
    and_outputs = np.array([1, -1, -1, -1])
    or_outputs = np.array([1, 1, 1, -1])
    weights = np.array([0.0, 0.0])
    bias = 0

    type_selector = input(
        "Please, enter which gate do you want? (and, or) (0 for exit): "
    ).strip()
    algorithm_selector = input(
        "Please, enter which algorithm do you want to run? (Hebb, Perceptron, Adaline) (0 for exit): "
    ).strip()

    while type_selector!= "0" and algorithm_selector != "0":

        if type_selector.lower() == "or":
            match algorithm_selector.lower():
                case "hebb":
                    returned_weights, returned_bias = hebb(or_outputs, weights, bias)
                case "perceptron":
                    returned_weights, returned_bias = perceptron(or_outputs, weights, bias)
                case "adaline":
                    returned_weights, returned_bias = adaline(or_outputs, weights, bias)

     
        elif type_selector.lower() == "and":
            
            match algorithm_selector.lower():
                case "hebb":
                    returned_weights, returned_bias = hebb(and_outputs, weights, bias)
                case "perceptron":
                    returned_weights, returned_bias = perceptron(and_outputs, weights, bias)
                case "adaline":
                    returned_weights, returned_bias = adaline(and_outputs, weights, bias)
                
        print('prediction for [1, 1]: ' + str(calculate_output(returned_weights, np.array([[1, 1]]), returned_bias)))
        print('prediction for [1, -1]: ' + str(calculate_output(returned_weights, np.array([[1, -1]]), returned_bias)))
        print('prediction for [-1, 1]: ' + str(calculate_output(returned_weights, np.array([[-1, 1]]), returned_bias)))
        print('prediction for [-1, -1]: ' + str(calculate_output(returned_weights, np.array([[-1, -1]]), returned_bias)))

        type_selector = input(
            "Please, enter which gate do you want? (and, or) (0 for exit): "
        ).strip()
        algorithm_selector = input(
            "Please, enter which algorithm do you want to run? (Hebb, Perceptron, Adaline) (0 for exit): "
        ).strip()
