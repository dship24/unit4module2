from django.shortcuts import render
from django.http.response import HttpResponse
from typing import List
from dataclasses import dataclass

@dataclass
class Team():
    name: str
    description: str
    members: List[str]


def home(request, name):
    context = {
        "name": name,
        "Teams": {
            "procurement": Team("Procurement Team", "The procurement team is mainly in charge of providing food for all of Base Camp and supplying all the other teams.", ["Richard", "Shiny Dylan", "Quinton", "Ethan", "Gary", "Mariann"]),
            "management": Team("Management Team", "The management team is in charge of chore management, laundry, schedules, and keeping everything organized.", ["Brock Lesnar", "Will", "Daelan", "Ed Sheeran", "John Lennon", "My Dad"]),
            "community": Team("Community Team", "The community team is in charge of planning Base Camp events and birthdays.", ["Rjay", "Ariyana", "Justin", "Logan W.", "Skatey_Dawg"]),
            "documentation": Team("Documentation Team", "The documentation team is in charge of managing Base Camp's social media accounts and capturing memorable moments.", ["Isaac", "Ben", "Makyla", "Ryan", "The man, the myth, the King of the Slowpokes, Ranch."])
    }
    }
    return render(request, "home.html", context)

def root(request):
    context = {
        "teams" : {
            "procurement": "Procurement Team",
            "management": "Management Team",
            "community": "Community Team",
            "documentation": "Documentation Team"
        }
    }
    return render(request, "index.html", context)