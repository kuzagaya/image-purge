# Image Purge: Removing Notes from a Directory
The goal of this project is to automate the process of deleting images of notes from your directory. The project was inspired by the personal experience of having to manually delete a large number of images of notes after the exams from the folders. So in this projet we automate this task using python.

A deep neural network is trained to classify images and delete those that are no longer needed. This saves users time and effort, allowing them to easily manage and organize their exam image collections.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Installing

1. Clone the repository:

```
git clone https://github.com/[user]/image-purge.git

```
2. Install the required libraries:
```
pip install -r requirements.txt
```
3. Download the dataset and extract it to the data directory.

4. Use the model to classify and delete notes from a project directory:
```
python purge.py [path_to_directory]
```
## Screenshots:
![screenshot2.png](https://i.postimg.cc/JhkSP6hP/screenshot2.png)

## Built With
* [Keras](https://www.tensorflow.org/) - The ML framework used
* [Jupyter Notebook](https://jupyter.org/) - Used to train the model
