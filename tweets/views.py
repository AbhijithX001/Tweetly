from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Tweet, Comment, Profile


def tweet_list(request):
    tweets = Tweet.objects.all().order_by("-created_at")
    return render(request, "tweets/tweet_list.html", {"tweets": tweets})


@login_required
def tweet_create(request):
    if request.method == "POST":
        text = request.POST.get("text")
        photo = request.FILES.get("photo")

        if photo:
            allowed_types = ["image/jpeg", "image/png"]
            if photo.content_type not in allowed_types:
                messages.error(request, "Only JPG or PNG images are allowed.")
                return redirect("tweet_create")

        Tweet.objects.create(user=request.user, text=text, photo=photo)
        return redirect("tweet_list")

    return render(request, "tweets/tweet_form.html")


@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, user=request.user)

    if request.method == "POST":
        tweet.text = request.POST.get("text")
        new_photo = request.FILES.get("photo")

        if new_photo:
            allowed_types = ["image/jpeg", "image/png"]
            if new_photo.content_type not in allowed_types:
                messages.error(request, "Only JPG or PNG images are allowed.")
                return redirect("tweet_edit", tweet_id=tweet_id)

            tweet.photo = new_photo

        tweet.save()
        return redirect("tweet_list")

    return render(request, "tweets/tweet_form.html", {"tweet": tweet})


@login_required
def tweet_confirm_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, user=request.user)

    if request.method == "POST":
        tweet.delete()
        return redirect("tweet_list")

    return render(request, "tweets/tweet_confirm_delete.html", {"tweet": tweet})


@login_required
def tweet_like_toggle(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)

    if request.user in tweet.likes.all():
        tweet.likes.remove(request.user)
    else:
        tweet.likes.add(request.user)

    return redirect("tweet_list")


@login_required
def comments_view(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)
    comments = Comment.objects.filter(tweet=tweet, parent=None).order_by("-created_at")

    return render(request, "tweets/comments.html", {
        "tweet": tweet,
        "comments": comments
    })


@login_required
def comment_add(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)

    if request.method == "POST":
        text = request.POST.get("text")
        parent_id = request.GET.get("parent")

        if parent_id:
            parent = Comment.objects.get(id=parent_id)
            Comment.objects.create(user=request.user, tweet=tweet, text=text, parent=parent)
        else:
            Comment.objects.create(user=request.user, tweet=tweet, text=text)

    return redirect("comments_view", tweet_id=tweet_id)


@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    tweet_id = comment.tweet.id
    comment.delete()
    return redirect("comments_view", tweet_id=tweet_id)


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("tweet_list")

    return render(request, "registration/register.html")


@login_required
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    tweets = Tweet.objects.filter(user=user).order_by("-created_at")

    return render(request, "profile/profile.html", {
        "profile_user": user,
        "tweets": tweets
    })


@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == "POST":
        profile.bio = request.POST.get("bio")
        new_image = request.FILES.get("image")

        if new_image:
            allowed_types = ["image/jpeg", "image/png"]
            if new_image.content_type not in allowed_types:
                messages.error(request, "Only JPG or PNG profile images are allowed.")
                return redirect("edit_profile")

            profile.image = new_image

        profile.save()
        return redirect("user_profile", username=request.user.username)

    return render(request, "profile/edit_profile.html", {"profile": profile})
