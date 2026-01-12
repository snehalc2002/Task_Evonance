{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "73d6e148",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'tensorflow'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mtensorflow\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mtf\u001b[39;00m\n\u001b[0;32m      3\u001b[0m data_augmentation \u001b[38;5;241m=\u001b[39m tf\u001b[38;5;241m.\u001b[39mkeras\u001b[38;5;241m.\u001b[39mSequential([\n\u001b[0;32m      4\u001b[0m     tf\u001b[38;5;241m.\u001b[39mkeras\u001b[38;5;241m.\u001b[39mlayers\u001b[38;5;241m.\u001b[39mRandomRotation(\u001b[38;5;241m0.1\u001b[39m),    \n\u001b[0;32m      5\u001b[0m     tf\u001b[38;5;241m.\u001b[39mkeras\u001b[38;5;241m.\u001b[39mlayers\u001b[38;5;241m.\u001b[39mRandomFlip(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhorizontal\u001b[39m\u001b[38;5;124m\"\u001b[39m),\n\u001b[0;32m      6\u001b[0m     tf\u001b[38;5;241m.\u001b[39mkeras\u001b[38;5;241m.\u001b[39mlayers\u001b[38;5;241m.\u001b[39mRandomZoom(\u001b[38;5;241m0.2\u001b[39m)          \n\u001b[0;32m      7\u001b[0m ])\n\u001b[0;32m      9\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mmatplotlib\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mpyplot\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mplt\u001b[39;00m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'tensorflow'"
     ]
    }
   ],
   "source": [
    "import tensorflow as tf\n",
    "\n",
    "data_augmentation = tf.keras.Sequential([\n",
    "    tf.keras.layers.RandomRotation(0.1),    \n",
    "    tf.keras.layers.RandomFlip(\"horizontal\"),\n",
    "    tf.keras.layers.RandomZoom(0.2)          \n",
    "])\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "from tensorflow.keras.utils import load_img, img_to_array\n",
    "\n",
    "\n",
    "img = load_img('your_image.jpg', target_size=(150, 150)) \n",
    "img_array = img_to_array(img) / 255.0                     \n",
    "img_array = tf.expand_dims(img_array, 0)                  \n",
    "\n",
    "augmented = data_augmentation(img_array)\n",
    "\n",
    "plt.imshow(augmented[0])\n",
    "plt.axis('off')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eeb0b41a",
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
