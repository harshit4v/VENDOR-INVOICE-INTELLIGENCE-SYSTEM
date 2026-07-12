import joblib
import pandas as pd
import numpy as np
import os

# Model Path
MODEL_PATH = "models/predict_freight_model.pkl"


def load_model(model_path: str = MODEL_PATH):
    print("\n📦 Loading Freight Prediction Model...")

    if not os.path.exists(model_path):
        print(f"❌ Model file not found!")
        print(f"📁 Expected Path: {model_path}")
        return None

    try:
        model = joblib.load(model_path)
        print("✅ Model loaded successfully.")
        print(f"📁 Model Path: {model_path}")
        return model

    except Exception as e:
        print(f"❌ Error loading model: {e}")
        return None


def predict_freight_cost(input_data):

    model = load_model()

    if model is None:
        return None

    print("\n📥 Reading Input Data...")

    # Create DataFrame
    input_df = pd.DataFrame(input_data)

    print("✅ Input received successfully.")
    print(f"📊 Total Records for Prediction: {len(input_df)}")

    try:
        print("\n🧠 Predicting Freight Cost...")

        # Model expects only Dollars
        data_values = input_df[['Dollars']].values

        predictions = model.predict(data_values)

        input_df["Predicted_Freight"] = (
            np.array(predictions)
            .flatten()
            .round(2)
        )

        print("✅ Prediction completed successfully!")

        return input_df

    except Exception as e:
        print(f"❌ Prediction Error: {e}")
        return None


if __name__ == "__main__":

    print("=" * 60)
    print("🚀 Freight Cost Prediction Started")
    print("=" * 60)

    sample_data = {
        "Quantity": [18500],
        "Dollars": [9000]
    }

    result = predict_freight_cost(sample_data)

    if result is not None:
        print("\n" + "=" * 60)
        print("🎉 PREDICTION COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        print(result)
        print("=" * 60)
    else:
        print("\n❌ Prediction failed.")