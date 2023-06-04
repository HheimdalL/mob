from django.db import models
from django.urls import reverse



class Index(models.Model):
    name = models.CharField(max_length = 6)
    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length = 35)
    def __str__(self):
        return self.name
    
class Street(models.Model):
    name = models.CharField(max_length = 35)
    def __str__(self):
        return self.name
    
class Person(models.Model):
    STATUS_TYPES_CHOISES = [
        ("M", "Мобилизованный"),
        ("W", "Военнослужащий"),
        ("D", "Погибший"),
        ("C", "Комиссованный"),
        ("L", "Пропавший без вести"),
    ]
    firstname = models.CharField("Фамилия", max_length = 35)
    lastname = models.CharField("Имя", max_length = 35)
    fathername = models.CharField("Отчество", max_length = 35)
    birthday = models.DateField("Дата рождения")
    status = models.CharField("Статус военнослужащего", max_length=1, choices=STATUS_TYPES_CHOISES, blank=False)
    statusdate = models.DateField("Дата получения статуса")
    otherdata = models.CharField("Примечание", max_length = 100)


    def __str__(self):
        return self.firstname + " " + self.lastname + " " + self.fathername + " " + str(self.birthday)
    
    def get_absolute_url(self): # new
        return reverse('home')

class FamilyMember(models.Model):
    RELATION_TYPES_CHOISES = [
        ("W", "Жена/Муж"),
        ("M", "Мать/Отец"),
        ("C", "Гражданская жена"),
        ("S", "Сын/Дочь"),
    ]
    SOCIAL_TYPES_CHOISES = [
        ("W", "Трудоспособный"),
        ("P", "Пенсионер"),
        ("D", "Инвалид"),
    ]
    phonenumber = models.CharField("Номер телефона", max_length=14)
    memberfirstname = models.CharField("Фамилия", max_length = 35)
    memberlastname = models.CharField("Имя", max_length = 35)
    memberfathername = models.CharField("Отчество", max_length = 35)
    memberbirthday = models.DateField("Дата рождения")
    social = models.CharField("Социальный статус", max_length=1, choices=SOCIAL_TYPES_CHOISES, blank=False)        
    relation = models.CharField("Семейный статус", max_length=1, choices=RELATION_TYPES_CHOISES, blank=False)
    memberotherdata = models.CharField("Примечание", max_length = 100)
    
    mobilized = models.ForeignKey(Person, on_delete=models.CASCADE)
    
    index = models.ForeignKey(Index, on_delete=models.CASCADE, verbose_name="Почтовый индекс")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="Название населенного пункта")
    street = models.ForeignKey(Street, on_delete=models.CASCADE, verbose_name="Улица")
    building = models.CharField("Номер дома", max_length = 10)
    apartment = models.IntegerField("Номер квартиры")
    
    def __str__(self):
        return self.memberfirstname + " " + self.memberlastname + " " + self.memberfathername + " " + str(self.memberbirthday)

class Needs(models.Model):
    needname = models.CharField(max_length=45)
    memberid = models.ManyToManyField(FamilyMember, through='Protocol')
    def __str__(self):
        return self.needname

class Protocol(models.Model):
    member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    need = models.ForeignKey(Needs, on_delete=models.CASCADE)
    number = models.IntegerField()
    date = models.DateField()
    expiredate = models.DateField() 
    reportdate = models.DateField() 
    complete = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    def __str__(self):
        return str(self.number) + " " + str(self.date) + " " + self.member.memberfirstname + " " + self.member.memberlastname + " " + self.member.memberfathername + " " + str(self.member.memberbirthday) + " " + self.need.needname


# Create your models here.
