# 🧠 LLM-Agent CV Assistant

A modular Django-based AI assistant powered by CrewAI and Ollama that analyzes and improves user CVs using multi-agent collaboration.

---

## 🔍 About the Project

This project allows users to upload a plain-text CV and enhances it through two intelligent agents:

- **CV Analyst Agent**: Identifies weaknesses such as missing job experience, vague summaries, or poor structure.
- **CV Writer Agent**: Rewrites the CV in a more professional, impactful, and structured format.

The system uses **CrewAI** for coordinating the agents and **Ollama** for local LLM inference using models like `mistral`.

PDF generation is handled by **WeasyPrint**, and the entire project runs inside a Docker container.

---

## ⚙️ Tech Stack

- Django 5 + Django REST Framework
- CrewAI (multi-agent framework)
- Ollama (local LLM runtime & model provider)
- WeasyPrint (PDF export)
- Docker & Docker Compose

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/llm-agent.git
cd llm-agent
```

### 2️⃣ Install Ollama and Pull a Model
Download Ollama: https://ollama.com/download

Then pull the model you'd like to use (e.g., mistral):

```bash
ollama pull mistral
```

Ensure the Ollama server is running at `http://localhost:11434`.

---

### 3️⃣ Create a `.env` File
Create a `.env` file in the project root with the following content:

```env
OLLAMA_BASE_URL=http://host.docker.internal:11434
OLLAMA_MODEL=mistral
```

ℹ️ `host.docker.internal` allows the Docker container to communicate with the host machine's Ollama server.  
If you're not using Docker, replace it with:

```env
OLLAMA_BASE_URL=http://localhost:11434
```

---

### 4️⃣ Run with Docker
```bash
docker-compose up --build
```

Visit the app at: [http://localhost:8000](http://localhost:8000)

Upload your CV in plain text, let the agents enhance it, and download a polished PDF version.

---

## 🗂 Project Structure

```
llm-agent/
├── cv_assistant/
│   ├── templates/
│   │   └── cv_assistant/
│   └── views.py
├── llm_agent/
│   ├── agents.py
│   ├── crew_setup.py
│   └── tasks.py
├── Docker/
│   ├── Dockerfile
│   └── start-container
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🌐 Multilingual Support

The application supports both English and Turkish CVs. Based on the selected language, agents generate context-appropriate output.

---

# 🇹🇷 LLM-Agent CV Asistanı

CrewAI ve Ollama destekli, Django tabanlı modüler bir yapay zekâ sistemiyle özgeçmişlerinizi analiz eder ve geliştirir.

---

## 🔍 Proje Hakkında

Bu proje, kullanıcıların sade metin formatında bir CV yüklemesini sağlar ve aşağıdaki iki akıllı ajan aracılığıyla geliştirir:

- **CV Analisti**: Eksik iş deneyimi, zayıf özetler, yetersiz yapı gibi sorunları tespit eder.
- **CV Yazarı**: CV’yi daha profesyonel, etkili ve yapılandırılmış bir biçimde yeniden yazar.

Ajan koordinasyonu için **CrewAI**, yerel LLM çıkarımı için ise **Ollama** (örneğin: `mistral` modeli) kullanılır.

PDF çıktısı **WeasyPrint** ile oluşturulur. Tüm sistem Docker konteyneri içinde çalışır.

---

## ⚙️ Kullanılan Teknolojiler

- Django 5 + Django REST Framework
- CrewAI (çok ajanlı framework)
- Ollama (yerel LLM çalıştırıcı ve model sağlayıcı)
- WeasyPrint (PDF çıktısı)
- Docker & Docker Compose

---

## 🚀 Kurulum Adımları

### 1️⃣ Depoyu Klonlayın
```bash
git clone https://github.com/kullanici-adiniz/llm-agent.git
cd llm-agent
```

### 2️⃣ Ollama'yı Kurun ve Modeli İndirin
Ollama'yı indirin: https://ollama.com/download

Ardından bir model indirin (örneğin: mistral):

```bash
ollama pull mistral
```

Ollama sunucusunun `http://localhost:11434` adresinde çalıştığından emin olun.

---

### 3️⃣ `.env` Dosyası Oluşturun
Proje kök dizinine aşağıdaki içeriğe sahip `.env` adlı bir dosya oluşturun:

```env
OLLAMA_BASE_URL=http://host.docker.internal:11434
OLLAMA_MODEL=mistral
```

ℹ️ `host.docker.internal`, Docker konteynerinin bilgisayarınızdaki Ollama sunucusuna erişmesini sağlar.  
Docker kullanmıyorsanız şu şekilde ayarlayabilirsiniz:

```env
OLLAMA_BASE_URL=http://localhost:11434
```

---

### 4️⃣ Docker ile Uygulamayı Başlatın
```bash
docker-compose up --build
```

Tarayıcınızdan uygulamaya erişin: [http://localhost:8000](http://localhost:8000)

CV’nizi yükleyin, geliştirilen versiyonunu görün ve PDF olarak indirin.

---

## 🗂 Proje Yapısı

```
llm-agent/
├── cv_assistant/
│   ├── templates/
│   │   └── cv_assistant/
│   └── views.py
├── llm_agent/
│   ├── agents.py
│   ├── crew_setup.py
│   └── tasks.py
├── Docker/
│   ├── Dockerfile
│   └── start-container
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🌐 Çok Dilli Destek

Uygulama hem İngilizce hem de Türkçe CV’leri destekler. Seçilen dile göre, ajanlar bağlama uygun çıktılar üretir.
