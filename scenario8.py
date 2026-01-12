{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "418823c1",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'tensorflow'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mtf\u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mkeras\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcallbacks\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m EarlyStopping\n\u001b[0;32m      4\u001b[0m model \u001b[38;5;241m=\u001b[39m tf\u001b[38;5;241m.\u001b[39mkeras\u001b[38;5;241m.\u001b[39mSequential([\n\u001b[0;32m      5\u001b[0m     tf\u001b[38;5;241m.\u001b[39mkeras\u001b[38;5;241m.\u001b[39mlayers\u001b[38;5;241m.\u001b[39mDense(\u001b[38;5;241m64\u001b[39m, activation\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mrelu\u001b[39m\u001b[38;5;124m'\u001b[39m, input_shape\u001b[38;5;241m=\u001b[39m(\u001b[38;5;241m784\u001b[39m,)),\n\u001b[0;32m      6\u001b[0m     tf\u001b[38;5;241m.\u001b[39mkeras\u001b[38;5;241m.\u001b[39mlayers\u001b[38;5;241m.\u001b[39mDense(\u001b[38;5;241m10\u001b[39m, activation\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124msoftmax\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m      7\u001b[0m ])\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'tensorflow'"
     ]
    }
   ],
   "source": [
    "import tensorflow as tf\n",
    "from tensorflow.keras.callbacks import EarlyStopping\n",
    "\n",
    "model = tf.keras.Sequential([\n",
    "    tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),\n",
    "    tf.keras.layers.Dense(10, activation='softmax')\n",
    "])\n",
    "\n",
    "model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])\n",
    "\n",
    "\n",
    "early_stop = EarlyStopping(\n",
    "    monitor='val_loss',\n",
    "    patience=3,\n",
    "    restore_best_weights=True\n",
    ")\n",
    "\n",
    "# Dummy data (just for example)\n",
    "x_train = tf.random.normal([1000, 784])\n",
    "y_train = tf.random.uniform([1000], maxval=10, dtype=tf.int32)\n",
    "x_val = tf.random.normal([200, 784])\n",
    "y_val = tf.random.uniform([200], maxval=10, dtype=tf.int32)\n",
    "\n",
    "model.fit(x_train, y_train,\n",
    "          validation_data=(x_val, y_val),\n",
    "          epochs=20,\n",
    "          callbacks=[early_stop])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa1a5808",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
