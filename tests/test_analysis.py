import pytest
from src.analysis import CyclonePreheaterAnalysis

def test_load_data():
    analysis = CyclonePreheaterAnalysis("data/data.xlsx")
    analysis.load_data()
    assert not analysis.data.empty, "Data should be loaded successfully."

def test_detect_anomalies():
    analysis = CyclonePreheaterAnalysis("data/data.xlsx", threshold=3)
    analysis.load_data()
    analysis.detect_anomalies()
    assert not analysis.anomalies.empty, "Anomalies should be detected."
