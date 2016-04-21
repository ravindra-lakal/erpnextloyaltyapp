from __future__ import unicode_literals
import frappe
from frappe.desk.reportview import get_match_cond
from frappe.model.db_query import DatabaseQuery
from frappe.utils import nowdate
import string
import random
from erpnext.setup.doctype.sms_settings.sms_settings import send_sms
import datetime
import json

# frappe.whitelist()
def customer_query(doctype, txt, searchfield, start, page_len, filters):
	cust_master_name = frappe.defaults.get_user_default("cust_master_name")

	if cust_master_name == "Customer Name":
		fields = ["name","mobile_no", "customer_group", "territory"]
	else:
		fields = ["name,""mobile_no", "customer_name", "customer_group", "territory"]

	fields = ", ".join(fields)

	return frappe.db.sql("""select {fields} from `tabCustomer`
		where docstatus < 2
			and (mobile_no like %(txt)s) and disabled=0
			{mcond}
		order by
			if(locate(%(_txt)s, name), locate(%(_txt)s, name), 99999),
			if(locate(%(_txt)s, customer_name), locate(%(_txt)s, customer_name), 99999),
			name, customer_name
		limit %(start)s, %(page_len)s""".format(**{
			"fields": fields,
			"key": searchfield,
			"mcond": get_match_cond(doctype)
		}), {
			'txt': "%%%s%%" % txt,
			'_txt': txt.replace("%", ""),
			'start': start,
			'page_len': page_len
		},debug=True)

@frappe.whitelist(allow_guest=True)
def otp(customerid):
    size=6
    chars=string.ascii_uppercase + string.digits + string.ascii_lowercase
    code=''.join(random.choice(chars) for _ in range(size))
    # frappe.errprint(docname)
    # docname.save()
    # frappe.db.set_value("Sales Order",docname,"otp",code)
    text="Your otp is %s"%code
    cust=frappe.get_doc("Customer",customerid)
    number= mobile_no=frappe.db.get_value("Customer",{"mobile_no":cust.mobile_no},"mobile_no")
    a=[]
    a.append(number)
    send_sms(a,text)
    # docname=frappe.get_doc("Customer",customer)
    frappe.db.set_value("Customer",customerid,"otp",code)
    frappe.db.set_value("Customer",customerid,"date",datetime.datetime.now())

    # docname.save()
    return code

@frappe.whitelist(allow_guest=True)
def profile_fetch(customerid):
	try:
		cust=frappe.get_doc("Customer",customerid)
		customer_details={}
		customer_details.update({"name":cust.customer_name,
		"mobile_no":cust.mobile_no,
		"email_id":cust.email_id,
		"age":cust.age,
		"dob":cust.dob,
		"gendor":cust.gendor,
		"edc_no":cust.edc_no,
		"gv_no":cust.gv_no,
		"payback_card_no":cust.payback_card_no,
		"income":cust.income,
		"points":cust.total_points
		})
		return customer_details
	except Exception, e:
		return e 

# # for making api call only
# @frappe.whitelist()
# def so_return(so,return_date):
# 	sales_order=frappe.get_doc("Sales Order",so)
# 	sales_order.type="Return"
# 	sales_order.return_date=return_date
# 	sales_order.submit()

#For API only
@frappe.whitelist(allow_guest=True)
def add_customer(name,mobile_no,email_id,age=None,dob=None,gendor=None,edc_no=None,gc_no=None,payback_card_no=None,income=None,):
	
		cust=frappe.new_doc("Customer")
		cust.customer_name=name
		cust.mobile_no=mobile_no
		cust.email_id=email_id
		cust.flags.ignore_permissions=1
		cust.save()
		if (name==None or customer_name==None or email_id==None):
			frappe.throw(_("Mandetory field name mobile no. or email is missing"))

#For API Only
# @frappe.whitelist(allow_guest=True)
# def make_sales_order(so_details):
	#return so_details
	# so=frappe.new_doc("Sales Order")
	# so_details=json.loads(so_details)
	# so.customer_mobile_no=so_details.get("customer_mobile_no")
	# so.transaction_date=so_details.get("transaction_date")
	# so.delivery_date=so_details.get("delivery_date")
	# itm=so.append('items',{})
	# for item in so_details.get('items'):
	# 	itm.qty=item.get('qty')
	# 	itm.item_name=item.get('item_name')
	# 	itm.amount=item.get('amount')
	# 	itm.net_rate=item.get('net_rate')
	# 	itm.stock_uom=item.get('stock_uom')
	# 	itm.item_code=item.get('item_code')
	# meth=so.append('payment_method',{})
	# for pm in so_details.get('payment_method'):
	# 	meth.method=pm.get('method')
	# 	meth.amount=pm.get('amount')
	# 	meth.card_no=pm.get('card_no')
	# 	meth.otp=pm.get('otp')
	# 	so.flags.ignore_permissions=1
	# 	so.docstatus=so_details.get('docstatus')
		# so.save()
		# pass

@frappe.whitelist(allow_guest=True)
def make_sales_return(so,return_date):
	sales_order=frappe.get_doc('Sales Order',so)
	sales_order.return_date=return_date
	sales_order.type="Return"
	sales_order.flags.ignore_permissions=1
	sales_order.submit()

@frappe.whitelist(allow_guest=True)
def make_sales_order(customer_mobile_no,transaction_date,delivery_date,items,payment_method):
	try:
		
		so=frappe.new_doc("Sales Order")
		cust=frappe.get_doc("Customer",customer_mobile_no)
		so.customer_mobile_no=customer_mobile_no
		so.transaction_date=transaction_date
		so.delivery_date=delivery_date
		items=json.loads(items)
		it=so.append('items',{})
		for item in items:
			it.item_code=item.get('item_code')
			it.qty=item.get('qty')
			it.item_name=item.get('item_name')
		method=so.append('payment_method',{})
		payment_method=json.loads(payment_method)
		for meth in payment_method:
			method.method=meth.get('method')
			method.amount=meth.get('amount')
			method.points=meth.get('points')
			method.card_no=meth.get('card_no')
			method.otp=meth.get('otp')
		cust.flags.ignore_permissions=1
		# so.flags.ignore_permissions=1

		cust.save()
		# so.flags.ignore_permissions=True
		so.flags.ignore_permissions=1
		so.save()
		so.submit()
		frappe.db.commit()
	except Exception:
		pass
		# sys.exc_clear()
    



	# so.save(ignore_permissions=1)


	
	











