from django import forms

class IdeaForm(forms.Form):
    title = forms.CharField(
        label="عنوان الفكرة",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل عنوان الفكرة'})
    )
    
    description = forms.CharField(
        label="وصف الفكرة",
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'اشرح فكرتك بالتفصيل'})
    )
    
    target_group = forms.ChoiceField(
        label="الفئة المستهدفة",
        choices=[
            ("طلاب", "طلاب"),
            ("أسر", "أسر"),
            ("ذوي إعاقة", "ذوي إعاقة"),
            ("شباب", "شباب"),
            ("نساء", "نساء"),
            ("أطفال", "أطفال"),
            ("كبار السن", "كبار السن"),
            ("عام", "عام")
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    location = forms.CharField(
        label="الموقع الجغرافي المقترح",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل الموقع الجغرافي'})
    )
    
    impact_type = forms.ChoiceField(
        label="نوع الأثر المتوقع",
        choices=[
            ("اجتماعي", "اجتماعي"),
            ("صحي", "صحي"),
            ("بيئي", "بيئي"),
            ("ثقافي", "ثقافي"),
            ("تعليمي", "تعليمي"),
            ("اقتصادي", "اقتصادي")
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    duration = forms.CharField(
        label="المدة الزمنية المقترحة",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'مثال: 6 أشهر'})
    )
    
    resources = forms.CharField(
        label="الموارد المطلوبة (إن وُجد)",
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'اذكر الموارد المطلوبة إن وجدت'})
    )
    
    previously_implemented = forms.ChoiceField(
        label="هل سبق تنفيذ الفكرة؟",
        choices=[
            ("نعم", "نعم"),
            ("لا", "لا")
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    author = forms.CharField(
        label="اسم صاحب الفكرة (اختياري)",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اختياري'})
    )
    
    contact = forms.CharField(
        label="وسيلة التواصل (اختياري)",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'بريد إلكتروني أو رقم جوال'})
    )
    
    goal = forms.IntegerField(
        label="الميزانية المطلوبة (ريال)",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أدخل المبلغ المطلوب'})
    )
    
    funded = forms.IntegerField(
        label="المبلغ المدفوع (ريال)",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أدخل المبلغ المدفوع'})
    )
    
    attachment = forms.FileField(
        label="مرفق (اختياري)",
        required=False,
        widget=forms.FileInput(attrs={'class': 'form-control'})
    ) 