import os

import numpy as np

from tensorflow.keras.preprocessing import image

from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import (

    Rescaling,
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense,
    Dropout
)


# Rebuild SAME model architecture
model = Sequential([

    Rescaling(

        1./255,

        input_shape=(224,224,3)
    ),

    Conv2D(

        32,

        (3,3),

        activation='relu'
    ),

    MaxPooling2D(),

    Conv2D(

        64,

        (3,3),

        activation='relu'
    ),

    MaxPooling2D(),

    Conv2D(

        128,

        (3,3),

        activation='relu'
    ),

    MaxPooling2D(),

    Conv2D(

        256,

        (3,3),

        activation='relu'
    ),

    MaxPooling2D(),

    Flatten(),

    Dense(

        256,

        activation='relu'
    ),

    Dropout(0.5),

    Dense(

        20,

        activation='softmax'
    )
])


# Absolute path to weights file
BASE_DIR = os.path.dirname(

    os.path.abspath(__file__)
)

weights_path = os.path.join(

    BASE_DIR,

    "weights.weights.h5"
)


# Load weights
model.load_weights(weights_path)


classes = [

    'Alstonia Scholaris_diseased',
    'Alstonia Scholaris_healthy',

    'Arjun_diseased',
    'Arjun_healthy',

    'Chinnar_diseased',
    'Chinnar_healthy',

    'Gauva_diseased',
    'Gauva_healthy',

    'Jamun_diseased',
    'Jamun_healthy',

    'Jatropha_diseased',
    'Jatropha_healthy',

    'Lemon_diseased',
    'Lemon_healthy',

    'Mango_diseased',
    'Mango_healthy',

    'Pomegranate_diseased',
    'Pomegranate_healthy',

    'Pongamia Pinnata_diseased',
    'Pongamia Pinnata_healthy'
]


def predict_disease(image_path):

    img = image.load_img(

        image_path,

        target_size=(224,224)
    )

    img_array = image.img_to_array(img)

    img_array = np.expand_dims(

        img_array,

        axis=0
    )

    prediction = model.predict(

        img_array
    )

    class_index = np.argmax(

        prediction
    )

    disease = classes[class_index]

    confidence = float(

        np.max(prediction) * 100
    )

    return disease, confidence