from django.shortcuts import render, redirect
from notesapp.models import Notes
from django.views.generic import View
from notesapp.forms import NotesForm
from django.db.models import Q

# Create your views here.

# class NotesCreateView(View):
#     def get(self,request,*args,**kwargs):
#         form=NotesForm()
#         return render(request,"index.html",{"form":form})
    
#     def post(self,request,*args,**kwargs):
#         form=NotesForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("notes-list")
#         return render(request,"index.html",{"form":form})
    
# class NotesListView(View):
#     def get(self,request,*args,**kwargs):
#         data=Notes.objects.all()
#         return render(request,"index.html",{"data":data})
    

class NotesListView(View):
    def get(self, request, *args, **kwargs):
        form = NotesForm()  # Initialize an empty form for adding new notes
        
        query = request.GET.get('q', '')  # Get the search query from the request

        if query:
            data = Notes.objects.filter(Q(title__icontains=query)).order_by('-created_at')
        
        else :
             data = Notes.objects.all().order_by('-created_at')  # Get all notes

        return render(request, "index.html", {"form": form, "data": data})  # Pass both form and notes to the template
    

    def post(self, request, *args, **kwargs):
        form = NotesForm(request.POST)  # Handle the submitted form
        if form.is_valid():
            form.save()  # Save the new note if the form is valid
            return redirect("notes-list")  # Redirect to the list of notes
        data = Notes.objects.all()  # If form is invalid, get all notes to re-render the page
        return render(request, "index.html", {"form": form, "data": data})  # Pass the form with errors and the notes list
    
    
class NotesDeleteView(View):
    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        Notes.objects.get(id=id).delete()
        return redirect('notes-list')

class NotesAllDeleteView(View):
    def get(self, request, *args, **kwargs):
        data=Notes.objects.all()
        data.delete()
        return redirect('notes-list')





       
    
        
        

