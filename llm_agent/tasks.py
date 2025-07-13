#llm_agent/llm_agent/tasks.py

from crewai import Task

def create_analyze_cv_task(agent, cv_text: str, language: str = "en"):
    prompt = {
        "en": (
            f"The following resume has been submitted by a user:\n\n"
            f"---\n{cv_text}\n---\n\n"
            "You are a professional career advisor. Analyze the resume with the following objectives:\n"
            "1. Identify missing or weak sections (e.g., incomplete work experience, vague summaries, missing education years)\n"
            "2. Point out any formatting or structural issues\n"
            "3. Detect language, grammar, or clarity problems\n"
            "4. Highlight strong elements (e.g., clear achievements, quantified outcomes)\n"
            "5. Suggest improvements in content, clarity, or organization.\n\n"
            "Respond under the following structured headings:\n"
            "**Strengths**\n- ...\n\n"
            "**Weaknesses**\n- ...\n\n"
            "**Recommendations**\n- ...\n\n"
            "Make sure the output is actionable and concise.\n"
            "**ONLY RESPOND IN ENGLISH. DO NOT USE OTHER LANGUAGES.**"
        ),
        "tr": (
            f"Aşağıda bir kullanıcı tarafından gönderilen özgeçmiş yer alıyor:\n\n"
            f"---\n{cv_text}\n---\n\n"
            "Sen profesyonel bir kariyer danışmanısın. Bu özgeçmişi aşağıdaki amaçlara göre analiz et:\n"
            "1. Eksik veya zayıf bölümleri belirle (örneğin: tamamlanmamış iş deneyimi, belirsiz özet, eksik eğitim yılları)\n"
            "2. Yapısal veya biçimsel sorunları tespit et\n"
            "3. Dil bilgisi, anlatım ya da yazım hatalarını belirt\n"
            "4. Güçlü yönleri vurgula (örneğin: net başarılar, sayısal çıktılar)\n"
            "5. İçerik, açıklık veya organizasyon konusunda öneriler sun\n\n"
            "Yanıtını aşağıdaki yapı ile oluştur:\n"
            "**Güçlü Yönler**\n- ...\n\n"
            "**Zayıf Yönler**\n- ...\n\n"
            "**Öneriler**\n- ...\n\n"
            "Yalın, doğrudan ve uygulanabilir öneriler sun.\n"
            "**SADECE Türkçe olarak yanıtla. İngilizce YANIT VERME.**"
        )
    }

    return Task(
        description=prompt[language],
        expected_output="Structured analysis with Strengths / Weaknesses / Recommendations",
        agent=agent,
        input={"cv": cv_text}
    )

def create_improve_cv_task(agent, cv_text: str, analyze_task, language: str = "en"):
    prompt = {
        "tr": (
            f"Aşağıda kullanıcı tarafından gönderilen orijinal özgeçmiş yer almaktadır:\n\n"
            f"---\n{cv_text}\n---\n\n"
            "CV analizine dayanarak bu özgeçmişi daha profesyonel, etkili ve dikkat çekici hale getirmelisin. "
            "Aşağıdaki yapıya uyarak açık ve düzenli bir biçimde yaz:\n\n"
            "- İletişim Bilgileri\n"
            "- Profesyonel Özet\n"
            "- İş Deneyimi\n"
            "- Teknik Yetenekler (diller, araçlar, veri tabanları ayrı ayrı gruplansın)\n"
            "- Eğitim\n"
            "- (Varsa) Sertifikalar / Projeler\n"
            "- (Opsiyonel) Kariyer Hedefi\n\n"
            "Boş kısımlar varsa dahil etme.\n"
            "**Yalnızca özgeçmiş metnini döndür. Açıklama yapma. SADECE Türkçe yaz. İngilizce yazma.**"
        ),
        "en": (
            f"Below is the original resume provided by the user:\n\n"
            f"---\n{cv_text}\n---\n\n"
            "Based on the analysis, rewrite the resume in a professional and clean format. Use the structure:\n\n"
            "- Contact Information\n"
            "- Professional Summary\n"
            "- Work Experience\n"
            "- Technical Skills (group into Languages, Tools, Databases, Concepts)\n"
            "- Education\n"
            "- (If available) Certifications / Projects\n"
            "- (Optional) Career Objective\n\n"
            "Do not include empty sections.\n"
            "**Only return the improved CV content. No explanation. ONLY RESPOND IN ENGLISH.**"
        )
    }

    return Task(
        description=prompt[language],
        expected_output="Professional, well-structured CV with grouped technical sections and removed empty fields.",
        agent=agent,
        input={"cv": cv_text},
        context=[analyze_task]
    )
