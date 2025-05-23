# أثر - منصة قياس الأثر التطوعي
# Athar - Volunteer Impact Measurement Platform

## Overview | نظرة عامة

أثر (Athar) is a Django-based web application designed for Arabic-speaking users to create and evaluate volunteer project impact. The platform features a beautiful, modern, and nature-inspired interface, operating without login requirements or databases — using only session data.

## Features | المميزات

- 11-step project assessment forms
- Idea submission system
- Project funding tracking
- PDF export functionality
- Full Arabic interface
- Session-based data storage
- No login required

## Installation | التثبيت

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run migrations:
```bash
python manage.py migrate
```
5. Start the development server:
```bash
python manage.py runserver
```

## Project Structure | هيكل المشروع

- `/core/` - Main application directory
  - `/templates/` - HTML templates
  - `/static/` - CSS, JS, and images
  - `forms.py` - Form definitions
  - `views.py` - View logic
  - `urls.py` - URL routing

## Forms | النماذج

1. Project Info
2. Strategic Alignment
3. Performance Indicators
4. Stakeholder Recommendations
5. Stakeholder Engagement ROI
6. Sustainability Evaluation
7. Resources & Outputs
8. Results Evaluation
9. Impact ROI Calculation
10. Final Recommendations
11. PDF Preview & Export

## License | الترخيص

MIT License #   M y   P r o j e c t  
 