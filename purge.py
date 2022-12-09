import pyfiglet
import os
import numpy as np
import argparse
import warnings
from PIL import Image
warnings.filterwarnings("ignore")


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

print('==================================================================================')
print("Welcome to Image-Purge")
ASCII_art_1 = pyfiglet.figlet_format('Image-Purge',font='slant')
print(ASCII_art_1)



from keras.models import load_model
from keras_preprocessing.image import load_img
from keras_preprocessing.image import img_to_array

model = load_model('models/model4.h5')

parser = argparse.ArgumentParser(description="Classify and delete images using a trained model")
parser.add_argument("image_dir", help="Path to the directory containing images to be purged")
args = parser.parse_args()

def predict_image(image_path, model):
    image = load_img(image_path, target_size=(224, 224))
    image = np.array(image)
    image = image / 255.0
    image = image.reshape(1, 224, 224, 3)
    label = model.predict(image, verbose=0)
    if label > 0.5:
        return "Notes"
    else:
        return "Not Notes"

result_list = []
for filename in os.listdir(args.image_dir):
    image_path = os.path.join(args.image_dir, filename)
    label = predict_image(image_path, model)
    print(f"Image {filename}: {label}")
    result_list.append((image_path, label))
print('==================================================================================')
print(' ')
print("Which Images do you want to delete?")
print("1. All the Not Notes images")
print("2. All the Notes images")
print("3. None of the images")
print(' ')
user_input = input("Enter your choice (1/2/3):")
if user_input == "1":
    for image_path, label in result_list:
        if label == "Not Notes":
            os.remove(image_path)
            print(f"Deleted {image_path}")
elif user_input == "2":
    for image_path, label in result_list:
        if label == "Notes":
            os.remove(image_path)
            print(f"Deleted {image_path}")
else:
    print("No images were deleted.")

print("==================================================================================")
import ascii_magic
my_art = ascii_magic.from_image_file('img/meme.png', columns= 82)
ascii_magic.to_terminal(my_art)
print('==================================================================================')




