from tensorflow.keras.models import load_model


# Load old model
model = load_model(

    "cnn/disease_model.h5",

    compile=False
)


# Save in new format
model.save(

    "cnn/fixed_model.keras"
)

print("Model converted successfully!")