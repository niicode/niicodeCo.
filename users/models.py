from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


class BlogUserManager(BaseUserManager):

    def create_user(self, phone_number, first_name, last_name, password=None):
        if not phone_number:
            raise ValueError('Users must have an email address')

        user = self.model(
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number, password, first_name, last_name):
        user = self.create_user(phone_number,
                                password=password,
                                first_name=first_name,
                                last_name=last_name)
        user.is_admin = True
        user.save(using=self._db)
        return user


class BlogUser(AbstractBaseUser):

    email = models.EmailField(
        verbose_name=_('email address'),
        unique=True,
        max_length=255
    )
    username = models.CharField(
        verbose_name=_('username'),
        max_length=100,
        default='0200000000',
    )
    first_name = models.CharField(default=' ', max_length=100)
    phone_number = models.CharField(unique=True, max_length=100)
    last_name = models.CharField(default=' ', max_length=100)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = BlogUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return '''{} {}'''.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('-id', )
        verbose_name = _('user')
        verbose_name_plural = _('users')

