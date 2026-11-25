"""Basic tests. They will pass as you implement the required functions."""
import pandas as pd
import pytest
from src.analysis import summarize_dataframe, clean_orders, calculate_metrics


def test_summarize_dataframe_reports_missing_values():
    df = pd.DataFrame({"a": [1, None, 3], "b": ["x", "y", "y"]})
    result = summarize_dataframe(df)
    assert set(["column", "dtype", "missing_count", "missing_percent", "unique_count"]).issubset(result.columns)
    assert int(result.loc[result["column"] == "a", "missing_count"].iloc[0]) == 1


def test_clean_orders_does_not_modify_original():
    orders = pd.DataFrame({
        "order_id": [1, 1, 2], "customer_id": [10, 10, 99],
        "product_id": [20, 20, 20], "order_date": pd.to_datetime(["2025-01-01"]*3),
        "quantity": [1, 1, 2], "unit_price": [10, 10, 10],
        "status": ["Complete", "Complete", "Complete"]
    })
    customers = pd.DataFrame({"customer_id": [10]})
    products = pd.DataFrame({"product_id": [20]})
    original = orders.copy(deep=True)
    clean_orders(orders, customers, products)
    pd.testing.assert_frame_equal(orders, original)


def test_calculate_metrics_returns_expected_keys():
    cleaned = pd.DataFrame({
        "order_id": [1, 2], "customer_id": [10, 10], "product_id": [20, 20],
        "order_date": pd.to_datetime(["2025-01-01", "2025-01-02"]),
        "quantity": [2, 1], "unit_price": [10, 10], "status": ["Complete", "Complete"]
    })
    products = pd.DataFrame({"product_id": [20], "unit_cost": [4]})
    result = calculate_metrics(cleaned, products)
    expected = {"total_orders", "total_units", "revenue", "cost", "gross_profit", "profit_margin_percent", "average_order_value"}
    assert expected.issubset(result.keys())
    assert result["revenue"] == pytest.approx(30)
