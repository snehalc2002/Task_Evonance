{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "62784cf8",
   "metadata": {},
   "outputs": [],
   "source": [
    "def truncate_summary(summary, max_words=50):\n",
    "    sentences = summary.strip().split('.')\n",
    "    word_count = 0\n",
    "    result = []\n",
    "\n",
    "    for s in sentences:\n",
    "        s = s.strip()\n",
    "        if not s:\n",
    "            continue\n",
    "        words_in_sentence = len(s.split())\n",
    "        if word_count + words_in_sentence <= max_words:\n",
    "            result.append(s)\n",
    "            word_count += words_in_sentence\n",
    "        else:\n",
    "            break\n",
    "\n",
    "    return '. '.join(result) + '.' if result else ''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9e3a1d8f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python is a versatile language used widely in data science. It supports libraries like NumPy and pandas. Its simple syntax and community make it beginner-friendly.\n"
     ]
    }
   ],
   "source": [
    "summary = (\"Python is a versatile language used widely in data science. \"\n",
    "           \"It supports libraries like NumPy and pandas. \"\n",
    "           \"Its simple syntax and community make it beginner-friendly.\")\n",
    "\n",
    "print(truncate_summary(summary, max_words=50))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0fef191f",
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
