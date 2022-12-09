import warnings
warnings.filterwarnings('ignore')

from keras.preprocessing.image import ImageDataGenerator
from keras import backend as K

img_width = 224
img_height = 224

train_data_dir = '../data/train'
validation_data_dir = '../data/valid'
nb_train_samples = 72
nb_validation_samples = 32
epochs = 10
batch_size = 4


train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='binary')

