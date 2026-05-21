# Malaria Detection with CNN

An end-to-end deep learning solution that automates malaria detection from microscopic blood cell images, featuring a custom CNN architecture and an interactive Streamlit web application.

---

## English

### About

Malaria is a life-threatening disease caused by parasites transmitted through infected mosquitoes. Prompt and precise diagnosis is essential for effective treatment. This project develops a **Convolutional Neural Network (CNN)** to automate the detection of malaria by classifying microscopic blood cell images as either parasitized (infected) or uninfected (healthy).

### Features

- Binary classification: Parasitized vs. Uninfected
- Custom Sequential CNN built with TensorFlow/Keras
- Interactive Streamlit web app for real-time predictions
- End-to-end pipeline: data loading → preprocessing → training → deployment

### Dataset

| Property | Detail |
|---|---|
| Total Images | 27,558 |
| Parasitized | 13,779 |
| Uninfected | 13,779 |
| Input Shape | 30 × 30 × 3 (RGB) |

Images are normalized to [0, 1] before training.

### Model Architecture

```
Input (30, 30, 3)
→ Conv2D → ReLU → MaxPooling2D
→ Conv2D → ReLU → MaxPooling2D
→ Flatten
→ Dense (Hidden Layers)
→ Dense (2, softmax)
```

Compiled with **Adam** optimizer and **Sparse Categorical Crossentropy** loss.  
Trained weights saved as `my_malaria_cnn_model.h5`.

### How to Run

**1. Clone the repository**
```bash
git clone https://github.com/MMertAvc/Malaria-Detection-CNN.git
cd Malaria-Detection-CNN
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the Streamlit app**
```bash
streamlit run app.py
```
Upload a cell image via the web interface to instantly classify it.

**4. (Optional) Retrain the model**
```bash
jupyter notebook "Image Classification with CNN for Malaria Data.ipynb"
```

### Project Structure

```
├── cell_images/
│   ├── Parasitized/
│   └── Uninfected/
├── Image Classification with CNN for Malaria Data.ipynb
├── app.py
├── my_malaria_cnn_model.h5
├── requirements.txt
└── README.md
```

### Requirements

```
tensorflow
keras
streamlit
numpy
pillow
matplotlib
scikit-learn
```

---

## Türkçe

### Hakkında

Sıtma, enfekte sivrisinekler tarafından iletilen parazitlerin yol açtığı hayatı tehdit eden bir hastalıktır. Hızlı ve hassas tanı, etkili tedavi için kritik önem taşır. Bu proje, mikroskobik kan hücresi görüntülerini parazitli (enfekte) veya enfekte olmayan (sağlıklı) olarak sınıflandırarak sıtma tespitini otomatikleştiren bir **Evrişimsel Sinir Ağı (CNN)** geliştirir.

### Özellikler

- İkili sınıflandırma: Parazitli - Enfekte Olmayan
- TensorFlow/Keras ile oluşturulmuş özel Sequential CNN
- Gerçek zamanlı tahminler için etkileşimli Streamlit web uygulaması
- Uçtan uca işlem hattı: veri yükleme → ön işleme → eğitim → dağıtım

### Veri Seti

| Özellik | Detay |
|---|---|
| Toplam Görüntü | 27.558 |
| Parazitli | 13.779 |
| Enfekte Olmayan | 13.779 |
| Giriş Boyutu | 30 × 30 × 3 (RGB) |

Görüntüler eğitim öncesinde [0, 1] aralığına normalize edilir.

### Model Mimarisi

```
Giriş (30, 30, 3)
→ Conv2D → ReLU → MaxPooling2D
→ Conv2D → ReLU → MaxPooling2D
→ Flatten
→ Dense (Gizli Katmanlar)
→ Dense (2, softmax)
```

**Adam** optimizörü ve **Seyrek Kategorik Çapraz Entropi** kaybı ile derlenir.  
Eğitilmiş ağırlıklar `my_malaria_cnn_model.h5` olarak kaydedilir.

### Nasıl Çalıştırılır

**1. Repoyu klonlayın**
```bash
git clone https://github.com/MMertAvc/Malaria-Detection-CNN.git
cd Malaria-Detection-CNN
```

**2. Bağımlılıkları yükleyin**
```bash
pip install -r requirements.txt
```

**3. Streamlit uygulamasını çalıştırın**
```bash
streamlit run app.py
```
Web arayüzü üzerinden bir hücre görüntüsü yükleyerek anında sınıflandırma yapın.

**4. (İsteğe Bağlı) Modeli yeniden eğitin**
```bash
jupyter notebook "Image Classification with CNN for Malaria Data.ipynb"
```

### Proje Yapısı

```
├── cell_images/
│   ├── Parasitized/
│   └── Uninfected/
├── Image Classification with CNN for Malaria Data.ipynb
├── app.py
├── my_malaria_cnn_model.h5
├── requirements.txt
└── README.md
```

### Gereksinimler

```
tensorflow
keras
streamlit
numpy
pillow
matplotlib
scikit-learn
```
