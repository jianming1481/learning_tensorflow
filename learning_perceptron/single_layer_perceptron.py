import numpy as np

x1 = np.array([0, 0, 1, 1])
x2 = np.array([0, 1, 0, 1])
y  = np.array([0, 0, 0, 1])
w1 = np.random.rand()
w2 = np.random.rand()
bias = np.random.rand()
learning_rate = 0.2
for i in range(1,100):
    np.random.seed()
    n = np.random.random_integers(0,3)
    pred_y = w1*x1[n] + w2*x2[n] + bias
    if pred_y>0:
        pred_y=pred_y
    else:
        pred_y=0
    error = y[n]-pred_y
    [w1,w2] = [w1, w2] + np.dot([w1, w2],learning_rate*error)
    bias = bias + learning_rate*error
    index =0
    for j in range(0,3):
        val_pred_y = w1*x1[j]+w2*x2[j] + bias
        e = y[j]-val_pred_y
        index = index+e*e*0.5
    
    if index == 0:
        print('index = 0')
        print(i,' times')
        break

