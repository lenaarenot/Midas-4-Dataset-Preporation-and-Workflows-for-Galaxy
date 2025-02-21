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
