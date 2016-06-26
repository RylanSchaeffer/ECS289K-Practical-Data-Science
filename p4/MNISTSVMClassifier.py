__author__ = 'rylan'

import numpy
from sklearn import svm, cross_validation, metrics
import struct

outfile = open('results.txt', 'a')

# Note: Code to import idx files taken from
# http://nbviewer.jupyter.org/github/rasbt/python-machine-learning-book/blob/master/code/ch12/ch12.ipynb#Obtaining-the-MNIST-dataset

# load mnist data file paths
testImagesPath = 't10k-images-idx3-ubyte'
testLabelsPath = 't10k-labels-idx1-ubyte'

trainImagesPath = 'train-images-idx3-ubyte'
trainLabelsPath = 'train-labels-idx1-ubyte'

# construct training images and labels
with open(trainLabelsPath, 'rb') as lbpath:
    magic, n = struct.unpack('>II', lbpath.read(8))
    trainLabels = numpy.fromfile(lbpath, dtype=numpy.uint8)

with open(trainImagesPath, 'rb') as imgpath:
    magic, num, rows, cols = struct.unpack(">IIII", imgpath.read(16))
    trainImages = numpy.fromfile(imgpath, dtype=numpy.uint8).reshape(len(trainLabels), 784)

# construct testing images and labels
with open(testLabelsPath, 'rb') as lbpath:
    magic, n = struct.unpack('>II', lbpath.read(8))
    testLabels = numpy.fromfile(lbpath, dtype=numpy.uint8)

with open(testImagesPath, 'rb') as imgpath:
    magic, num, rows, cols = struct.unpack(">IIII", imgpath.read(16))
    testImages = numpy.fromfile(imgpath, dtype=numpy.uint8).reshape(len(testLabels), 784)



# create linear SVM
linearSVC = svm.LinearSVC()
linearSVC.fit(trainImages, trainLabels)

# report linear SVM confusion matrix and classification report
predictedTestLabels = linearSVC.predict(testImages)
with open('results.txt', 'a') as outfile:
    outfile.write('Linear Kernel SVM Classification Report: \n%s\n'
                  % metrics.classification_report(testLabels, predictedTestLabels))
    outfile.write('Linear Kernel SVM Confusion Matrix: \n%s\n\n\n'
                  % metrics.confusion_matrix(testLabels, predictedTestLabels))



# create polynomial kernel SVM
polySVC = svm.SVC(kernel='poly')
polySVC.fit(trainImages, trainLabels)

# report polynomial kernel SVM
predictedTestLabels = polySVC.predict(testImages)
with open('results.txt', 'a') as outfile:
    outfile.write('Polynomial Kernel SVM Classification Report: \n%s'
                  % metrics.classification_report(testLabels, predictedTestLabels))
    outfile.write('Polynomial Kernel SVM Confusion Matrix: \n%s\n\n\n'
                  % metrics.confusion_matrix(testLabels, predictedTestLabels))



# create rbf kernel SVM
rbfSVC = svm.SVC(kernel='rbf')
rbfSVC.fit(trainImages, trainLabels)

# report rbf kernel SVM
predictedTestLabels = rbfSVC.predict(testImages)
with open('results.txt', 'a') as outfile:
    outfile.write('RBF Kernel SVM Classification Report: \n%s\n'
                  % metrics.classification_report(testLabels, predictedTestLabels))
    outfile.write('RBF Kernel SVM Confusion Matrix: \n%s\n\n\n'
                  % metrics.confusion_matrix(testLabels, predictedTestLabels))



# create sigmoid kernel SVM
sigmoidSVC = svm.SVC(kernel='sigmoid')
sigmoidSVC.fit(trainImages, trainLabels)

# report sigmoid kernel SVM
predictedTestLabels = sigmoidSVC.predict(testImages)
with open('results.txt', 'a') as outfile:
    outfile.write('Sigmoid Kernel SVM Classification Report: \n%s\n'
                  % metrics.classification_report(testLabels, predictedTestLabels))
    outfile.write('Sigmoid Kernel SVM Confusion Matrix: \n%s\n\n\n'
                  % metrics.confusion_matrix(testLabels, predictedTestLabels))


outfile.close()
