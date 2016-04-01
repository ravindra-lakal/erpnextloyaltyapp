from __future__ import unicode_literals
import frappe
from frappe.desk.reportview import get_match_cond
from frappe.model.db_query import DatabaseQuery
from frappe.utils import nowdate
import string
import random
from erpnext.setup.doctype.sms_settings.sms_settings import send_sms
import datetime

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
@frappe.whitelist(allow_guest=True)
def add_customer(name,mobile_no,email_id):

	cust=frappe.new_doc("Customer")
	cust.customer_name=name


	# cust.email_id=email_id
	# if (name=None or customer_name=None or email_id=None):
	# 	frappe.throw(_("Mandetory field name mobile no. or email is missing"))
	# cust.insert()
	cust.insert(ignore_permissions=True)


