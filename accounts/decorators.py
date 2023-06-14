from django.contrib.auth.decorators import user_passes_test


def payment_required(f):
    return user_passes_test(lambda u: u.has_paid, login_url='/home')(f)
