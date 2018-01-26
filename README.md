# who-is-in-the-photo
An attempt to solve a face recognition problem with deep learning for identify famous people in images.

This project was built as a capstone project for the Udacity Machine Learning Nanodegree.

## Project Organization

This repository has 2 main folders:

1) exploratory-analysis

    In this folder are all jupyter notebooks created during the exploratory data analysis.

2) project
    
    In this folder you will find a web project that demonstrates the model in action.

## Installation

- clone the project
- install OpenCV. [ Tutorial to install in Ubuntu here.](https://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/)
- install Dlib. [ Tutorial to install in Ubuntu here.](https://www.pyimagesearch.com/2017/03/27/how-to-install-dlib/) 
- `pip install -r requirements_full.txt`

### Dataset

To train the models, this project uses the [PubFig83](http://vision.seas.harvard.edu/pubfig83/). You can download the dataset using this link:

https://www.dropbox.com/s/15g5lngya9ivqom/faces.zip?dl=0  

After download, you need to extract the files into a face folder. It must stay at the same level of `exploratory-analysis/` and `project/`.

## Exploratory analysis

There are 2 notebooks inside this folder: `base-line-model.ipynb` and `deep-learning-model.ipynb`.

### Baseline notebook

In this notebook is defined the baseline model (PCA+SVM+Eingenfaces).

To run this notebook, you can use: 

`cd exploratory-analysis`

`jupyter notebook base-line-model.ipynb`

### Deep Learning Model notebook

In this notebook is defined and tested the deep learning model.

To run this notebook:

`cd exploratory-analysis`

`jupyter notebook deep-learning-model.ipynb`

To optimize the use of the deep learning model, I saved the train weights of the 3 architecture tested . You can download this using this link:

https://drive.google.com/open?id=13CWCTqvwDk58OKBHyzCYJ1ii8rOJ-D_c

Extract the files into the folder `exploratory-analysis/saved_models`.

The are 3 saved files, one for each architecture:

- VGG16 - `custom_vgg16_weights.custom.model.hdf5`
- ResNet50 - `custom_resnet50_weights.custom.model.hdf5`
- Custom model - `weights.custom.model.hdf5`

## Web Project

The web project is writen in Python + Flask. All the code is located inside the folder `project/`

To run a local version, you can use:

`cd project`

`python runserver.py`

Open the browser and go to http://127.0.0.1:5000/

There are also a online version of the project. You can access the demo using this url:

https://who-is-in-the-photo.herokuapp.com/


If you have any questions, send me a message:

`gutomcosta at gmail.com`