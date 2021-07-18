from django.shortcuts import render


def home(request):
    temp = "20°"
    hot = float(temp[:-1]) > 37.5
    print(hot)
    return render(request, 'index.html',
                  {
                    "temp": temp,
                    "hot": hot,
                    "class": "hot" if hot else "cold"
                  })
