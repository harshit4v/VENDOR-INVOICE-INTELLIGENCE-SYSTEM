import joblib
import pandas as pd
import numpy as np
from pathlib import Path

# ============================================================
# Project Paths
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "predict_flag_invoice.pkl"
SCALER_PATH = BASE_DIR / "models" / "scaler.pkl"


def load_artifacts():
    """Load trained model and scaler."""

    print("\n📦 Loading ML Artifacts...")

    if not MODEL_PATH.exists():
        print(f"❌ Model not found!")
        print(f"📁 Expected Path: {MODEL_PATH}")
        return None, None

    if not SCALER_PATH.exists():
        print(f"❌ Scaler not found!")
        print(f"📁 Expected Path: {SCALER_PATH}")
        return None, None

    try:
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)

        print("✅ Model loaded successfully.")
        print("✅ Scaler loaded successfully.")
        print(f"📁 Model Path : {MODEL_PATH}")
        print(f"📁 Scaler Path: {SCALER_PATH}")

        return model, scaler

    except Exception as e:
        print(f"❌ Error loading artifacts: {e}")
        return None, None


# Load once
MODEL, SCALER = load_artifacts()


def predict_invoice_flag(input_data):

    if MODEL is None or SCALER is None:
        return None

    print("\n📥 Reading Input Data...")

    input_df = pd.DataFrame(input_data)

    print("✅ Input received successfully.")
    print(f"📊 Records to Predict: {len(input_df)}")

    try:

        print("\n⚙ Preparing Features...")

        features = [
            "invoice_quantity",
            "invoice_dollars",
            "Freight",
            "total_item_quantity",
            "total_item_dollars"
        ]

        input_ready = input_df[features]

        print("✅ Feature selection completed.")

        print("\n📏 Scaling Features...")
        input_scaled = SCALER.transform(input_ready)

        print("✅ Scaling completed.")

        print("\n🧠 Predicting Invoice Risk...")

        predictions = MODEL.predict(input_scaled)

        input_df["Predicted_Flag"] = (
            np.array(predictions)
            .flatten()
            .astype(int)
        )

        print("✅ Prediction completed successfully!")

        return input_df

    except Exception as e:
        print(f"\n❌ Prediction Error: {e}")
        print(f"📝 Input Columns: {list(input_df.columns)}")
        return None


if __name__ == "__main__":

    print("=" * 60)
    print("🚀 Invoice Flag Prediction Started")
    print("=" * 60)

    sample_data = {
        "invoice_quantity": [50],
        "invoice_dollars": [1200.0],
        "Freight": [45.0],
        "total_item_quantity": [50],
        "total_item_dollars": [1195.0]
    }

    result = predict_invoice_flag(sample_data)

    if result is not None:

        print("\n" + "=" * 60)
        print("🎉 PREDICTION COMPLETED SUCCESSFULLY!")
        print("=" * 60)

        print(result)

        flag = result["Predicted_Flag"].iloc[0]

        print("\n📋 Prediction Summary")
        print("-" * 60)

        if flag == 1:
            print("🚩 Invoice Status : HIGH RISK")
            print("⚠ Recommendation : Review this invoice before approval.")
        else:
            print("✅ Invoice Status : LOW RISK")
            print("✔ Recommendation : Invoice appears normal.")

        print("=" * 60)

    else:
        print("\n❌ Prediction failed.")