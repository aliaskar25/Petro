from django.contrib import admin
from django import forms
from django.urls import path
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import get_user_model

from .models import Order

import csv
import codecs
from datetime import date


User = get_user_model()


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    change_list_template = "entities/heroes_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]

            if not csv_file.name.endswith(".csv"):
                self.message_user(request, 'Only .csv files', level=messages.ERROR)
                return redirect("..")

            csv_file.seek(0)
            data = csv.DictReader(codecs.iterdecode(csv_file, 'utf-8'))

            for i in data:
                birth_date = i['BirthDate'].split('/')
                birth_date = date(
                    year=int(birth_date[0]), 
                    month=int(birth_date[1]), 
                    day=int(birth_date[2])
                )
                registration_date = i['RegistrationDate'].split('/')
                registration_date = date(
                    year=int(registration_date[0]), 
                    month=int(registration_date[1]), 
                    day=int(registration_date[2])
                )
                try:
                    user = User.objects.create(
                        first_name=i['FirstName'],
                        last_name=i['LastName'],
                        birth_date=birth_date,
                        registration_date=registration_date
                    )
                    user.save()
                except:
                    pass

            self.message_user(request, "Users have been added")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(
            request, "csv_form.html", payload
        )


admin.site.register(Order)