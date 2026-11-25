from pathlib import Path
from src.analysis import load_data, summarize_dataframe, clean_orders, calculate_metrics


def main():
    data_dir = Path(__file__).parent / "data"
    data = load_data(data_dir)

    print("\\n=== DATA QUALITY: ORDERS ===")
    print(summarize_dataframe(data["orders"]).to_string(index=False))

    cleaned = clean_orders(data["orders"], data["customers"], data["products"])
    metrics = calculate_metrics(cleaned, data["products"])

    print("\\n=== BUSINESS METRICS ===")
    for name, value in metrics.items():
        print(f"{name}: {value}")


if __name__ == "__main__":
    main()
