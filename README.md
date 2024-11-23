# Self-Medi Care

**Self-Medi Care** is a web-based platform designed to predict potential diseases based on symptoms entered by users. The platform provides actionable insights, such as recommended medications, diets, precautions, and workouts, empowering users to take control of their health.

---

## Features

1. **Disease Prediction**
   - Powered by a machine learning model trained on comprehensive datasets.
   - Predicts diseases based on symptoms entered by the user.

2. **Health Guidance**
   - Provides disease descriptions, medications, dietary advice, precautions, and workout recommendations.

3. **Speech Recognition**
   - Enables voice input for entering symptoms using the Web Speech API.

4. **Interactive Blog**
   - Offers health-related blog posts to keep users informed and educated.

5. **PDF Prescription Report**
   - Generates a downloadable PDF report with the predicted disease, precautions, medications, diets, and workouts.

---

## Tech Stack

### Frontend
- **HTML5**
- **CSS3**
- **JavaScript**
- **Bootstrap**

### Backend
- **Flask** (Python Framework)
- **FPDF** (PDF generation)

### Machine Learning
- **Decision Tree Classifier**
- Libraries: `numpy`, `pandas`

### Database
- CSV files for:
  - Disease descriptions
  - Symptoms
  - Precautions
  - Medications
  - Diets
  - Workout recommendations

---

## System Architecture

1. **User Input:** Users can input symptoms via text or speech.
2. **Prediction Engine:** Symptoms are processed by a Decision Tree Classifier model to predict potential diseases.
3. **Data Retrieval:** Relevant data (e.g., medications, precautions) is fetched from CSV datasets.
4. **Output:** Results are displayed on the web interface and a downloadable prescription PDF is generated.

---

## How to Run the Project

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/AmritaSinha8976/Self-Medi-Care
   cd Self-Medi-Care
   ```

2. **Set Up Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: .\env\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask App:**
   ```bash
   python main.py
   ```

5. **Access the Application:**
   Open your browser and navigate to `http://127.0.0.1:5000/`.

---

## Project Files

- **`main.py`**: Core Flask application file.
- **Templates**:
  - `index.html`: Homepage for symptom entry and results.
  - `about.html`: About the platform.
  - `contact.html`: Contact details.
  - `developer.html`: Information about the contributors.
  - `blog.html`: Health-related blog content.
- **Datasets**:
  - `symptoms_df.csv`: Symptom descriptions.
  - `precautions_df.csv`: Precautions for diseases.
  - `description.csv`: Disease descriptions.
  - `medications.csv`: Suggested medications.
  - `diets.csv`: Recommended diets.
  - `workout_df.csv`: Workout plans.
- **Models**:
  - `svc.pkl`: Pre-trained Decision Tree Classifier model.

---

### Contributors

- [Amrita Sinha](https://github.com/AmritaSinha8976)
  - Lead model development, optimized Decision Tree, backend setup, and frontend integration.

- [Surya Sah](https://github.com/SuryaSahh)
  - Data preparation, model validation, prediction routes, and frontend output integration.

- [Moha](https://github.com/)
  - Dataset management, route testing, and debugging for smooth data flow.


---

## Future Enhancements

1. **Dataset Expansion:**
   - Add more diseases, symptoms, and recommendations.
2. **Advanced Models:**
   - Integrate neural networks for improved prediction accuracy.
3. **User Accounts:**
   - Enable user profiles for tracking health history.
4. **Real-Time Updates:**
   - Integrate APIs for real-time health alerts and news.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
We extend our gratitude to our mentors and colleagues who supported this project. Special thanks to open-source contributors and libraries that made this project possible.

---

Feel free to explore, contribute, and share your feedback! Let’s make healthcare more accessible together.
