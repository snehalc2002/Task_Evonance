{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "72d3ca0e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Valid JSON received:\n",
      "{\n",
      "  \"benefits\": [\n",
      "    \"Easy to learn and use\",\n",
      "    \"Rich ecosystem of libraries like pandas and NumPy\",\n",
      "    \"Great community support and documentation\"\n",
      "  ]\n",
      "}\n"
     ]
    }
   ],
   "source": [
    "import json\n",
    "\n",
    "def call_gemini(prompt):\n",
    "    return '''\n",
    "    {\n",
    "      \"benefits\": [\n",
    "        \"Easy to learn and use\",\n",
    "        \"Rich ecosystem of libraries like pandas and NumPy\",\n",
    "        \"Great community support and documentation\"\n",
    "      ]\n",
    "    }\n",
    "    '''\n",
    "\n",
    "\n",
    "prompt = \"List 3 benefits of Python for data science. Respond in JSON format.\"\n",
    "response_text = call_gemini(prompt)\n",
    "\n",
    "\n",
    "try:\n",
    "    response_json = json.loads(response_text)\n",
    "    print(\"Valid JSON received:\")\n",
    "    print(json.dumps(response_json, indent=2))\n",
    "\n",
    "except json.JSONDecodeError:\n",
    "    print(\"Invalid JSON received. Raw output:\")\n",
    "    print(response_text)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bf327bf7",
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
