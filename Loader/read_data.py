import os
import struct
from array import array

class data_loader():

    def __init__(self):

        self.train_img_file = 'data/train-images-idx3-ubyte'
        self.train_labels_file = 'data/train-labels-idx1-ubyte'

        self.test_img_file = 'data/t10k-images-idx3-ubyte'
        self.test_label_file = 'data/t10k-labels-idx1-ubyte'

        self.train_img = []
        self.train_label = []

        self.test_img = []
        self.test_label = []

    def load(load , img_path , label_path) :

        with open(img_path , 'rb') as image_file:
            magic , size , rows , cols = struct.unpack('>IIII' , image_file.read(4*4))
            image_data = array('B' , image_file.read())

        img_size = rows*cols
        images = []

        for i in range(size) :
            image = image_data[i*img_size : (i+1)*img_size]
            images.append(image)

        with open(label_path , 'rb') as label_file :
            magic , size = struct.unpack('>II' , label_file.read(2*4))
            labels = array('B' , label_file.read())

        return images , labels

    def load_training(self) :
        self.train_img , self.train_label = self.load(os.path.join( os.getcwd() ,self.train_img_file) , 
                                                                    os.path.join( os.getcwd() ,self.train_labels_file))
    
    def load_test(self) :
        self.test_img , self.test_label = self.load(os.path.join( os.getcwd() ,self.test_img_file) , 
                                                                    os.path.join( os.getcwd() ,self.test_labels_file))
