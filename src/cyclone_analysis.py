import pandas as pd
from scipy.stats import zscore
import os

class CyclonePreheaterAnalysis:
    def __init__(self, file_path, threshold=3):
        self.file_path = file_path
        self.threshold = threshold
        self.data = None
        self.anomalies = None

    def load_data(self):
        """Load and preprocess the data."""
        try:
            self.data = pd.read_excel(self.file_path, sheet_name='internship-data-1')
            self.data['time'] = pd.to_datetime(self.data['time'], errors='coerce')
            numeric_columns = [
                'Cyclone_Inlet_Gas_Temp',
                'Cyclone_Material_Temp',
                'Cyclone_Outlet_Gas_draft',
                'Cyclone_cone_draft',
                'Cyclone_Gas_Outlet_Temp',
                'Cyclone_Inlet_Draft'
            ]
            for col in numeric_columns:
                self.data[col] = pd.to_numeric(self.data[col], errors='coerce')
            self.data.dropna(inplace=True)
            print("Data successfully loaded and preprocessed.")
        except Exception as e:
            print(f"Error in loading data: {e}")

    def detect_anomalies(self):
        """Detect anomalies using Z-score."""
        try:
            numeric_columns = [
                'Cyclone_Inlet_Gas_Temp',
                'Cyclone_Material_Temp',
                'Cyclone_Outlet_Gas_draft',
                'Cyclone_cone_draft',
                'Cyclone_Gas_Outlet_Temp',
                'Cyclone_Inlet_Draft'
            ]
            anomalies = []

            for col in numeric_columns:
                self.data[col + '_zscore'] = zscore(self.data[col])
                column_anomalies = self.data[abs(self.data[col + '_zscore']) > self.threshold]
                anomalies.append(column_anomalies[['time', col, col + '_zscore']])

            self.anomalies = pd.concat(anomalies, ignore_index=True)
            print("Anomalies successfully detected.")
        except Exception as e:
            print(f"Error in detecting anomalies: {e}")

    def save_results(self, output_path):
        """Save anomalies to a CSV file."""
        try:
            output_dir = os.path.dirname(output_path)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            self.anomalies.to_csv(output_path, index=False)
            print(f"Anomalies saved to {output_path}")
        except Exception as e:
            print(f"Error in saving results: {e}")
