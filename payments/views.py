from django.shortcuts import render, HttpResponsePermanentRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Payment
from account.models import Profile
from django.conf import settings

@login_required(login_url="/account/signin/")
def initiate_payment(request):
	if request.method == "POST":
		amount = request.POST['amount']
		email = request.POST['email']

		pk = settings.PAYSTACK_PUBLIC_KEY

		payment = Payment.objects.create(amount=amount, email=email, user=request.user)
		payment.save()

		context = {
			'payment': payment,
			'field_values': request.POST,
			'paystack_pub_key': pk,
			'amount_value': payment.amount_value(),
		}
		return render(request, 'make_payment.html', context)

	return render(request, 'payment.html')

@login_required(login_url="/account/signin/")
def verify_payment(request, ref):
	payment = Payment.objects.get(ref=ref)
	verified = payment.verify_payment()

	if verified:
		#calculate point
		total_point = int(payment.amount / 10)
		user_profile = Profile.objects.get(user=request.user)
		#update point fieldd
		user_profile.point += total_point
		user_profile.save()
		# user_wallet = UserWallet.objects.get(user=request.user)
		# user_wallet.balance += payment.amount
		# user_wallet.save()
		print(total_point)
		messages.success(request, f'congardulation you have purchased {total_point} points !!!')
		return render(request, "success.html", {'total_point' : total_point})
	return render(request, "success.html")