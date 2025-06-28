# Heart Disease Prediction Project

This project is a web application that predicts the likelihood of a person having heart disease based on various medical attributes. It utilizes a Logistic Regression model trained on a dataset of patient information.

## Project Structure

- `app.py`: The main Streamlit application file. It handles user input, runs the prediction model, and displays the results.
- `Heart Disease Prediction Projects.ipynb`: A Jupyter Notebook containing the data loading, preprocessing, model training, and evaluation steps.
- `heart_disease_data.csv`: The dataset used to train the prediction model.
- `requirements.txt`: A list of Python dependencies required to run the project.
- `README.md`: This file, providing an overview of the project.
- `.devcontainer/`: Folder containing configuration for development containers.

## Features

- **User-friendly Interface:** Provides a simple web form for users to input their medical information.
- **Instant Prediction:** Delivers real-time predictions on the likelihood of heart disease.
- **Model Transparency:** The Jupyter Notebook (`Heart Disease Prediction Projects.ipynb`) details the model training process and performance metrics.

## Dataset

The prediction model is trained on the `heart_disease_data.csv` dataset. The dataset includes the following attributes:

| Column     | Description                                                                                         |
|------------|---------------------------------------------------------------------------------------------------|\
| **age**      | Age of the patient (in years)                                                                    |
| **sex**      | Gender of the patient (0 = female, 1 = male)                                                     |
| **cp**       | Chest pain type:                                                                                  |
|              | - 0 = typical angina                                                                             |
|              | - 1 = atypical angina                                                                            |
|              | - 2 = non-anginal pain                                                                           |
|              | - 3 = asymptomatic                                                                              |
| **trestbps** | Resting blood pressure (in mm Hg)                                                                |
| **chol**     | Serum cholesterol level (in mg/dl)                                                                |
| **fbs**      | Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)                                            |
| **restecg**  | Resting electrocardiographic results:                                                           |
|              | - 0 = normal                                                                                     |
|              | - 1 = having ST-T wave abnormality                                                              |
|              | - 2 = showing probable or definite left ventricular hypertrophy by Estes' criteria                |
| **thalach**  | Maximum heart rate achieved                                                                       |
| **exang**    | Exercise induced angina (1 = yes, 0 = no)                                                        |
| **oldpeak**  | ST depression induced by exercise relative to rest                                              |
| **slope**    | The slope of the peak exercise ST segment:                                                       |
|              | - 0 = downsloping                                                                               |
|              | - 1 = flat                                                                                       |
|              | - 2 = upsloping                                                                                |
| **ca**       | Number of major vessels colored by fluoroscopy (0-3)                                             |
| **thal**     | Thalassemia status:                                                                              |
|              | - 0 = normal                                                                                     |
|              | - 1 = fixed defect                                                                              |
|              | - 2 = reversible defect                                                                         |
| **target**   | Presence of heart disease (1 = yes, 0 = no)                                                      |

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```
2.  Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).
3.  Fill in the required medical information in the form.
4.  Click the "Predict" button to see the prediction.

## Model Details

The prediction model is a Logistic Regression classifier implemented using the scikit-learn library. The model is trained on the `heart_disease_data.csv` dataset. For details on data preprocessing, model training, and evaluation, please refer to the `Heart Disease Prediction Projects.ipynb` notebook.

**Model Performance:**
-   **Training Accuracy:** Approximately 85.12%
-   **Test Accuracy:** Approximately 81.97%

*(These accuracy scores are based on the last run in the provided notebook and `app.py`.)*

## Contributing

Contributions are welcome! If you have suggestions for improvements or find any issues, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

## License

This project is open-source and available under the [MIT License](LICENSE.txt) (assuming MIT, if no license file exists, this section can be updated or removed).

---

*This README was generated by an AI assistant.*
