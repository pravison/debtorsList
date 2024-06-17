from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from . models import Defaulter
from account.models import Profile

# Create your views here.

def search(request):
    context = {
       
    }
    return render(request, 'search.html', context)

@login_required(login_url="/account/signin/")
def searchResults(request):
    user_profile = Profile.objects.get(user=request.user)
    if user_profile.point >= 1 :
        defaulters = Defaulter.objects.all().filter(cleared = False)
        query = request.GET.get('query')
        if not query:
            return redirect('search')
        else:
            defaulters = defaulters.filter(national_id__icontains=query)
            context ={ }

            if defaulters.exists():
                total_loans = defaulters.count()
                total_amount = defaulters.aggregate(Sum('amount_in_default'))['amount_in_default__sum']
                #sum of all loan taken before default 
                total_loans_taken = defaulters.aggregate(Sum('number_of_loans_taken'))['number_of_loans_taken__sum']
                average_loans_taken_before_default = (int(total_loans_taken)/int(total_loans))

                context['defaulters'] = defaulters
                context['total_amount'] = total_amount
                context['total_loans'] = total_loans
                context['average_loans_taken_before_default'] = average_loans_taken_before_default
                context['query'] =query
                # subtracting  users points
                user_profile = Profile.objects.get(user=request.user)
                #update point fieldd
                user_profile.point -=1
                user_profile.save()
            else:
                context['no_results'] =True
                context['query'] = query
                # subtracting  users points
                user_profile = Profile.objects.get(user=request.user)
                #update point fieldd
                user_profile.point -=1
                user_profile.save()
        
        return render(request, 'search-results.html', context)
    else:
        return redirect('initiate_payment')

@login_required(login_url="/account/signin/")
def addDefaulter(request):
    user_profile = Profile.objects.get(user=request.user)
    if user_profile.banned == True:
        messages.success(request, "Most of Your added data was verified and found to be false for that reason you've been banned from adding defaulters if you think this act is unfair launch a complain and we will work it through together  !!!")
        return redirect('search')
    else:
        if request.method == 'POST':
            customer_name = request.POST['customer_name']
            national_id = request.POST['national_id']
            customer_location = request.POST['customer_location']
            bussiness_type = request.POST['bussiness_type']
            number_of_loans_taken = request.POST['number_of_loans_taken']
            amount_in_default = request.POST['amount_in_default']
            date_defaulted = request.POST['date_defaulted']

            if Defaulter.objects.filter(national_id=national_id, added_by=request.user, cleared=False).exists():
                messages.success(request, "You already added this Customer for trying to duplicate you will be deducted 1 point  !!!")
                # adding user points
                user_profile = Profile.objects.get(user=request.user)
                #update point fieldd
                user_profile.point -=1
                user_profile.save()
                return redirect('search')
            else:
            # get company defaulter 
                try:
                    profile = request.user.profile
                    company  = profile.company_name
                except Profile.DoesNotExist:
                    company  = f' {request.user.first_name}  {request.user.last_name}'
                print(company)
                defaulter = Defaulter(customer_name=customer_name, added_by= request.user,  national_id=national_id, customer_location=customer_location, bussiness_type=bussiness_type, number_of_loans_taken=number_of_loans_taken, amount_in_default=amount_in_default, date_defaulted=date_defaulted, company_defaulted = company )
                defaulter.save()
                messages.success(request, "You have succefully added a defaulter plus gained one point  !!!")
                # adding user points
                user_profile = Profile.objects.get(user=request.user)
                #update point fieldd
                user_profile.point +=1
                user_profile.save()
                return redirect('search')
        else:
            return render(request, 'add-defaulter.html')
    

def clearDefaulter(request):
    customer_id = request.GET.get('customer', 0)
    defaulter = Defaulter.objects.get(id=customer_id)
    #update cleared fieldd
    defaulter.cleared = True
    defaulter.save()
    messages.success(request, "You have succefully cleared customer from defaulters list  !!!")
    return redirect('search')