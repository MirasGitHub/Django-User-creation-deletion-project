from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView

from users.forms import UserForm
from users.models import User


# Create your views here.


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def create_user(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('user_list')

    return render(request, 'create_user.html', {'form': form})


class DeleteUserView(APIView):
    def delete(self, request, pk):
        event = User.objects.get(pk=pk)
        event.delete()
        return Response('Deletion Successful')
