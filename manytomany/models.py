from django.db import models

class Doctor(models.Model):
    name = models.TextField()

class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    # related_name으로 역참조 이름을 반드시 설정해줘야 충돌을 막을 수 있다.

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now_add=True)
    place = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.pk} 예약: {self.doctor.name}의 환자 {self.patient.name}'