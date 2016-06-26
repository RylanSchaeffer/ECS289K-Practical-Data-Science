__author__ = 'rylan'

from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import SGD
import numpy
import struct

outfile = open('results3.txt', 'a')

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

# convert training labels to 10-dimensional vector
copy = trainLabels
trainLabels = numpy.ndarray((60000, 10))
for pos in range(len(copy)):
    label = copy[pos]
    vector = numpy.zeros(10,)
    vector[label] += 1
    trainLabels[pos] = vector


with open(trainImagesPath, 'rb') as imgpath:
    magic, num, rows, cols = struct.unpack(">IIII", imgpath.read(16))
    trainImages = numpy.fromfile(imgpath, dtype=numpy.uint8).reshape(len(trainLabels), 784)/255.0

# construct testing images and labels
with open(testLabelsPath, 'rb') as lbpath:
    magic, n = struct.unpack('>II', lbpath.read(8))
    testLabels = numpy.fromfile(lbpath, dtype=numpy.uint8)

# convert testing labels to 10-dimensional vector
copy = testLabels
testLabels = numpy.ndarray((10000, 10))
for pos in range(len(copy)):
    label = copy[pos]
    vector = numpy.zeros(10,)
    vector[label] += 1
    testLabels[pos] = vector

with open(testImagesPath, 'rb') as imgpath:
    magic, num, rows, cols = struct.unpack(">IIII", imgpath.read(16))
    testImages = numpy.fromfile(imgpath, dtype=numpy.uint8).reshape(len(testLabels), 784)/255.0

for alpha in range(1, 27):

    # create neural network
    neuralNet = Sequential()
    neuralNet.add(Dense(output_dim=30, input_dim=784, init='glorot_normal'))
    neuralNet.add(Activation('sigmoid'))
    neuralNet.add(Dense(output_dim=10, init='glorot_normal'))
    neuralNet.add(Activation('sigmoid'))


    # configure nn learning process
    neuralNet.compile(loss='categorical_crossentropy', optimizer=SGD(lr=alpha/100.0, momentum=0.9))

    # train neural net
    neuralNet.fit(trainImages, trainLabels, nb_epoch=50)

    # predict labels
    predictedLabels = neuralNet.predict(testImages)

    [objective_score, accuracy] = neuralNet.evaluate(testImages, testLabels, show_accuracy=True)

    outfile.write('1 hidden layer, %f alpha, %f accuracy, rectifier\n'
                  % (alpha/100.0, accuracy))

outfile.close()

# compute accuracy
