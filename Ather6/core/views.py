from django.shortcuts import render, redirect
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from .forms import IdeaForm
from datetime import datetime

# Arabic month names mapping
MONTHS_AR = {
    "01": "يناير", "02": "فبراير", "03": "مارس", "04": "أبريل",
    "05": "مايو", "06": "يونيو", "07": "يوليو", "08": "أغسطس",
    "09": "سبتمبر", "10": "أكتوبر", "11": "نوفمبر", "12": "ديسمبر"
}

def render_to_pdf(template_src, context_dict={}):
    try:
        template = get_template(template_src)
        html = template.render(context_dict)
        
        # Create the PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="project_report.pdf"'
        
        # Define base CSS that's compatible with xhtml2pdf
        base_css = '''
            @page {
                size: A4;
                margin: 2cm;
            }
            
            body {
                font-family: Arial, sans-serif;
                direction: rtl;
                font-size: 14pt;
                line-height: 1.7;
                color: #222;
                margin: 0;
                padding: 0;
            }
            
            .section {
                margin-bottom: 20px;
                page-break-inside: avoid;
            }
            
            .section-title {
                color: #155724;
                border-bottom: 2px solid #155724;
                padding-bottom: 5px;
                margin-bottom: 15px;
                font-size: 18pt;
                font-weight: bold;
            }
            
            .subsection-title {
                color: #0d6efd;
                margin: 10px 0;
                font-size: 16pt;
                font-weight: bold;
            }
            
            .label {
                font-weight: bold;
                color: #155724;
                margin-left: 5px;
            }
            
            .info-item {
                margin-bottom: 10px;
            }
            
            .signature-section {
                margin-top: 30px;
                page-break-inside: avoid;
            }
            
            .signature-line {
                border-bottom: 2px dashed #888;
                width: 300px;
                height: 40px;
                margin: 10px 0;
            }
            
            .footer {
                margin-top: 30px;
                padding-top: 10px;
                border-top: 1px solid #ddd;
                font-size: 12pt;
                color: #666;
                text-align: center;
            }
            
            .row {
                display: block;
                margin-bottom: 15px;
            }
            
            .col-md-6 {
                display: inline-block;
                width: 48%;
                vertical-align: top;
            }
            
            .text-center {
                text-align: center;
            }
            
            .text-muted {
                color: #666;
            }
            
            .mb-4 {
                margin-bottom: 15px;
            }
            
            .mt-4 {
                margin-top: 15px;
            }
            
            .mt-2 {
                margin-top: 8px;
            }
            
            .py-5 {
                padding-top: 20px;
                padding-bottom: 20px;
            }
            
            .container {
                width: 100%;
                max-width: 100%;
                padding: 0;
                margin: 0;
            }
            
            @media print {
                .no-print {
                    display: none;
                }
            }
        '''
        
        # Create the PDF with custom options
        pisa_status = pisa.CreatePDF(
            html,
            dest=response,
            encoding='utf-8',
            show_error_as_pdf=True,
            link_callback=None,
            default_css=base_css
        )
        
        if pisa_status.err:
            # Log the error for debugging
            print(f"PDF Generation Error: {pisa_status.err}")
            return HttpResponse('حدث خطأ أثناء إنشاء ملف PDF. يرجى المحاولة مرة أخرى.')
            
        return response
        
    except Exception as e:
        # Log the exception for debugging
        print(f"Exception in PDF Generation: {str(e)}")
        return HttpResponse('حدث خطأ غير متوقع. يرجى المحاولة مرة أخرى.')

def home(request):
    return render(request, 'core/home.html')

def form1(request):
    if request.method == "POST":
        request.session['form1'] = request.POST
        return redirect('form2')
    return render(request, 'core/form1.html')

def form2(request):
    if request.method == "POST":
        request.session['form2'] = request.POST
        return redirect('form3')
    return render(request, 'core/form2.html')

def form3(request):
    if request.method == "POST":
        request.session['form3'] = request.POST
        return redirect('form4')
    return render(request, 'core/form3.html')

def form4(request):
    if request.method == "POST":
        request.session['form4'] = request.POST
        return redirect('form5')
    return render(request, 'core/form4.html')

def form5(request):
    if request.method == "POST":
        request.session['form5'] = request.POST
        return redirect('form6')
    return render(request, 'core/form5.html')

def form6(request):
    if request.method == "POST":
        request.session['form6'] = request.POST
        return redirect('form7')
    return render(request, 'core/form6.html')

def form7(request):
    if request.method == "POST":
        request.session['form7'] = request.POST
        return redirect('form8')
    return render(request, 'core/form7.html')

