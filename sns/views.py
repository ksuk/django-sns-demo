from django.shortcuts import render, redirect
from .models import NewTweet
from .forms import NewTweetForm
# Create your views here.
# 
def index(request):
    tweet_list = NewTweet.objects.values_list("tweet", flat=True)
    id_list = NewTweet.objects.values_list("tweet", flat=True)
    id_list = list(id_list)
    like_list = []
    for i in id_list:
        try:
            if Like.objects.get(new_tweet_id=i):
                like = "like is done"
                like_list.append(like)
        except:
            like = "like"
            like_list.append(like)   
    tweets = zip(id_list, tweet_list, like_list)
    tweets = list(tweets)             
    return render(request, "sns/index.html", {"tweets": tweets})


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


def like(request, tweet_id):
    try:
        if Like.objects.get(new_tweet_id=tweet_id):
            Like.objects.filter(new_tweet_id=tweet_id).delete()
    except:
        like = Like(new_tweet_id=tweet_id)
        like.save()
    return redirect("/")