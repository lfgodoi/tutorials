# Importing packages
import tensorflow as tf
import numpy as np
import pickle
import psycopg2

# Generating some random data
n_samples = 1000
n_features = 9
X = np.random.random((n_samples, n_features))
y = np.random.choice([0, 1], size=n_samples, p=[.3, .7])

# Instantiating a simple neural network model
original_model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(n_features,)),
  tf.keras.layers.Dense(32, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(16, activation='relu'),
  tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compiling the model
original_model.compile(optimizer='adam',
                       loss='binary_crossentropy',
                       metrics=['accuracy'])

# Training the model
original_model.fit(X, y, epochs=10)

# Evatuating the model
original_loss, original_accuracy = original_model.evaluate(X, y)

# Serializing the model
pickled_original_model = pickle.dumps(original_model)

# Connecting to the database
conn = psycopg2.connect(
           host="localhost",
           database="db",
           port=5432,
           user="postgres",
           password="postgres")

# Saving the serialized model in the database
cursor = conn.cursor()
cursor.execute("INSERT INTO models (data) VALUES (%s) RETURNING id", 
               (pickled_original_model,))
conn.commit()

# Getting the ID from the saved model
model_id = cursor.fetchone()[0]

# Reading the saved model
cursor.execute("SELECT data FROM models WHERE id = %s LIMIT 1", (model_id,))
pickled_retrieved_model = cursor.fetchone()[0]

# Deserializing the retrieved model
retrieved_model = pickle.loads(pickled_retrieved_model)

# Evatuating the retrieved model
retrieved_loss, retrieved_accuracy = original_model.evaluate(X, y)

# Comparing the original and the retrieved model
print(f"Original loss: {original_loss}")
print(f"Retrieved loss: {retrieved_loss}")
print(f"Original accuracy: {original_accuracy}")
print(f"Retrieved accuracy: {retrieved_accuracy}")

# Comparing a piece of the weights
print(f"Some weights of original model: {original_model.weights[0][0]}\n")
print(f"Some weights of retrieved model: {retrieved_model.weights[0][0]}")

# Closing the database connection
conn.close()
