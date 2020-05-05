# Send email 
This code is intended for checking and sending email
There are a few steps you need to take before you can send emails through Gmail with SMTP, 
and it has to do with authentication. If you're using Gmail as the provider, 
you'll need to tell Google to allow you to connect via SMTP, which is considered a "less secure" method.

First, you'll want to allow less secure apps to access your account.
For detailed instructions on how to do this, you should check out this page: https://support.google.com/accounts/answer/6010255

If you have 2-step verification enabled on your account, then you'll need to create an app-specific password for less secure apps like this.
In that case, you'll need to follow the instructions here: https://support.google.com/accounts/answer/185833

And finally, if you're still getting an SMTPAuthenticationError with an error code of 534,
then you'll need to do yet another step for this to work. https://accounts.google.com/b/0/DisplayUnlockCaptcha

For check the email address use https://pypi.org/project/validate_email module
