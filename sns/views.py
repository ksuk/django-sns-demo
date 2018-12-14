from django.shortcuts import render, redirect
from .models import NewTweet
from .forms import NewTweetForm
# Create your views here.
# 
def index(request):
    return render(request, "sns/index.html")


def new(request):
    new_tweet = NewTweetForm(request.POST or None)
    if new_tweet.is_valid():
        new_tweet = new_tweet.cleaned_data
        new_tweet = new_tweet["tweet"]
        tweet = NewTweet(tweet=new_tweet)
        tweet.save()
        return redirect("/")
    else:
        new_tweet = new_tweet.as_table()
        f = {"new_tweet":new_tweet}
        return render(request, "sns/new.html", f)    


def delete(request, tweet_id):
    NewTweet.objects.filter(id=tweet_id).delete()
    return redirect("")


def update(request, tweet_id):
    new_tweet = NewTweetForm(request.POST or None)
    if new_tweet.is_valid():
        new_tweet = new_tweet.cleaned_data["tweet"]
        old_tweet = NewTweet.objects.get(id=tweet_id)
        old_tweet.tweet = new_tweet
        old_tweet.save()
        return redirect("/")
    else:
        new_tweet = new_tweet.as_table()
        f = {"new_tweet":new_tweet}
        return render(request, "sns/index.html", f) 