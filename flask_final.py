{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "46bc0905",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "921dbf35",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "f53736f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/')\n",
    "def home():\n",
    "    return 'Welcome to my credit scoring application!'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1584f585",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Welcome to my credit scoring application!'"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "home()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "afabd52e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c2aa7acf",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "from flask import Flask, request, render_template\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "80c00f24",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RandomForestClassifier(random_state=10)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model = joblib.load('credit_scoring_model.joblib')\n",
    "model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "03c710d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "d0f2808b",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('index.html')\n",
    "\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    input_values = [float(x) for x in request.form.values()]\n",
    "    input_data = np.array(input_values).reshape(1, -1)\n",
    "    prediction = model.predict(input_data)[0]\n",
    "    return render_template('prediction.html', prediction=prediction)\n"
   ]
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
