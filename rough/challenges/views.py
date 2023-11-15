from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


monthly_challenges = {
    "january": "January - Java 30 minutes",
    "february": "February - Python 30 minutes",
    "march": "March - Django 30 minutes",
    "april": "April - DRF 30 minutes",
    "may": "May - Springboot 30 minutes",
    "june": "June - Problem Solving 30 minutes",
    "july": "July - Machine Learning 30 minutes",
    "august": "August - Exercise 30 minutes",
    "september": "September - content creation 60 minutes",
    "october": "October - play flute 30 minutes",
    "november": "November - play guitar 30 minutes",
    "december": "December - business development 30 minutes"
}

def monthly_challenge_by_number(request, month):
   months = list(monthly_challenges.keys())
   redirect_month = months[month]
   return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse (challenge_text)
    except:
        return HttpResponseNotFound("This month in not supported!")