from tensorflow.keras.datasets import cifar10


def load_cifar10():
    (Xtrain, Ytrain), (Xtest, Ytest) = cifar10.load_data()
    
    X_mean, X_std = Xtrain.mean(), Xtrain.std()

    Xtrain = (Xtrain - X_mean) / X_std
    Xtest = (Xtest - X_mean) / X_std
    return (Xtrain, Ytrain), (Xtest, Ytest), (X_mean, X_std)
