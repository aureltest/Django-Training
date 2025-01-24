from django.shortcuts import render, get_object_or_404
from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandForm, ListingForm
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages


def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", {"bands": bands})


def band_detail(request, id):  # notez le paramètre id supplémentaire
    band = get_object_or_404(
        Band, id=id
    )  # https://docs.djangoproject.com/fr/3.2/topics/http/shortcuts/#get-object-or-404
    return render(
        request, "listings/band_detail.html", {"band": band}
    )  # nous passons l'id au modèle


def band_create(request):
    if request.method == "POST":
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            messages.success(
                request, f'Le groupe "{band.name}" a été crée avec succès.'
            )
            return redirect("band-detail", band.id)
    else:
        form = BandForm()
    return render(request, "listings/band_create.html", {"form": form})


def band_update(request, id):
    band = get_object_or_404(Band, id=id)
    if request.method == "POST":
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Le groupe "{band.name}" a été modifié avec succès.'
            )
            return redirect("band-detail", band.id)
    else:
        form = BandForm(instance=band)
    return render(request, "listings/band_update.html", {"form": form, "band": band})


def band_delete(request, id):
    band = get_object_or_404(Band, id=id)
    if request.method == "POST":
        band.delete()
        messages.success(
            request, f'Le groupe "{band.name}" a été supprimé avec succès.'
        )
        return redirect("band-list")
    return render(request, "listings/band_delete.html", {"band": band})


def annonce_list(request):
    lists = Listing.objects.all()
    return render(request, "listings/annonce_list.html", {"lists": lists})


def annonce_detail(request, id):  # notez le paramètre id supplémentaire
    list = get_object_or_404(
        Listing, id=id
    )  # https://docs.djangoproject.com/fr/3.2/topics/http/shortcuts/#get-object-or-404
    return render(
        request, "listings/annonce_detail.html", {"list": list}
    )  # nous passons l'id au modèle


def annonce_create(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            list = form.save()
            messages.success(
                request, f'L"annonce "{list.title}" a été crée avec succès.'
            )
            return redirect("annonce-detail", list.id)
    else:
        form = ListingForm()
    return render(request, "listings/annonce_create.html", {"form": form})


def annonce_update(request, id):
    list = get_object_or_404(Listing, id=id)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=list)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'L"annonce "{list.title}" a été modifiée avec succès.'
            )
            return redirect("annonce-detail", list.id)
    else:
        form = ListingForm(instance=list)
    return render(request, "listings/annonce_update.html", {"form": form, "list": list})


def annonce_delete(request, id):
    list = get_object_or_404(Listing, id=id)
    if request.method == "POST":
        list.delete()
        messages.success(
            request, f"L'annonce '{list.title}' a été supprimé avec succès."
        )
        return redirect("annonce-list")
    return render(request, "listings/annonce_delete.html", {"list": list})


def contact(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=["admin@merchex.xyz"],
            )
            return redirect("email-sent")
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
        form = ContactUsForm()  # ajout d’un nouveau formulaire ici
    return render(request, "listings/contact.html", {"form": form})


def email_sent(request):
    return render(request, "listings/email_sent.html")


def about(request):
    return render(request, "listings/about.html")


def custom_404(request, exception):
    return render(request, "404.html", status=404)