def form8(request):
    if request.method == "POST":
        request.session['form8'] = request.POST
        return redirect('form9')
    return render(request, 'core/form8.html')

def form9(request):
    if request.method == "POST":
        request.session['form9'] = request.POST
        return redirect('form10')
    return render(request, 'core/form9.html')

def form10(request):
    if request.method == "POST":
        request.session['form10'] = request.POST
        return redirect('form11')
    return render(request, 'core/form10.html')

def form11(request):
    if request.method == "POST":
        request.session['form11'] = request.POST
        return redirect('export_pdf')
    return render(request, 'core/form11.html')

def classify_idea(idea_data):
    """Auto-classify the idea based on description and impact type"""
    text = idea_data.get('description', '').lower()
    impact_type = idea_data.get('impact_type', '').lower()
    
    # Check impact type first
    if impact_type == "صحي":
        return "مشروع صحي"
    elif impact_type == "تعليمي":
        return "مشروع تعليمي"
    elif impact_type == "بيئي":
        return "مشروع بيئي"
    elif impact_type == "اجتماعي":
        return "مشروع اجتماعي"
    elif impact_type == "ثقافي":
        return "مشروع ثقافي"
    elif impact_type == "اقتصادي":
        return "مشروع اقتصادي"
    
    # If no clear impact type, check description
    if "صحة" in text or "طبي" in text or "علاج" in text:
        return "مشروع صحي"
    elif "تعليم" in text or "مدرسة" in text or "جامعة" in text:
        return "مشروع تعليمي"
    elif "بيئة" in text or "نظافة" in text or "تلوث" in text:
        return "مشروع بيئي"
    elif "مجتمع" in text or "أسرة" in text or "شباب" in text:
        return "مشروع اجتماعي"
    elif "ثقافة" in text or "فن" in text or "تراث" in text:
        return "مشروع ثقافي"
    elif "اقتصاد" in text or "تجارة" in text or "استثمار" in text:
        return "مشروع اقتصادي"
    
    return "مشروع عام"

def ideas(request):
    if request.method == "POST":
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            if 'ideas' not in request.session:
                request.session['ideas'] = []
            
            idea_data = form.cleaned_data
            
            # Handle file upload
            if 'attachment' in request.FILES:
                uploaded_file = request.FILES['attachment']
                idea_data['file_name'] = uploaded_file.name
                idea_data['file_size'] = uploaded_file.size
                idea_data['file_type'] = uploaded_file.content_type
            
            # Add auto-classification
            idea_data['category'] = classify_idea(idea_data)
            
            # Handle editing
            edit_index = request.session.get('edit_index')
            if edit_index is not None and edit_index < len(request.session['ideas']):
                request.session['ideas'][edit_index] = idea_data
                request.session['ideas'][edit_index]['modified'] = True
                request.session['can_edit'] = False
                request.session['edit_index'] = None
            else:
                idea_data['modified'] = False
                request.session['ideas'].append(idea_data)
            
            request.session.modified = True
            return redirect('ideas')
    else:
        form = IdeaForm()
    
    # Get existing ideas for display
    ideas = request.session.get('ideas', [])
    can_edit = request.session.get('can_edit', True)
    
    return render(request, 'core/ideas.html', {
        'form': form,
        'ideas': ideas,
        'can_edit': can_edit
    })

def edit_idea(request, index):
    if request.method == "POST":
        if 'ideas' in request.session and 0 <= index < len(request.session['ideas']):
            request.session['edit_index'] = index
            request.session['can_edit'] = True
            request.session.modified = True
    return redirect('ideas')

def funders(request):
    ideas = request.session.get('ideas', [])
    
    # Sort ideas by modification status
    ideas = sorted(ideas, key=lambda x: x.get('modified', False), reverse=True)
    
    # Calculate funding percentages and remaining amounts
    for idea in ideas:
        goal = float(idea.get('goal', 0))
        funded = float(idea.get('funded', 0))
        idea['remaining'] = goal - funded
        idea['percent'] = int((funded / goal) * 100) if goal > 0 else 0
        idea['percent_remaining'] = 100 - idea['percent']
        
        # Set color and icon based on funding percentage
        if idea['percent'] >= 70:
            idea['color'] = '#28a745'  # Green
            idea['icon'] = '✅'
            idea['status'] = 'مكتمل أو شبه مكتمل'
        elif idea['percent'] >= 30:
            idea['color'] = '#fd7e14'  # Orange
            idea['icon'] = '⚠️'
            idea['status'] = 'قيد التنفيذ'
        else:
            idea['color'] = '#dc3545'  # Red
            idea['icon'] = '❌'
            idea['status'] = 'بحاجة عاجلة للدعم'
    
    return render(request, 'core/funders.html', {'ideas': ideas})

