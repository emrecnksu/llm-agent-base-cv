# 🧠 LLM-Agent CV Assistant

A modular Django-based AI Assistant powered by CrewAI and Ollama that analyzes and improves user CVs using multi-agent collaboration.

---

## 🔍 About the Project

This project enables users to submit a plain-text CV and uses two LLM agents to analyze and enhance it:

- **CV Analyst Agent**: Detects issues like missing work experience, weak summaries, or unclear language.
- **CV Writer Agent**: Rewrites the CV to make it professional, structured, and impactful.

The system uses **CrewAI** for multi-agent coordination and **Ollama** for local LLM inference (via models like `mistral`).

PDF generation is handled through **WeasyPrint**, and the entire project runs inside a Docker container.

---

## ⚙️ Tech Stack

- Django 5 + DRF
- CrewAI (multi-agent framework)
- Ollama (local LLM backend)
- WeasyPrint (PDF export)
- Docker & Docker Compose

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/llm-agent.git
cd llm-agent
```

### 2️⃣ Install Ollama and Pull Model

Download Ollama: https://ollama.com/download

Then pull the model (e.g., mistral):

```bash
ollama pull mistral
```

Ensure it’s running at `http://localhost:11434`.

### 3️⃣ Create .env File

Create a `.env` file in the root directory and add:

```env
OLLAMA_BASE_URL=http://host.docker.internal:11434
OLLAMA_MODEL=mistral
```

ℹ️ `host.docker.internal` allows Docker containers to access the host machine.
If you're not using Docker, use `http://localhost:11434` instead.

### 4️⃣ Run with Docker

```bash
docker-compose up --build
```

Visit the app at: [http://localhost:8000](http://localhost:8000)

Upload your CV, review the improved version, and download it as a PDF.

---

## 🗃 Project Structure

```
llm-agent/
├── cv_assistant/
│   ├── templates/
│       ├── cv_assistant
│   ├── views.py
│   └── ...
├── llm_agent/
│   ├── agents.py
│   ├── tasks.py
│   └── crew_setup.py
├── Docker/
│   ├── Dockerfile
│   └── start-container
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🌐 Multilingual Support

The application supports both **English** and **Turkish** CVs. Based on selected language, the agents generate context-appropriate output.

---

# 🇹🇷 LLM-Agent CV Asistanı

CrewAI ve Ollama destekli, Django tabanlı bir çok ajanlı yapay zekâ sistemiyle özgeçmişlerinizi analiz eder ve geliştirir.

---

## 🔍 Proje Hakkında

Bu proje, sade metin biçimindeki CV’leri analiz edip geliştirmek üzere iki farklı yapay zekâ ajanı kullanır:

- **CV Analisti**: Eksik iş deneyimi, zayıf özetler, dil bilgisi sorunları gibi problemleri analiz eder.
- **CV Yazarı**: CV’yi profesyonel ve yapılandırılmış biçimde yeniden yazar.

Ollama sayesinde **yerel** bir LLM modeliyle çalışır. Çıktılar PDF olarak sunulur. Docker üzerinden kolay kurulum sağlar.

---

## ⚙️ Kullanılan Teknolojiler

- Django 5 + Django REST Framework
- CrewAI (çok ajanlı framework)
- Ollama (yerel LLM motoru)
- WeasyPrint (PDF çıktısı)
- Docker & Docker Compose

---

## 🚀 Kurulum Adımları

### 1️⃣ Depoyu Klonla

```bash
git clone https://github.com/kullanici-adiniz/llm-agent.git
cd llm-agent
```

### 2️⃣ Ollama'yı Kur ve Modeli İndir

Ollama'yı indir: https://ollama.com/download

Ardından modeli indir:

```bash
ollama pull mistral
```

### 3️⃣ .env Dosyasını Oluştur

Kök dizine `.env` adında bir dosya oluşturun ve şu değerleri ekleyin:

```env
OLLAMA_BASE_URL=http://host.docker.internal:11434
OLLAMA_MODEL=mistral
```

ℹ️ `host.docker.internal`, Docker konteynerinden makinenize erişim sağlar.  
Docker kullanmıyorsanız `http://localhost:11434` olarak da ayarlayabilirsiniz.

### 4️⃣ Docker ile Uygulamayı Başlat

```bash
docker-compose up --build
```

Uygulamaya tarayıcıdan erişin: [http://localhost:8000](http://localhost:8000)

CV’nizi yükleyin, geliştirilen sürümünü görün ve PDF olarak indirin.
