# **Cyclone Preheater Anomaly Detection**

## **Overview**

This project aims to analyze operational data from a cyclone preheater, part of an industrial process, to identify periods of abnormal behavior. The analysis is based on a **Z-score anomaly detection** approach, which identifies outliers in multiple parameters over a three-year period. The results provide actionable insights into potential system inefficiencies or failures, which can help optimize operations and enhance maintenance planning.

---

## **Motivation**

The cyclone preheater is a critical component in industrial processes, and its efficient operation is vital for productivity and safety. Abnormalities in parameters such as temperature and draft pressures can indicate potential issues such as:

* Equipment wear or malfunction.  
* Suboptimal operating conditions.  
* Early warning signs of catastrophic failure.

The primary motivation for this project was:

1. **Preventative Maintenance**: Detect abnormalities early to reduce downtime and repair costs.  
2. **Operational Efficiency**: Improve the performance of the cyclone preheater by identifying deviations from normal operations.  
3. **Data-Driven Insights**: Leverage historical data to predict and mitigate risks.

---

## **Dataset Description**

The dataset contains operational parameters recorded every 5 minutes over three years. It includes the following variables:

1. **Cyclone\_Inlet\_Gas\_Temp**: Temperature of hot gas entering the cyclone.  
2. **Cyclone\_Material\_Temp**: Temperature of the material exiting the cyclone.  
3. **Cyclone\_Outlet\_Gas\_draft**: Gas draft (pressure) at the cyclone outlet.  
4. **Cyclone\_cone\_draft**: Gas draft (pressure) at the cone section of the cyclone.  
5. **Cyclone\_Gas\_Outlet\_Temp**: Gas temperature leaving the cyclone.  
6. **Cyclone\_Inlet\_Draft**: Gas draft (pressure) at the inlet of the cyclone.  
7. **time**: Timestamp of each recorded observation.

---

## **Methodology**

### **1\. Preprocessing**

* Converted the `time` column to a datetime format for accurate time-based analysis.  
* Ensured that all numeric columns were converted to float data types.  
* Removed rows containing missing or invalid values to ensure a clean dataset for analysis.

### **2\. Anomaly Detection**

* Used **Z-score analysis** to standardize each numeric column. The Z-score indicates how many standard deviations a value is from the mean.  
* Applied a threshold of **3 standard deviations** to detect anomalies. Any value exceeding this threshold was flagged as an anomaly.

### **3\. Output**

* Combined all detected anomalies into a single dataset, including:  
  * The timestamp of the anomaly (`time`).  
  * The parameter in which the anomaly was detected.  
  * The Z-score value, indicating the severity of the anomaly.

---

## **Results**

### **Sample Output**

The following is a sample from the `Anomalies_Detected.csv` file:

| time | Cyclone\_Inlet\_Gas\_Temp | Cyclone\_Inlet\_Gas\_Temp\_zscore | Cyclone\_Material\_Temp | Cyclone\_Material\_Temp\_zscore | Cyclone\_Outlet\_Gas\_draft | Cyclone\_Outlet\_Gas\_draft\_zscore | Cyclone\_cone\_draft | Cyclone\_cone\_draft\_zscore | Cyclone\_Gas\_Outlet\_Temp | Cyclone\_Gas\_Outlet\_Temp\_zscore | Cyclone\_Inlet\_Draft | Cyclone\_Inlet\_Draft\_zscore |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 2018-08-01 00:05:00 |  |  |  |  |  |  | \-459.31 | \-3.27 |  |  |  |  |
| 2018-09-15 08:35:00 |  |  |  |  |  |  | 488.86 | 7.25 |  |  |  |  |
| 2018-09-15 08:45:00 |  |  |  |  |  |  | 137.39 | 3.35 |  |  |  |  |
| 2018-08-01 00:05:00 |  |  |  |  |  |  |  |  |  |  | \-396.37 | \-3.29 |
| 2018-08-23 02:15:00 |  |  |  |  |  |  |  |  |  |  | \-391.08 | \-3.22 |

### **Insights**

1. **Cyclone Cone Draft**:  
   * Detected two severe anomalies: **488.86 (Z \= 7.25)** and **137.39 (Z \= 3.35)**.  
   * These values indicate significant deviations from normal operation, potentially caused by equipment malfunctions or process inefficiencies.  
2. **Cyclone Inlet Draft**:  
   * Found two anomalies: **\-396.37 (Z \= \-3.29)** and **\-391.08 (Z \= \-3.22)**.  
   * Negative drafts at this magnitude might suggest improper airflow or blockages.  
3. **Cyclone Outlet Draft**:  
   * Significant anomaly detected at **\-459.31 (Z \= \-3.27)**, pointing to an unusual drop in outlet pressure.

---

## **How to Use the Project**

### **Setup**

1. Clone or download the project.  
2. Place your input file (`data.xlsx`) in the `data/` directory.

Install dependencies:  
bash  
Copy code  
`python3 -m venv venv`  
`source venv/bin/activate`  
`pip install -r requirements.txt`

3. 

### **Run the Analysis**

Run the following command to execute the analysis:

bash  
Copy code  
`python Assignment_ALGO8.py`

### **Output**

* The results are saved in the `output/Anomalies_Detected.csv` file.

---

## **Conclusion**

This project successfully detects anomalies in the cyclone preheater's operation, providing insights into abnormal conditions. These results can assist in:

* Proactive maintenance scheduling.  
* Identifying inefficiencies and optimizing operations.  
* Enhancing overall process reliability.

---

## **Future Work**

1. **Visualization**: Add graphical representations of anomalies.  
2. **Advanced Models**: Implement machine learning models like Isolation Forest or LSTM for anomaly detection.  
3. **Integration**: Combine results with SCADA systems for real-time monitoring.

