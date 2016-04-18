import frappe
from frappe.model.naming import make_autoname
import datetime 
from frappe import _
def autoname(doc,method):
    """ sets the naming series for customer"""
    doc.naming_series="CUST-"
    doc.name = make_autoname(doc.naming_series+'.#####')
    doc.customer_id=doc.name
def before_insert(doc,method):
    mobile_no=frappe.db.get_value("Customer",{"mobile_no":doc.mobile_no},"mobile_no")
    email_id=frappe.db.get_value("Customer",{"email_id":doc.email_id},"email_id")
    customer_id=frappe.db.get_value("Customer",{"mobile_no":doc.mobile_no},"customer_id")
    if email_id==doc.email_id and mobile_no==doc.mobile_no and customer_id!=doc.customer_id:
        frappe.throw(_("Mobile Number and Email ID already used please enter diffrent one"))
    if mobile_no==doc.mobile_no and customer_id!=doc.customer_id:
        frappe.throw(_("Username already used please enter diffrent one"))
    #counts total points on each update
    if email_id==doc.email_id and customer_id!=doc.customer_id:
        frappe.throw(_("Email ID already used please enter diffrent one"))

    
def validate(doc,method):
    

    """checks if the mobile number is unique if email and mobile number are same then it allows to save the customer """
    doc.date=datetime.datetime.now()
    
    points_earned=0
    points_consumed=0
    total_points=0
    remaining_points=0
    if  doc.get("points_table"):
        for raw in doc.get("points_table"):
            # if raw.points_earned:
            if raw.status=="Active" or raw.status=="Partially Consumed":
                remaining_points += raw.remaining_points 
                # points_earned+=int(raw.points_earned)


            # else:
            #     raw.points_earned=0
            # points_consumed+=int(raw.points_consumed)
        # doc.total_points=points_earned - points_consumed
        #self.pos_customer_id=self.name
        doc.total_points=remaining_points

