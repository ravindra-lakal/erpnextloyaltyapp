import frappe
import datetime
from frappe.utils import data

def all():
	""" Expires unused otp s after 24 hours"""
	# customers=frappe.get_all("Customer",fields=["mobile_no","otp","date"],filters={"otp": ["!=", 'null']})
	# customers=frappe.get_all("Customer",fields=["mobile_no","otp","date"])
	customers=frappe.get_all("Customer",fields=["otp","mobile_no","date","customer_id"])
	print "customers", customers
	for customer in customers:
		if customer.get("otp")!=None and customer.get("date")!=None:
			# print "customers", customer
			date=customer.get('date')
			startdate=str(date)
			enddate=str(datetime.datetime.now())
			customerid=customer.get('customer_id')
			# print "%s ======== %s" %(date,enddate)
			diff=data.time_diff_in_hours(enddate,startdate)
			# print diff==0.0005 or diff>0.0005
			if diff==24 or diff>24:
				frappe.db.set_value("Customer",customerid,"otp",None)
				# customer.otp=None
				# customer.save()
def hourly():

	""" Expires unused points of the customers s after specified time"""
	customers=frappe.get_all("Customer",fields=["customer_id"])
	for customer in customers:
		customer_id=customer.get("customer_id")
		doc=frappe.get_doc("Customer",customer_id)
		if doc.get("points_table")!=None:
			for raw in doc.get("points_table"):
				startdate=str(raw.purchase_date)
				enddate=str(datetime.datetime.now())
				 



	

