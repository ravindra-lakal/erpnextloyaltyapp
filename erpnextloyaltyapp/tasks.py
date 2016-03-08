import frappe
import datetime
from frappe.utils import data

def all():
	customers=frappe.get_all("Customer",fields=["mobile_no","otp","date"],filters={"otp": ["!=", 'null']})
	print "customers", customers
	for customer in customers:
		date=customer.get('date')
		startdate=str(date)
		enddate=str(datetime.datetime.now())
		diff=data.time_diff_in_hours(enddate,startdate)
		print diff==0.0005 or diff>0.0005
		if diff==0.0005 or diff>0.0005:
			customer.otp=None
			customer.save()


