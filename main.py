import random
import sys
from dvclive import Live
import tensorflow as tf

# train.py


with Live(save_dvc_exp=True) as live:
    NUM_EPOCHS = 1

    live.log_param("epochs", NUM_EPOCHS)

    for epoch in range(NUM_EPOCHS):
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
        model.fit(x_train,y_train,epochs=1)

        metrics = model.evaluate(x_test,y_test,verbose=2)
        live.log_metric("accuracy", metrics[0])
        # for metric_name, value in metrics.items():
        #     live.log_metric(metric_name, value)

        live.next_step()

    live.log_artifact("./model", type="model", name="test1")
