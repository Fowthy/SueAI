import random
import sys
from dvclive import Live

with Live(save_dvc_exp=True) as live:
    epochs = int(sys.argv[1])
    live.log_param("epochs", epochs)
    for epoch in range(epochs):
        live.log_metric("train/accuracy", epoch + random.random())
        live.log_metric("train/loss", epochs - epoch - random.random())
        live.log_metric("val/accuracy",epoch + random.random() )
        live.log_metric("val/loss", epochs - epoch - random.random())
        live.next_step()





#import necessary libraries
import tensorflow as tf

#load training data and split into train and test sets
mnist = tf.keras.datasets.mnist

(x_train,y_train), (x_test,y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0


#define model
model = tf.keras.models.Sequential([
                               tf.keras.layers.Flatten(input_shape=(28,28)),
                                   tf.keras.layers.Dense(128,activation='relu'),
                                   tf.keras.layers.Dropout(0.2),
                                   tf.keras.layers.Dense(10)
])

#define loss function variable
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

#define optimizer,loss function and evaluation metric
model.compile(optimizer='adam',
             loss=loss_fn,
             metrics=['accuracy'])

#train the model
model.fit(x_train,y_train,epochs=5)


#test model accuracy on test set
model.evaluate(x_test,y_test,verbose=2)