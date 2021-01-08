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

    X_mean, X_std = Xtrain.mean(axis=0), Xtrain.std(axis=0)

    Xtrain = (Xtrain - X_mean) / X_std
    Xtest = (Xtest - X_mean) / X_std
    return (Xtrain, Ytrain), (Xtest, Ytest), (X_mean, X_std)
