from django.db import models

class Job(models.Model):
    STATUS_CHOICES = [
        ('saved', 'Saved'),
        ('applied', 'Applied'),
        ('interview', 'Interview'),
        ('rejected', 'Rejected'),
        ('offer', 'Offer'),
    ]

    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    link = models.URLField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='saved')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.company}"