from dj_rest_auth.serializers import PasswordResetSerializer


class CustomPasswordResetSerializer(PasswordResetSerializer):
    def save(self):
        request = self.context.get('request')
        # Set some values to trigger the send_email method.
        opts = {
            'use_https': request.is_secure(),
            'from_email': 'admin@c3n7.games',
            'request': request,
            # here I have set my desired template to be used
            # don't forget to add your templates directory in settings to be found
            # Reference:
            # /venv/lib/python3.9/site-packages/django/contrib/admin/templates/registration/
            'email_template_name': 'password_reset_email.html'
        }

        opts.update(self.get_email_options())
        self.reset_form.save(**opts)
