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
				startdate=data.getdate(raw.purchase_date)
				enddate=data.getdate(datetime.datetime.now())
				print data.date_diff(enddate,startdate)
				rule_engine=frappe.get_all("Rule Engine",fields=['rule_type','points_expiry_duration'], filters={"status":"Active","docstatus":1})
				for rule in rule_engine:
					if rule.get('points_expiry_duration')=="1 Year":
					    if data.date_diff(enddate,startdate)==365 or data.date_diff(enddate,startdate)>365:
							raw.status="Expired"
							print raw.status
							doc.save()
					if rule.get('points_expiry_duration')=="3 Months":
						if data.date_diff(enddate,startdate)==90 or data.date_diff(enddate,startdate)>90:
							raw.status="Expired"
							print raw.status
							doc.save()
					if rule.get('points_expiry_duration')=="6 Months":
						if data.date_diff(enddate,startdate)==180 or data.date_diff(enddate,startdate)>180:
							raw.status="Expired"
							print raw.status
							doc.save()