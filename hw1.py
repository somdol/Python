{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "f1c16f3c",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "넓이를 구하고자 하는 원의 반지름은?55\n",
      "반지름이 55 인 원의 넓이는 3.14 x 55 x = 9498.500000000002\n"
     ]
    }
   ],
   "source": [
    "def get_radius(prompt) :\n",
    "    r= int(input(prompt))\n",
    "    return r\n",
    "\n",
    "def get_circle_area(r) :\n",
    "    return 3.14*r*r\n",
    "\n",
    "prompt='넓이를 구하고자 하는 원의 반지름은?'\n",
    "r = get_radius(prompt)\n",
    "result = get_circle_area(r)\n",
    "print('반지름이',r,'인 원의 넓이는','3.14','x',r,'x','=',result)"
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
