from django.shortcuts import render

# Create your views here.
def index(request):
    person = {'name': 'Roger', 'profession': 'Teacher'}
    hobbies = ['football', 'tennis', 'reading', 'knitting', 'polo', 'golf', 'flirting']
    langs = ['Python', 'Java', 'PHP', 'JavaScript', 'Rust', 'Ruby']
    dct = {'digits': ['One', 'Two', 'Three'],'tens': ['Ten', 'Twenty', 'Thirty']}
    movies = ['Matrix']
    music_bands = ['Oasis']
    return render(request, 'dtl/dtl.html', {
        'person': person, 
        'hobbies': hobbies, 
        'langs': langs, 
        'dct': dct, 
        'movies': movies,
        'music_bands': music_bands
    })

def filters(request):
    context = {
        "name": "JoHn DoE",
        "items": ["apple", "banana", "cherry"],
        "my_list": ["first_item", "second_item", "third_item"],
        "words": ["Django", "Templates", "Filters", "are", "powerful"],
        "string": "Django Templates Filters are powerful",
        "numbers": [1, 2, 3, 4, 5, 6]
    }
    return render(request, 'dtl/filters.html', context)

def home(request):
    return render(request, 'dtl/home.html')

def about(request):
    return render(request, 'dtl/about.html')