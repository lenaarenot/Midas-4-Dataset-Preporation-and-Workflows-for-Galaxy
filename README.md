# Repository Overview
**MiDAS 4 Dataset Preparation and Workflows for Galaxy**

This repository contains all resources used for processing and analysing the MiDAS 4 wastewater treatment plant dataset within the Galaxy framework.

**Contents**
* **Python Code**: Scripts for data preparation and format conversion.
* **Galaxy Workflows**: Automated pipelines used for data processing.
* **Modified Dataset Files**: Adjusted input files for reproducibility.

**Dataset Modifications** <br />
To align the raw MiDAS 4 dataset for analysis, several adjustments were made. These can be found in the _python_snippets_ folder:

* **ASV Table**: Split into smaller sheets, merged related columns, and converted to TSV format.
* **Taxonomy Table**: Standardised ASV identifiers for consistency. Additionally, the header of the first column was manually changed to "ASV."
* **Metadata Table**: Reformatted dates, replaced empty values with "NA" in key columns, and ensured uniform process type naming. Additionally, rows with missing continent, country, and related information were manually removed.

These modifications enabled the dataset to be processed effectively within Galaxy.

**Galaxy Workflows** <br />
The following Galaxy workflows were used for dataset processing and analysis. Each workflow automates a specific step in data transformation or visualisation:

**Pre-processing Workflows**

* _ampvis2__1.half_no_DA_features_: Prepares input data without differential abundance (DA) features.
* _ampvis2__with_MaAsLin2_1.half_all_DA_features_: Prepares input data including all DA features.
* _ampvis2__ordination_with_MaAsLin2_1.half_C_against_Anammox_: Prepares specific DA features for ordination analysis (C vs Anammox).
* _ampvis2__ordination_with_MaAsLin2_1.half_C_against_C_N_DN_P_: Prepares specific DA features for ordination analysis (C vs C_N_DN_P).
* _ampvis2__heatmap_boxplot_with_MaAsLin2_1.half_C_against_Anammox_: Prepares specific specific DA features for heatmap and boxplot visualisation (C vs Anammox).
* _ampvis2__heatmap_boxplot_with_MaAsLin2_1.half_C_against_C_N_DN_P_: Prepares specific DA features for heatmap and boxplot visualisation (C vs C_N_DN_P).

**Visualisation Workflows**

* _ampvis2__ordination_no_DA_features_2.half_: Performs ordination analysis without DA features.
* _ampvis2__heatmap_boxplot_no_DA_features_2.half_: Generates heatmap and boxplot without DA features.
* _ampvis2__ordination_after_MaAsLin_2.half_: Performs ordination analysis for all or specific DA features.
* _ampvis2__heatmap_boxplot_after_MaAsLin_2.half_: Generates heatmap and boxplot for all or specific DA features.

Each workflow is available on Galaxy Europe for reproducibility. 
