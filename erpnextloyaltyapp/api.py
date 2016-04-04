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
def otp(customer):
    size=6
    chars=string.ascii_uppercase + string.digits + string.ascii_lowercase
    code=''.join(random.choice(chars) for _ in range(size))
    # frappe.errprint(docname)
    # docname.save()
    # frappe.db.set_value("Sales Order",docname,"otp",code)
    text="Your otp is %s"%code
    cust=frappe.get_doc("Customer",customer)
    number= mobile_no=frappe.db.get_value("Customer",{"mobile_no":cust.mobile_no},"mobile_no")
    a=[]
    a.append(number)
    send_sms(a,text)
    # docname=frappe.get_doc("Customer",customer)
    frappe.db.set_value("Customer",customer,"otp",code)
    frappe.db.set_value("Customer",customer,"date",datetime.datetime.now())

    # docname.save()
    return code

@frappe.whitelist(allow_guest=True)
def points(customer):
	cust=frappe.get_doc("Customer",customer)
	total=cust.total_points
	# print "Total is",total
	return total
# # for making api call only
# @frappe.whitelist()
# def so_return(so,return_date):
# 	sales_order=frappe.get_doc("Sales Order",so)
# 	sales_order.type="Return"
# 	sales_order.return_date=return_date
# 	sales_order.submit()

#For API only
@frappe.whitelist(allow_guest=True)
def add_customer(name,mobile_no,email_id,age,dob,gendor,edc_no,gc_no,payback_card_no,income,):
	cust=frappe.new_doc("Customer")
	cust.customer_name=name
	cust.mobile_no=mobile_no
	cust.email_id=email_id
	cust.flags.ignore_permissions=1
	cust.save()
	#if (name=None or customer_name=None or email_id=None):
	#frappe.throw(_("Mandetory field name mobile no. or email is missing"))

#For API Only
@frappe.whitelist(allow_guest=True)
def make_sales_order(so_details):
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
		pass

@frappe.whitelist(allow_guest=True)
def make_sales_return(so,return_date):
	sales_order=frappe.get_doc('Sales Order',so)
	sales_order.return_date=return_date
	sales_order.type="Return"
	sales_order.flags.ignore_permissions=1
	sales_order.submit()












