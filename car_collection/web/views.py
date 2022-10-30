from django.shortcuts import render, redirect
from car_collection.web.forms import ProfileCreateForm, CarCreateForm, CarDeleteForm, ProfileDeleteForm, \
    ProfileEditForm, CarEditForm
from car_collection.web.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        return create_profile(request)

    context = {
        'profile': Car.objects.all(),
    }

    return render(
        request,
        'index.html',
        context,
    )


def details_car(request, pk):
    car = Car.objects \
        .filter(pk=pk) \
        .get()

    context = {
        'car': car,
    }

    return render(
        request,
        'car/car-details.html',
        context,
    )


def add_car(request):
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(
        request,
        'car/car-create.html',
        context,
    )


def edit_car(request, pk):
    car = Car.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'car': car,
    }


def delete_car(request, pk):
    car = Car.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('view catalogue')

    context = {
        'form': form,
        'car': car,
    }

    return render(
        request,
        'car/car-delete.html',
        context,
    )


def create_profile(request):
    if get_profile() is not None:
        return redirect('index')

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'hide_nav_links': True,
    }

    return render(
        request,
        'profiles/profile-create.html',
        context,
    )


def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
    }


def edit_profile(request, pk):
    profile = Profile.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(
        request,
        'profiles/profile-edit.html',
        context,
    )


def details_profile(request):
    profile = get_profile()
    cars_count = Profile.objects.count()
    car_price = Profile.objects.count()

    context = {
        'profile': profile,
        'cars_count': cars_count,
        'car_price': car_price,
    }

    return render(
        request,
        'profiles/profile-details.html',
        context,
    )


def view_catalogue(request):
    car = Car.objects.all()
    total_cars = Car.objects.count()

    context = {
        'car': car,
        'total_cars': total_cars,

    }
    return render(
        request,
        'catalogue.html',
        context,
    )

