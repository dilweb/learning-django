from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


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