from django.shortcuts import render, HttpResponse, redirect
from .models import *
# Create your views here.
def reviews_list(request):
    reviews = Review.objects.all()
    context = {
        "reviews" : reviews
    }
    return render(request, 'reviews_list.html', context)

def reviews_read(request, pk):
    review = Review.objects.get(id = pk)

    context = {
        "review" : review,
    }
    return render(request, "reviews_read.html", context)

def reviews_create(request):
    if request.method == "POST":
        Review.objects.create(
            title = request.POST["title"],
            director = request.POST["director"],
            mainActor = request.POST["mainActor"],
            genre = request.POST["genre"],
            horoscope = int(request.POST["horoscope"]),
            runningTime = int(request.POST["runningTime"]),
            reviewContent = request.POST["reviewContent"],
        )
        return redirect("/reviews")
    return render(request, "reviews_create.html")

def reviews_update(request, pk):
    review = Review.objects.get(id=pk)
    if request.method == "POST":
        review.title = request.POST["title"]
        review.director = request.POST["director"]
        review.mainActor = request.POST["mainActor"]
        review.genre = request.POST["genre"]
        review.horoscope = int(request.POST["horoscope"])
        review.runningTime = int(request.POST["runningTime"])
        review.reviewContent = request.POST["reviewContent"]
        review.save()
        return redirect(f"/reviews/{pk}")
    context = {
        "review": review
    }
    return render(request, "reviews_update.html", context)

def reviews_delete(request, pk):
    if request.method == "POST":
        review = Review.objects.get(id=pk)
        review.delete()
    return redirect("/reviews")