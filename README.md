# Malaria Image Classification with Convolutional Neural Networks

## Project Overview

Malaria is a life-threatening disease caused by parasites transmitted through infected mosquitoes. Prompt and precise diagnosis is essential for treatment. This project develops a **Convolutional Neural Network (CNN)** to automate the detection of malaria by analyzing microscopic blood cell images. 

The end-to-end solution features data preprocessing, a custom CNN architecture, and an interactive **Streamlit web application** for real-time predictions.

## Dataset

The dataset consists of **27,558 microscopic cell images** equally divided into two classes:
- **Parasitized:** Cells containing Plasmodium parasites.
- **Uninfected:** Healthy, parasite-free cells.

## Model Architecture

A custom Sequential Deep Learning model built with TensorFlow/Keras. Features include:
- Input shape of `(30, 30, 3)` (RGB normalized images)
- 2x `Conv2D` layers with `ReLU` activation for feature extraction.
- 2x `MaxPooling2D` layers to reduce spatial dimensions.
- Flattened output connected to Dense Hidden Layers.
- Final output layer using `Softmax` for Binary Classification (Parasitized vs. Uninfected).

## Project Structure

```
├── cell_images/                              # Image directory
│   ├── Parasitized/                          # Infected cell images
│   └── Uninfected/                           # Healthy cell images
├── Image Classification with CNN for Malaria Data.ipynb  # Jupyter Notebook for EDA & Model Training
├── app.py                                    # Streamlit Web UI application
├── my_malaria_cnn_model.h5                   # Trained Keras Model
├── requirements.txt                          # Python dependencies
└── README.md                                 # Project documentation
```

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/malaria-cnn-classification.git
   cd malaria-cnn-classification
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit Web App:**
   ```bash
   streamlit run app.py
   ```
   *Upload a cell image using the web UI to instantly classify whether the cell is infected with Malaria.*

4. **Train the Model (Optional):**
   Open the Jupyter Notebook to explore the data pipeline and retrain the CNN.
   ```bash
   jupyter notebook "Image Classification with CNN for Malaria Data.ipynb"
   ```

## Key Learnings & Improvements
- **Robust Feature Extraction:** Deep learning proves highly capable of identifying complex microscopic patterns for disease diagnosis.
- **Micro-service Deployment:** Streamlit is used for seamless, interactive end-user deployment.
