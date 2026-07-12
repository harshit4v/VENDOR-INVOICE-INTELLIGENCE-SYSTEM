from data_preprocessing import (
    load_invoice_data,
    apply_labels,
    split_data,
    scale_features
)
from modeling_evaluation import (
    train_random_forest,
    evaluate_classifier
)
import joblib

FEATURES = [
    "invoice_quantity",
    "invoice_dollars",
    "Freight",
    "total_item_quantity",
    "total_item_dollars"
]

TARGET = "flag_invoice"


def main():

    print("=" * 60)
    print("🚀 Vendor Invoice Fraud Detection Model Training Started")
    print("=" * 60)

    # Load data
    print("\n📂 Loading dataset...")
    df = load_invoice_data()
    print(f"✅ Dataset loaded successfully. Total records: {len(df)}")

    # Apply labels
    print("\n🏷️ Applying labels...")
    df = apply_labels(df)
    print("✅ Labels applied successfully.")

    # Split data
    print("\n🔀 Splitting dataset into training and testing sets...")
    X_train, X_test, y_train, y_test = split_data(
        df,
        FEATURES,
        TARGET
    )
    print("✅ Data split completed.")

    # Scale features
    print("\n⚙️ Scaling features...")
    X_train_scaled, X_test_scaled = scale_features(
        X_train,
        X_test,
        "models/scaler.pkl"
    )
    print("✅ Feature scaling completed.")
    print("✅ Scaler saved at: models/scaler.pkl")

    # Train model
    print("\n🌲 Training Random Forest Classifier...")
    grid_search = train_random_forest(X_train_scaled, y_train)

    print("✅ Training completed.")
    print(f"🏆 Best Parameters: {grid_search.best_params_}")

    # Evaluate model
    print("\n📊 Evaluating model...\n")
    evaluate_classifier(
        grid_search.best_estimator_,
        X_test_scaled,
        y_test,
        "Random Forest Classifier"
    )

    # Save model
    model_path = "models/predict_flag_invoice.pkl"
    joblib.dump(grid_search.best_estimator_, model_path)

    print("\n" + "=" * 60)
    print("🎉 MODEL TRAINING COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print(f"✅ Best Model : {type(grid_search.best_estimator_).__name__}")
    print(f"📁 Model Saved : {model_path}")
    print("💾 Scaler Saved: models/scaler.pkl")
    print("=" * 60)


if __name__ == "__main__":
    main()