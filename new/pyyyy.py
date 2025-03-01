from new.models import *
from datetime import datetime

# 1 savol object yaratish
Hub = Blog.objects.create(name="Beatles Blog",tagline="...")
#2 savol  name="Cheddar Talk" va tagline="Say cheese!"  yaratib uni qaytarsa boladimi yoqmi tekshirish True yoki false bilan
H = Blog.objects.create(name="Cheddar Talk" ,tagline="Say cheese!") 
# qaytarsa boladim yoqmi tekshirish
Chees = Blog.objects.filter(name="Cheddar Talk" ,tagline="Say cheese!").exists()
Chees

# savol 3  O  yozilgan barhca  mualiflarni toping Oldindan Birnecha objects lar yaratganim uchun  yaratib otiqmayman qayta
f = Author.objects.filter(name__icontains="o")
f 
# savol 4 2021 yilda nashir qilngan Entry larni topish  
y =  Entry.objects.filter(pub_date__year=2025)#chunki menda 2025 yildagi malumot bor faqat
y 
# savol 5 pub_date boyicha tartiblab boshidagi uchutasi olib tashlash har brinir
d = Entry.objects.order_by('-pub_date')[:3]
d
# savol 6 sarlavhasida ("headline") "Bio" so‘zini o‘z ichiga olgan Entry obyektlarini topish
f = Entry.objects.filter(headline__icontains="Bio")
f 
# savol 7  
g = Blog.objects.get(name="Tadam")
t  = Entry.objects.filter(blog=g)
td  = Entry.objects.filter(blog=g).exists()
print(g) 
print(d)
#savol 8 
g = Author.objects.get(name="Nurullo")
t  = Entry.objects.filter(authors=g)
if t.exists():
	print(f"{g}tegishli bolgan barcha postlar\n"  +  "\n".join([entry.headline for entry in t]))
else:
	print("Bu user yozgan maqola topilmadi")
# 9 savol javobi 
john = Author.objects.create(name="John", email="nurullo@nurullo.uz")
paul = Author.objects.create(name="Paul", email="nurullo@nurullo.uz")
george = Author.objects.create(name="George", email="nurullo@nurullo.uz")
entry1 = Entry.objects.create(blog=beatles_blog, headline="John's Journey", body_text="Story of John", pub_date="2024-02-27")
entry1.authors.add(john)
entry2 = Entry.objects.create(blog=beatles_blog, headline="Paul's Melodies", body_text="Music by Paul", pub_date="2024-02-26")
entry2.authors.add(paul)
entry3 = Entry.objects.create(blog=beatles_blog, headline="George's Guitar", body_text="George and his guitar", pub_date="2024-02-25")
entry3.authors.add(george)
entry4 = Entry.objects.create(blog=beatles_blog, headline="Collaboration", body_text="George & Paul working together", pub_date="2024-02-24")
entry4.authors.add(george, paul)
#endi savolni bajaramiz
Blog = Blog.objects.get(name="Beatles Blog")
george = Author.objects.get(name="George")
paul =  Author.objects.get(name="Paul")

Entry = Entry.objects.filter(blog=Blog,authors=george).exclude(authors=paul)
Entry
# 10 savol javobi
entries = Entry.objects.filter(pub_date__range=("2015-01-01","2020-12-31"))
c = entries.count()
c
#11 savol javobi ...
max_of_comment = Entry.objects.filter(number_of_comments__gt=F('number_of_pingbacks'))
max_of_comment
# 12 savol
from django.db.models import F

entry = Entry.objects.create(
    blog=bo,  
    headline="Django i18n",
    body_text="Localization in Django",
    pub_date="2024-03-15",
    number_of_comments=500,
    number_of_pingbacks=400
)

plus_1_of_comment = Entry.objects.filter(number_of_comments=F('number_of_pingbacks')+1)
plus_1_of_comment
# ozim uchun yengli anonate va ExpressionWrapper
add_new_field  = Entry.objects.annotate(
	ratio=ExpressionWrapper(
		F('number_of_pingbacks') / F('number_of_comments') ,output_field=FloatField()
		)
	)
add_new_field
add_new =Entry.objects.annotate(
>>>	sum_of_2 = ExpressionWrapper(
>>>		F('number_of_pingbacks') + F('number_of_comments'),output_field=IntegerField()
>>>		)
>>>	)
>>>add_new
>>>#13 
>>>blogs_with_lennon = Blog.objects.filter(entry__headline__icontains="Lennon").distinct()
>>>blogs_with_lennon
>>>#14
>>>jazz_blog = Blog.objects.create(name="Jazz Blog", tagline="Smooth & All That Jazz")
>>>pop_blog = Blog.objects.create(name="Pop Music Blog", tagline="Chart Toppers")
>>>music_blogs = Blog.objects.filter(tagline__icontains="music")
>>># 15
>>>entry_django_tips = Entry.objects.filter(headline__icontains="Django").filter(headline__icontains="Tips")
>>>
>>>from django.db.models import Count
>>>
>>>blogs_with_authors_count = Blog.objects.annotate(num_authors=Count('entry__authors', distinct=True))

