from django.contrib.auth.models import User
from django.db import models


# Create your models here.
"""
class SessionYearModel(models.Model):
    id = models.AutoField(primary_key=True)
    session_start_year = models.DateField()
    session_end_year = models.DateField()
    objects = models.Manager()


class CustomUser(AbstractUser):
    user_type_data = ((1, "Admin"), (2, "Staff"), (3, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class Staffs(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class Students(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    gender = models.CharField(max_length=50)
    profile_pic = models.FileField()
    address = models.TextField()
    branch = models.CharField(max_length=50)
    course_id = models.ForeignKey(Courses, on_delete=models.DO_NOTHING, default=1)
    session_year_id = models.ForeignKey(SessionYearModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


class Payment(models.Model):
	id = models.AutoField(primary_key=True)
	fee_type = models.CharField()
	student_id = models.ForeignKey(Students, on_delete=models.DO_NOTHING)
	amount_paid = models.FloatField()
	ref_no = models.CharField(max_length=50, default=None)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

class Fee_Structure(models.Model):
	id = models.AutoField(primary_key=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Tuition_Fee(models.Model):
	category = 
	amount = 

"""
class Student(models.Model):

	BRANCH = (
		('CSE','CSE'),
		('ISE','ISE'),
		('ME','ME'),
		('CVE','CVE'),
		('ECE','ECE'),
		('EEE','EEE'),
		('Aeronautical/ Aerospace Eng','AE'),
		('Artificial Intelligence Eng','AIE'),
		)


	CATEGORY1 = (
		('KCET','KCET'),
		('COMEDK','COMEDK'),
		('MANAGEMENT','MANAGEMENT')
		)


	EDUCATIONAL_LEVEL = (
		('12','12'),
		('DIPLOMA','DIPLOMA'),
		)

	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	usn = models.CharField(max_length=200, unique=True, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	ad_date = models.DateField()
	batch = models.CharField(max_length=10)
	branch = models.CharField(max_length=50, choices=BRANCH)
	sem = models.CharField(max_length=5)	
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	profile_pic = models.ImageField(default="default_profile_pic.png",null=True)
	category = models.CharField(max_length=20, choices=CATEGORY1) 
	ed_level = models.CharField(max_length=20, choices=EDUCATIONAL_LEVEL)

	def __str__(self):
		return self.name

	#def __str__(self):
	#	return '%s %s' % (self.student_name, self.batch)
	
	


"""
class Student_Profile(models.Model):

	student = models.OneToOneField(Student, on_delete=models.CASCADE, null=True)
	email = models.EmailField(max_length=50)
	father_name = models.CharField(max_length=50) 
	mother_name = models.CharField(max_length=50)
	phone1 = models.CharField(max_length=20) 
	phone2 = models.CharField(max_length=20)
	address = models.CharField(max_length=200)
	photo = models.ImageField(upload_to='images/')
	dob = models.DateField(null=True) 
	caste = models.CharField(max_length=20)
	subcaste = models.CharField(max_length=20)
	aadhar = models.CharField(max_length=20)

	def __str__(self):
		return (self.email)
"""

#------- fee structure---------
"""
	ENTRY = (
		('KCET', 'KCET'),
		('COMEDK', 'COMEDK'),
		('MANAGEMENT', 'MANAGEMENT'),
	)

	QUOTA = (
		('GENERAL MERIT','GM'),
		('OTHER BACKWARD CLASSES','OBC'),
		('SC/ST','SC/ST'),
		('CAT-1',(
				('IC < 2.5 LPA','IC < 2.5 LPA'),
				('IC > 2.5 LPA','IC > 2.5 LPA'),
			)
		),
	)

	COLLEGE_TYPE = (
		('GOVT / AIDED','GOVT / AIDED'),
		('Deemed / PRIV. Univ','Deemed / PRIV. Univ'),
		('ALL-COLLEGES','ALL'),
		)

	COURSE = (
		('ENGINEERING/ARCHITECTURE','ENGINEERING/ARCHITECTURE'),
		('ENGINEERING SNQ','ENGINEERING SNQ'),
		)
"""

class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name


class Fee(models.Model):

	CATEGORY = (
		('Tuition_Fee','Tuition_Fee'),
		('Miscellaneous_Fee','Miscellaneous_Fee'),
		('University_Fee','University_Fee'),
		)

	name = models.CharField(max_length=200, null=True)
	amount = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name
	
	"""
	course = models.CharField(max_length=50, choices=COURSE)
	college_type = models.CharField(max_length=50, choices=COLLEGE_TYPE)
	entry = models.CharField(max_length=20, choices=ENTRY)
	quota = models.CharField(max_length=50, choices=QUOTA)
	amount = models.FloatField()
	date_created = models.DateTimeField(auto_now_add=True)
	ayear = models.DateField()

	"""

	


class Payment(models.Model):

	STATUS = (
		('Pending', 'Pending'),
		('Recieved', 'Recieved'),
		('Acknowledged', 'Acknowledged'),
		)
	MODE_OF_PAYMENT = (
		('NEFT','NEFT'),
		('BANK-TO-BANK','BANK-TO-BANK'),
		('NETBANKING','NETBANKING'),
		('CASH','CASH'),
		)
	student = models.ForeignKey(Student, null=True, on_delete= models.SET_NULL)
	fee = models.ForeignKey(Fee, null=True, on_delete= models.SET_NULL)
	amount_paid = models.FloatField()
	mode_payment = models.CharField(max_length=25, choices=MODE_OF_PAYMENT)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	def __str__(self):
		return str(self.fee)


