{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "12e423ef-b865-4bd5-8b8a-47259117ec0a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os, shutil"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "40ea94fd-8902-43a9-af3a-1b9f8023a95e",
   "metadata": {},
   "outputs": [],
   "source": [
    "path = r\"C:/Users/DIVYA BASANTRAY/Downloads/Python Tutorials\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "94113832-bf13-4229-b5e7-2ec1a19ddea4",
   "metadata": {},
   "outputs": [],
   "source": [
    "file_name = os.listdir(path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "51554955-911f-4c81-83b0-c406f779aff0",
   "metadata": {},
   "outputs": [],
   "source": [
    "folder_names = ['csv files', 'image files', 'text files']\n",
    "\n",
    "for loop in range(0,3):\n",
    "    if not os.path.exists(path + folder_names[loop]):\n",
    "        #print(path + folder_names[loop])\n",
    "        os.makedirs(path + folder_names[loop])\n",
    "\n",
    "for file in file_name:\n",
    "    if \".csv\" in file and not os.path.exists(path + \"csv files/\" + file):\n",
    "        shutil.move(path + file, path + \"csv files/\" + file)\n",
    "    elif \".png\" in file and not os.path.exists(path + \"image files/\" + file):\n",
    "        shutil.move(path + file, path + \"image files/\" + file)\n",
    "    elif \".txt\" in file and not os.path.exists(path + \"text files/\" + file):\n",
    "        shutil.move(path + file, path + \"text files/\" + file)"
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
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
