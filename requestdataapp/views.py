from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

from .forms import UserBioForm

# Create your views here.
def process_get_view(request: HttpRequest) -> HttpResponse:

		a = request.GET.get("a", "")
		b = request.GET.get("b", "")
		result = a + b
		context = {
			"a": a,
			"b": b,
			"result": result
		}
		return render(request, "requestdataapp/request-querry-params.html", context=context)


def user_form(request: HttpRequest) -> HttpResponse:
	submitted = False
	submitted_data = None
	if request.method == "POST":
		form = UserBioForm(request.POST)
		if form.is_valid():
			submitted = True
			submitted_data = form.cleaned_data
			# Print results to console as requested (minimal behavior)
			print("UserBioForm submitted:", submitted_data)
			# Recreate empty form for further input
			form = UserBioForm()
	else:
		form = UserBioForm()

	context = {
		"form": form,
		"submitted": submitted,
		"submitted_data": submitted_data,
	}
	return render(request, "requestdataapp/user-bio-form.html", context=context)
