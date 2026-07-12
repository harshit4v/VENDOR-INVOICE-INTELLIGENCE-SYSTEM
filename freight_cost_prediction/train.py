import joblib
from pathlib import Path

from data_preprocessing import (
    load_vendor_invoice_data,
    prepare_features,
    split_data
)

from model_evaluation import (
    train_linear_regression,
    train_decision_tree,
    train_random_forest,
    evaluate_model
)


def main():

    print("=" * 60)
    print("🚀 Freight Prediction Model Training Started")
    print("=" * 60)

    # Paths
    db_path = r"/Users/Asus/Desktop/VENDOR INVOICE INTELLIGENT SYSTEM/data/inventory.db"
    model_dir = Path("models")
    model_dir.mkdir(exist_ok=True)

    print(f"\n📂 Database Path: {db_path}")
    print(f"📁 Model Directory: {model_dir}")

    # Load data
    print("\n📥 Loading vendor invoice data...")
    df = load_vendor_invoice_data(db_path)
    print(f"✅ Dataset loaded successfully.")
    print(f"📊 Total Records: {len(df)}")

    # Prepare features
    print("\n🛠 Preparing features and target...")
    X, Y = prepare_features(df)
    print("✅ Feature preparation completed.")

    # Split data
    print("\n🔀 Splitting dataset into training and testing sets...")
    X_train, X_test, Y_train, Y_test = split_data(X, Y)
    print("✅ Data split completed.")

    # Train models
    print("\n📈 Training Machine Learning Models...")

    print("   ➜ Training Linear Regression...")
    lr_model = train_linear_regression(X_train, Y_train)
    print("   ✅ Linear Regression completed.")

    print("\n   ➜ Training Decision Tree Regression...")
    dt_model = train_decision_tree(X_train, Y_train)
    print("   ✅ Decision Tree Regression completed.")

    print("\n   ➜ Training Random Forest Regression...")
    rf_model = train_random_forest(X_train, Y_train)
    print("   ✅ Random Forest Regression completed.")

    # Evaluate models
    print("\n📊 Evaluating Models...\n")

    results = []

    results.append(
        evaluate_model(
            lr_model,
            X_test,
            Y_test,
            "Linear Regression"
        )
    )

    results.append(
        evaluate_model(
            dt_model,
            X_test,
            Y_test,
            "Decision Tree Regression"
        )
    )

    results.append(
        evaluate_model(
            rf_model,
            X_test,
            Y_test,
            "Random Forest Regression"
        )
    )

    # Select best model (Lowest MAE)
    best_model_info = min(results, key=lambda x: x["MAE"])
    best_model_name = best_model_info["model"]

    model_mapping = {
        "Linear Regression": lr_model,
        "Decision Tree Regression": dt_model,
        "Random Forest Regression": rf_model
    }

    best_model = model_mapping[best_model_name]

    # Save best model
    model_path = model_dir / "predict_freight_model.pkl"
    joblib.dump(best_model, model_path)

    # Final Summary
    print("\n" + "=" * 60)
    print("🎉 MODEL TRAINING COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print(f"🏆 Best Model      : {best_model_name}")
    print(f"📉 Best MAE        : {best_model_info['MAE']:.4f}")
    print(f"📈 Best RMSE       : {best_model_info['RMSE']:.4f}")
    print(f"📊 Best R² Score   : {best_model_info['R2']:.4f}")
    print(f"💾 Model Saved At  : {model_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()