from django.db import models
from django.utils.translation import get_language, gettext_lazy as _
from django.conf import settings
from django.db.models.deletion import CASCADE, PROTECT
from django.core.exceptions import ValidationError
from transl.models import MultilanguageText, MultilanguageTextField

class History(models.Model):
    post_title = models.ForeignKey(MultilanguageText, on_delete=models.CASCADE, related_name='posttitle', null=True)
    post_text = models.ForeignKey(MultilanguageTextField, on_delete=models.CASCADE, related_name='posttext', null=True)
    post_author = models.ForeignKey(MultilanguageText, on_delete=models.CASCADE, related_name='postauthor', null=True)
    post_videos = models.ForeignKey(MultilanguageTextField, on_delete=models.CASCADE, related_name='historyvideo', null=True, blank=True)
    post_img = models.ImageField(upload_to = "historyimgs", null=True, blank=True, default='humansimg/default.png')
    def __str__(self):
        return str(self.post_title)

    def class_name(self):
        return self.__class__.__name__
    
    def serialize(self):
        return {
            'title': self.post_text,
            'body': self.post_text,
            'image': self.post_img.url,
        }

class Culture(models.Model):
    post_title = models.ForeignKey(MultilanguageText, on_delete=models.CASCADE, related_name='posttitleculture', null=True)
    post_text = models.ForeignKey(MultilanguageTextField, on_delete=models.CASCADE, related_name='posttextculture', null=True)
    post_author = models.ForeignKey(MultilanguageText, on_delete=models.CASCADE, related_name='postauthorculture', null=True)
    post_videos = models.ForeignKey(MultilanguageTextField, on_delete=models.CASCADE, related_name='culturevideo', null=True, blank=True)
    post_img = models.ImageField(upload_to = "cultureimgs", null=True, blank=True, default='humansimg/default.png')
    def __str__(self):
        return str(self.post_title)

    def class_name(self):
        return self.__class__.__name__
        
class Architect(models.Model):
    post_title = models.ForeignKey(MultilanguageText, on_delete=models.CASCADE, related_name='posttitlearchitect', null=True)
    post_text = models.ForeignKey(MultilanguageTextField, on_delete=models.CASCADE, related_name='posttextarchitect', null=True)
    post_author = models.ForeignKey(MultilanguageText, on_delete=models.CASCADE, related_name='postauthorarchitect', null=True)
    post_videos = models.ForeignKey(MultilanguageTextField, on_delete=models.CASCADE, related_name='architectvideo', null=True, blank=True)
    post_img = models.ImageField(upload_to = "architectimgs", null=True, blank=True, default='humansimg/default.png')
    def __str__(self):
        return str(self.post_title)

    def class_name(self):
        return self.__class__.__name__

class AboutProjectDonors(models.Model):
    project_info = models.ForeignKey(MultilanguageTextField, on_delete=models.CASCADE, related_name='aboutproject', null=True)
    donors_text = models.ForeignKey(MultilanguageTextField, on_delete=models.CASCADE, related_name='aboutprojectdonors', null=True)
    support_text = models.ForeignKey(MultilanguageTextField, on_delete=models.CASCADE, related_name='aboutprojectsupports', null=True)
    def __str__(self):
        return str('About Project')

class Human(models.Model):
    post_title =  models.ForeignKey(MultilanguageTextField, on_delete=models.CASCADE, related_name='humans', null=True)
    post_text =  models.ForeignKey(MultilanguageTextField, on_delete=models.CASCADE, related_name='huamnstext', null=True)
    post_image_description =  models.ForeignKey(MultilanguageTextField, on_delete=models.CASCADE, related_name='humanimgdescription', null=True, blank=True)
    post_img = models.ImageField(upload_to = "humansimg", null=True, blank=True, default='humansimg/default.png')
    post_cover_img = models.ImageField(upload_to = "humanscoverimg", null=True, blank=True, default='None')
    def __str__(self):
        return str(self.post_title)

class Video(models.Model):
    video_title =  models.ForeignKey(MultilanguageTextField, on_delete=models.CASCADE, related_name='videos', null=True)
    video_src = models.ForeignKey(MultilanguageTextField, on_delete=models.CASCADE, related_name='videossrc', null=True)
    minutes = models.IntegerField(null=True)
    seconds = models.IntegerField(null=True)
    def __str__(self):
        return str(self.video_title)

class PinedPost(models.Model):
    pined_history_post_1 = models.ForeignKey(History, on_delete=models.CASCADE, related_name='historypost1', null=True)
    pined_history_post_2 = models.ForeignKey(History, on_delete=models.CASCADE, related_name='historypost2', null=True)
    pined_culture_post_1 = models.ForeignKey(Culture, on_delete=models.CASCADE, related_name='culturepost1', null=True)
    pined_culture_post_2 = models.ForeignKey(Culture, on_delete=models.CASCADE, related_name='culturepost2', null=True)
    pined_video_post_1 = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='videopost1', null=True)
    pined_video_post_2 = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='videopost2', null=True)
    pined_video_post_3 = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='videopost3', null=True)
    def __str__(self):
        return str("Pined Posts On Main Page")


class PostForPin(models.Model):
    post_title = models.CharField(default='', max_length=250)
    post_text = models.TextField(default='', max_length=5000)
    post_location_link = models.CharField(default='', max_length=1000, null=True, blank=True)
    post_location = models.CharField(default='', max_length=500, null=True, blank=True)
    post_videos = models.CharField(default='', max_length=500, blank=True)
    post_img = models.ImageField(upload_to = "postpinimg", null=True, blank=True)
    post_source = models.CharField(default='', max_length=500, blank=True)

    post_title_en = models.CharField(default='', max_length=250)
    post_text_en = models.TextField(default='', max_length=5000)
    post_videos_en = models.CharField(default='', max_length=500, blank=True)
    post_source_en = models.CharField(default='', max_length=500, blank=True)

    def __str__(self):
        return str(self.post_title)

    def class_name(self):
        return self.__class__.__name__
    
    def serialize(self):
        return {
            'title': self.post_title,
            'body': self.post_text,
            'video': self.post_videos,
            'img': self.post_img.url,
            'source': self.post_source,
            'title_en': self.post_title_en,
            'body_en': self.post_text_en,
            'video_en': self.post_videos_en,
            'source_en': self.post_source_en,
            'location': self.post_location,
            'location_link': self.post_location_link,
        }


class Pin(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    post = models.ForeignKey(
        PostForPin, on_delete=models.CASCADE, related_name='pins', null=True, db_constraint=False)

    def __str__(self):
        return f'{self.latitude},{self.longitude}'

    def serialize(self):
        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "post": self.post.serialize()
        }