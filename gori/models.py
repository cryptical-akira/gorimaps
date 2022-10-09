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
    post_img = models.ImageField(upload_to = "historyimgs", null=True)
    def __str__(self):
        return str(self.post_title)

class Culture(models.Model):
    post_title = models.ForeignKey(MultilanguageText, on_delete=models.CASCADE, related_name='posttitleculture', null=True)
    post_text = models.ForeignKey(MultilanguageTextField, on_delete=models.CASCADE, related_name='posttextculture', null=True)
    post_author = models.ForeignKey(MultilanguageText, on_delete=models.CASCADE, related_name='postauthorculture', null=True)
    post_img = models.ImageField(upload_to = "cultureimgs", null=True)
    def __str__(self):
        return str(self.post_title)
        
class Architect(models.Model):
    post_title = models.ForeignKey(MultilanguageText, on_delete=models.CASCADE, related_name='posttitlearchitect', null=True)
    post_text = models.ForeignKey(MultilanguageTextField, on_delete=models.CASCADE, related_name='posttextarchitect', null=True)
    post_author = models.ForeignKey(MultilanguageText, on_delete=models.CASCADE, related_name='postauthorarchitect', null=True)
    post_img = models.ImageField(upload_to = "architectimgs", null=True)
    def __str__(self):
        return str(self.post_title)

class AboutProjectDonors(models.Model):
    project_info = models.ForeignKey(MultilanguageTextField, on_delete=models.CASCADE, related_name='aboutproject', null=True)
    post_img_first = models.ImageField(upload_to = "aboutproject", null=True)
    post_img_second = models.ImageField(upload_to = "aboutproject", null=True)
    donors_text = models.ForeignKey(MultilanguageTextField, on_delete=models.CASCADE, related_name='aboutprojectdonors', null=True)
    support_text = models.ForeignKey(MultilanguageTextField, on_delete=models.CASCADE, related_name='aboutprojectsupports', null=True)
    def __str__(self):
        return str('About Project')