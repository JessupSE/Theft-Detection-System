from django.db import models

class Alert(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    alert_type = models.CharField(max_length=100)
    message = models.TextField()
    status = models.CharField(max_length=50, default="unread")

    def __str__(self):
        return f"{self.alert_type} - {self.timestamp}"

# class MediaFile(models.Model):
#     alert = models.ForeignKey(Alert, on_delete=models.CASCADE, related_name='media')
#     file_type = models.CharField(max_length=20)  # photo or video
#     file_url = models.URLField()
#     uploaded_at = models.DateTimeField(auto_now_add=True)

class MediaFile(models.Model):
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE, related_name='media')
    file_type = models.CharField(max_length=20)  # e.g., 'photo' or 'video'
    file = models.FileField(upload_to='media/')  # for uploading real files
    uploaded_at = models.DateTimeField(auto_now_add=True)


class KnownPerson(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='faces/')
    risk_level = models.CharField(max_length=50)

    def __str__(self):
        return self.name
