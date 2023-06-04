from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView
from .models import Person, FamilyMember
from .forms import PersonCustomForm, FamilyMemberCustomForm

class PersonsPageView(ListView):
	model = Person
	template_name = "personview.html"
	context_object_name = "persons"

class PersonsDetailView(DetailView):
	model = Person
	template_name = "persondetail.html"
	context_object_name = "person"

class PersonChangeView(UpdateView):
	model = Person
	template_name = "personchange.html"
	fields = ['firstname', 'lastname', 'fathername', 'birthday', 'status', 'statusdate', 'otherdata']

def create_person(request):
	if (request.method == 'POST'):
		p_form = PersonCustomForm(request.POST)
		m_form = FamilyMemberCustomForm(request.POST)
		if (p_form.is_valid() and m_form.is_valid()):
			p_firstname = p_form.cleaned_data['firstname']
			p_lastname = p_form.cleaned_data['lastname']
			p_fathername = p_form.cleaned_data['fathername']
			p_birthday = p_form.cleaned_data['birthday']
			p_status = p_form.cleaned_data['status']
			p_statusdate = p_form.cleaned_data['statusdate']
			p_otherdata = p_form.cleaned_data['otherdata']
			person = Person.objects.create(firstname = p_firstname, lastname = p_lastname, fathername = p_fathername, birthday = p_birthday, status = p_status, statusdate = p_statusdate, otherdata = p_otherdata)
			person.save()


			m_firstname = m_form.cleaned_data['memberfirstname']
			m_lastname = m_form.cleaned_data['memberlastname']
			m_fathername = m_form.cleaned_data['memberfathername']
			m_birthday = m_form.cleaned_data['memberbirthday']
			m_social = m_form.cleaned_data['social']
			m_otherdata = m_form.cleaned_data['memberotherdata']
			m_mobilized = Person.objects.filter(firstname = p_firstname, lastname = p_lastname, fathername = p_fathername, birthday = p_birthday)[0]
			m_relation = m_form.cleaned_data['relation']
			m_phonenumber = m_form.cleaned_data['phonenumber']
			m_index = m_form.cleaned_data['index']
			m_city = m_form.cleaned_data['city']
			m_street = m_form.cleaned_data['street']
			m_building = m_form.cleaned_data['building']
			m_apartment = m_form.cleaned_data['apartment']			
			member = FamilyMember.objects.create(memberfirstname = m_firstname, memberlastname = m_lastname, memberfathername = m_fathername, memberbirthday = m_birthday, social = m_social, relation = m_relation, phonenumber = m_phonenumber, memberotherdata = m_otherdata, mobilized = m_mobilized, index = m_index, city = m_city, street = m_street, building = m_building, apartment = m_apartment)
			member.save()

			return HttpResponseRedirect('/')
	p_form = PersonCustomForm()
	m_form = FamilyMemberCustomForm()
	return render(request, 'personnew.html', {'p_form' : p_form, 'm_form' : m_form})



#class PersonNewView(CreateView):
#	form = PersonCustomForm()
#	model = Person
#	template_name = "personnew.html"
#	fields = ['firstname', 'lastname', 'fathername', 'birthday', 'status', 'statusdate', 'otherdata']

# def home(request):
# 	return HttpResponse('<h1>Главная</h1>')
 
# def about(request):
# 	return HttpResponse('<h1>Наш клуб</h1>')