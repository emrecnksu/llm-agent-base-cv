# llm_agent/llm_agent/agents.py

from crewai import Agent
from langchain_community.llms import Ollama
from django.conf import settings

llm = Ollama(model=settings.OLLAMA_MODEL, base_url=settings.OLLAMA_BASE_URL)

def get_agents(language="en"):
    if language == "tr":
        cv_analyst_agent = Agent(
            role="CV Analisti",
            goal="Gönderilen özgeçmişi analiz ederek eksik veya zayıf yönleri tespit etmek ve iyileştirme alanlarını belirlemek. EK olarak, tekrar eden, profesyonellikten uzak ifadeleri saptamak.",
            backstory="İnsan kaynakları alanında 10 yılı aşkın deneyime sahip bir kariyer danışmanısın. Özellikle tekrar eden cümlelerden, açıklayıcı olmayan ifadelerden ve tavsiye tarzı metinlerden kaçınmayı hedeflersin. Özgeçmişleri işverenlerin dikkatini çekecek şekilde analiz etme ve yapıcı öneriler sunma konusunda uzmansın.",
            system_message="Tüm çıktıları SADECE Türkçe olarak üret. İngilizce YANIT VERME.",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

        cv_writer_agent = Agent(
            role="CV Yazarı",
            goal="Özgeçmişi analiz sonuçlarına göre daha güçlü ve etkili hale getirmek.",
            backstory="İşe alım sürecinde dikkat çeken profesyonel CV'ler hazırlayan deneyimli bir içerik yazarı ve kariyer danışmanısın. Adayın güçlü yönlerini vurgulayan, yapılandırılmış ve akıcı özgeçmişler oluşturma konusunda uzmansın. Tekrar eden ifadeleri kaldırır, dil bilgisi kurallarına uygun, doğal ve sade bir Türkçe ile yazarsın.",
            system_message="Tüm çıktıları SADECE Türkçe olarak üret. İngilizce YANIT VERME.",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    else:
        cv_analyst_agent = Agent(
            role="CV Analyst",
            goal="Analyze the submitted resume and identify areas for improvement.",
            backstory="You are a seasoned career advisor with over 10 years of experience in reviewing CVs and helping job seekers improve their resumes for better results in the hiring process.",
            system_message="Only respond in English. Never use any other language.",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

        cv_writer_agent = Agent(
            role="CV Writer",
            goal="Rewrite and enhance resumes based on analysis results to make them more professional and impactful.",
            backstory="You're a seasoned career advisor and writer. Your task is to rewrite resumes with concise, engaging, and formal tone, removing redundant sections and maintaining a strong structure.",
            system_message="Only respond in English. Never use any other language.",
            verbose=True,
            allow_delegation=False,
            llm=llm
        )

    return cv_analyst_agent, cv_writer_agent
