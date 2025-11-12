from django.shortcuts import render, redirect
from .forms import ResumeUploadForm
from .models import Resume
from .utils import parse_resume
import os

def upload_resume(request):
    if request.method == 'POST':
        form = ResumeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save()
            file_path = resume.uploaded_file.path
            parsed_data = parse_resume(file_path)

            resume.name = parsed_data['name']
            resume.email = parsed_data['email']
            resume.phone = parsed_data['phone']
            resume.skills = parsed_data['skills']
            resume.save()

            return redirect('resume_detail', resume.id)
    else:
        form = ResumeUploadForm()
    return render(request, 'parser_app/upload.html', {'form': form})


def resume_detail(request, pk):
    resume = Resume.objects.get(pk=pk)
    return render(request, 'parser_app/detail.html', {'resume': resume})
