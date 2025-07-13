# cv_assistant/views.py

from django.shortcuts import render
from llm_agent.crew_setup import run_crew
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template.loader import get_template
from weasyprint import HTML

def download_pdf(request):
    cv_text = request.GET.get('cv', '')
    html_string = render_to_string('cv_assistant/pdf_template.html', {'cv_text': cv_text})

    pdf_file = HTML(string=html_string).write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="cv.pdf"'
    return response

def improve_cv_view(request):
    return render(request, 'cv_assistant/improve_form.html')

def process_cv(request):
    if request.method == 'POST':
        user_input = request.POST.get('cv', '')
        language = request.POST.get('language', 'en') 

        if not user_input:
            return render(request, 'cv_assistant/improve_form.html', {
                'error': 'Lütfen CV metninizi giriniz.'
            })

        improved_cv = run_crew(user_input, language=language)

        return render(request, 'cv_assistant/improve_result.html', {
            'improved_cv': improved_cv
        })

    return render(request, 'cv_assistant/improve_form.html')
