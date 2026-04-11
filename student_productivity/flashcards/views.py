from django.shortcuts import render, redirect, get_object_or_404
from .models import Flashcard
from datetime import date, timedelta


def flashcard_list(request):
    cards = Flashcard.objects.filter(user=request.user)
    return render(request, "flashcards/list.html", {"cards": cards})


def create_flashcard(request):
    if request.method == "POST":
        question = request.POST.get("question")
        answer = request.POST.get("answer")

        Flashcard.objects.create(
            user=request.user,
            question=question,
            answer=answer
        )
        return redirect('flashcard_list')

    return render(request, "flashcards/create.html")


def delete_flashcard(request, id):
    card = get_object_or_404(Flashcard, id=id, user=request.user)
    card.delete()
    return redirect('flashcard_list')


def review_flashcards(request, index=0):
    cards = list(Flashcard.objects.filter(user=request.user))

    if not cards:
        return render(request, "flashcards/review.html", {"card": None})

    # 🔥 LOOP FOREVER
    index = index % len(cards)

    card = cards[index]

    context = {
        "card": card,
        "next_index": index + 1
    }

    return render(request, "flashcards/review.html", context)


def update_flashcard(request, id, difficulty):
    card = get_object_or_404(Flashcard, id=id, user=request.user)

    if difficulty == "easy":
        card.interval = int(card.interval * 2)
    elif difficulty == "medium":
        card.interval = int(card.interval * 1.5)
    else:
        card.interval = 1

    card.next_review = date.today() + timedelta(days=card.interval)
    card.save()

    return redirect(f'/flashcards/review/{0}/')