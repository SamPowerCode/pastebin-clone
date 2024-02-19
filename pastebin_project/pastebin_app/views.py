from django.shortcuts import render, redirect, get_object_or_404
from .forms import PasteForm, Paste
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

def create_paste(request):
    if request.method == 'POST':
        form = PasteForm(request.POST)
        if form.is_valid():
            paste = form.save()
            return redirect('paste_detail', pk=paste.pk)  # Redirect to paste detail page
    else:
        form = PasteForm()
    return render(request, 'create_paste.html', {'form': form})

def paste_list(request):
    pastes = Paste.objects.all()
    return render(request, 'paste_list.html', {'pastes': pastes})

def paste_detail(request, pk):
    paste = get_object_or_404(Paste, pk=pk)
    lexer = get_lexer_by_name(paste.language.name.lower(), stripall=True)
    formatter = HtmlFormatter()
    highlighted_code = highlight(paste.content, lexer, formatter)
    return render(request, 'paste_detail.html', {'paste': paste, 'highlighted_code': highlighted_code})
