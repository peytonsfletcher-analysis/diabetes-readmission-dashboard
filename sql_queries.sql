-- Overall readmission distribution
SELECT
  readmitted,
  COUNT(*) AS total_encounters
FROM cleaned_diabetes_data
GROUP BY readmitted
ORDER BY total_encounters DESC;

-- Readmitted within 30 days rate
SELECT
  ROUND(100.0 * SUM(readmitted_30_flag) / COUNT(*), 2) AS readmitted_30_rate_pct
FROM cleaned_diabetes_data;

-- Readmission within 30 days by HbA1c result
SELECT
  a1cresult,
  COUNT(*) AS total_encounters,
  ROUND(100.0 * SUM(readmitted_30_flag) / COUNT(*), 2) AS readmitted_30_rate_pct
FROM cleaned_diabetes_data
GROUP BY a1cresult
ORDER BY total_encounters DESC;

-- Readmission within 30 days by time in hospital
SELECT
  time_in_hospital,
  COUNT(*) AS total_encounters,
  ROUND(100.0 * SUM(readmitted_30_flag) / COUNT(*), 2) AS readmitted_30_rate_pct
FROM cleaned_diabetes_data
GROUP BY time_in_hospital
ORDER BY time_in_hospital;
