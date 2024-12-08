from src.cyclone_analysis import CyclonePreheaterAnalysis

if __name__ == "__main__":
    # Paths
    input_file_path = "data/data.xlsx"  # Replace with your actual file path
    output_file_path = "output/Anomalies_Detected.csv"

    # Initialize the analysis object
    analysis = CyclonePreheaterAnalysis(file_path=input_file_path, threshold=3)

    # Step 1: Load and preprocess the data
    print("Loading and preprocessing data...")
    analysis.load_data()

    # Step 2: Detect anomalies
    print("Detecting anomalies...")
    analysis.detect_anomalies()

    # Step 3: Save the results
    print("Saving results...")
    analysis.save_results(output_path=output_file_path)
    print(f"Results saved to {output_file_path}")