def export_pdf(request):
    # Helper function to safely get values with default empty string
    def safe_get(data, key, default=''):
        return str(data.get(key, default) or default)

    # Get all form data from session with default empty dictionaries
    form1_data = request.session.get('form1', {})
    form2_data = request.session.get('form2', {})
    form3_data = request.session.get('form3', {})
    form4_data = request.session.get('form4', {})
    form5_data = request.session.get('form5', {})
    form6_data = request.session.get('form6', {})
    form7_data = request.session.get('form7', {})
    form8_data = request.session.get('form8', {})
    form9_data = request.session.get('form9', {})
    form10_data = request.session.get('form10', {})
    form11_data = request.session.get('form11', {})

    # Get current date in Arabic format
    now = datetime.now()
    today = f"{now.day} {MONTHS_AR[now.strftime('%m')]} {now.year}"

    # Organize data for the template
    context = {
        # Current date
        'today': today,
        
        # Basic Project Information (Form 1)
        'project_name': safe_get(form1_data, 'project_name'),
        'implementing_agency': safe_get(form1_data, 'implementing_agency'),
        'project_duration': safe_get(form1_data, 'project_duration'),
        'project_location': safe_get(form1_data, 'project_location'),
        'project_type': safe_get(form1_data, 'project_type'),

        # Project Goals and Objectives (Form 2)
        'project_objectives': safe_get(form2_data, 'project_goals'),
        'target_audience': safe_get(form2_data, 'target_audience'),
        'expected_impact': safe_get(form2_data, 'expected_impact'),

        # Activities and Outputs (Form 3)
        'main_activities': safe_get(form3_data, 'activities'),
        'project_outputs': safe_get(form3_data, 'outputs'),
        'performance_indicators': safe_get(form3_data, 'indicators'),
        'implementation_steps': safe_get(form3_data, 'implementation_steps'),

        # Project Outcomes (Form 4)
        'project_outcomes': safe_get(form4_data, 'outcomes'),
        'success_criteria': safe_get(form4_data, 'success_criteria'),
        'impact_measurement': safe_get(form4_data, 'impact_measurement'),

        # Stakeholders (Form 5)
        'stakeholders': {
            'internal': safe_get(form5_data, 'internal_stakeholders'),
            'external': safe_get(form5_data, 'external_stakeholders'),
            'roles': safe_get(form5_data, 'stakeholder_roles'),
            'engagement': safe_get(form5_data, 'stakeholder_engagement')
        },

        # ROI and Impact (Form 6)
        'roi': {
            'financial': safe_get(form6_data, 'financial_roi'),
            'social': safe_get(form6_data, 'social_impact'),
            'environmental': safe_get(form6_data, 'environmental_impact'),
            'sustainability': safe_get(form6_data, 'sustainability_impact')
        },

        # Budget and Resources (Form 7)
        'budget': {
            'total': safe_get(form7_data, 'total_budget'),
            'breakdown': safe_get(form7_data, 'budget_breakdown'),
            'resources': safe_get(form7_data, 'required_resources'),
            'funding_sources': safe_get(form7_data, 'funding_sources')
        },

        # Timeline and Schedule (Form 8)
        'timeline': {
            'start_date': safe_get(form8_data, 'start_date'),
            'end_date': safe_get(form8_data, 'end_date'),
            'milestones': safe_get(form8_data, 'project_milestones'),
            'schedule': safe_get(form8_data, 'detailed_schedule')
        },

        # Monitoring and Evaluation (Form 9)
        'monitoring_and_evaluation': {
            'criteria': safe_get(form9_data, 'monitoring_criteria'),
            'methods': safe_get(form9_data, 'monitoring_methods'),
            'frequency': safe_get(form9_data, 'monitoring_frequency'),
            'reporting': safe_get(form9_data, 'reporting_mechanisms')
        },

        # Final Report (Form 10)
        'final_report': {
            'recommendations': safe_get(form10_data, 'final_recommendations'),
            'challenges': safe_get(form10_data, 'challenges_faced'),
            'solutions': safe_get(form10_data, 'solutions_implemented'),
            'future_plans': safe_get(form10_data, 'future_plans')
        },

        # Project Completion (Form 11)
        'completion': {
            'lessons_learned': safe_get(form11_data, 'lessons_learned'),
            'completion_date': safe_get(form11_data, 'completion_date'),
            'final_status': safe_get(form11_data, 'project_status'),
            'sustainability': safe_get(form11_data, 'sustainability_measures')
        }
    }

    if request.method == 'POST':
        return render_to_pdf('core/export_pdf.html', context)
    return render(request, 'core/export_pdf.html', context)
