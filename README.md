# NEXT-CYPInh

NEXT-CYPInh is an open-source software specifically designed for predicting potential inhibitors of Cytochrome P450 enzymes based on our existing best models.

## Usage

### 1. Single Molecule Prediction

First copy/text the **SMILES** of the molecule. Next, select the CYP450 isoforms you aim to predict in the **"Select Prediction Models"** section. Once you have made your selection, click the **"Submit Prediction"** button to run the prediction. The prediction results will be displayed directly in the table below. If the input molecule exists in the training set, its true label will cover the predicted value, and a '*' will be appended to the result. You can also download the results by clicking the **"Save Results"** button below the table. The results displayed in the table can be cleared using the **"Clear Results"** button. Note that the downloaded file will contain all the results currently displayed in the table.

### 2. Batch Prediction

In this module, you can predict a batch of molecules simultaneously. Click the **"Browse"** button to upload a file in **TXT** or **SDF** format that contains the input molecules. The subsequent steps are the same as those in the above module.

## License

This software is powered by the PySide6 library (LGPLv3) and is released under the BSD 3-Clause License.