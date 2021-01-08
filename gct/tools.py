from tensorflow.keras.datasets import cifar10, boston_housing


def load_cifar10():
    (Xtrain, Ytrain), (Xtest, Ytest) = cifar10.load_data()
    
    Xtrain_flat = Xtrain.reshape(-1, 3)
    X_mean, X_std = Xtrain_flat.mean(axis=0), Xtrain_flat.std(axis=0)

    Xtrain = (Xtrain - X_mean) / X_std
    Xtest = (Xtest - X_mean) / X_std
    return (Xtrain, Ytrain), (Xtest, Ytest), (X_mean, X_std)


def load_boston_housing():
    (Xtrain, Ytrain), (Xtest, Ytest) = boston_housing.load_data()
    Ytrain = Ytrain.reshape(-1, 1)
    Ytest = Ytest.reshape(-1, 1)

    X_mean, X_std = Xtrain.mean(axis=0), Xtrain.std(axis=0)

    Xtrain = (Xtrain - X_mean) / X_std
    Xtest = (Xtest - X_mean) / X_std

    Y_mean, Y_std = Ytrain.mean(axis=0), Ytrain.std(axis=0)

    Ytrain = (Ytrain - Y_mean) / Y_std
    Ytest = (Ytest - Y_mean) / Y_std
    return (Xtrain, Ytrain), (Xtest, Ytest), (X_mean, X_std), (Y_mean, Y_std)
