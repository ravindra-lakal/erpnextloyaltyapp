import frappe
from frappe import _
def points_allocation(doc,method):
    """  Allocates the points to the user before submission of the document based on the rule engine"""
    points_check(doc)

    a=frappe.get_all("Rule Engine", fields=["rule_type","minimum_amount","points ","points_multiplication_factor","converted_rupees"], filters={"status":"Active","docstatus":1})
    # docstatus is 1 when document is submitted
    for i in a:
        if i.get('rule_type')=="Loyalty Points":
            # print "in loyality points foor loop"
            minamount=int(i.get('minimum_amount'))
            pointsawarded=int(i.get('points'))
            factor=int(i.get('points_multiplication_factor'))
            # wrong amount calculation
            # amount=int(doc.total)
            amount=redeem_amount(doc)
            points=int((amount*pointsawarded))/int(minamount)
            a=factor*points
            doc.points_earned=a
            doc.amount=amount
            # order stops if payment is incomplete
            # if payment_check(doc)!=0:
            #     doc.points_earned=a
            # else:
            #     frappe.throw(_("Payment incomplete please complete the payment"))
            #     doc.points_earned=0
            # doc.doc_no=doc.name
            # rupees=int(i.get('converted_rupees'))

def check_method(doc):

    # """ checks the payment method if finds points then it returns them or returns 0 used while insertng data in points child table"""
    l1=[]
    for raw in doc.get("payment_method"):
        if raw.points!=None:
            return raw.points
        else:
            return 0

def on_submit(doc,method):
# """ the points allocated to the perticular user are inserted into the points child table with total points earned,consumed remaining points and status also sets otp to none after completion of SO"""
    required_points=0
    now=0
    customer=frappe.get_doc("Customer",doc.customer_mobile_no)
     #customer.set('Points Details',[])
    n1 = customer.append('points_table', {})
    n1.purchase_date=doc.transaction_date
    n1.points_earned=doc.points_earned
    n1.remaining_points=doc.points_earned
    n1.status="Active"

    if check_method(doc)==0:
        n1.points_consumed=0
    else:
        new_points=n1.points_consumed=check_method(doc)
        require_points_check(customer,new_points)
    customer.otp=None
    # print "OTP is",customer.otp
    # print customer.points_table[0].status
    customer.save()

def points_check(doc):
    # """ checks if the customer has desired number of points in his account if not throws an exception"""
		customer=frappe.get_doc("Customer",doc.customer_mobile_no)
		tpoint=customer.total_points
		for raw in doc.get("payment_method"):
			if raw.method=="Points":
				if int(raw.points) > int(tpoint):


					frappe.throw(_("Customer doesn't have enough points for redumption."))

def on_update(doc,method):
    # """ Checks if the user has entered correct otp and points at the time of redumption"""
    if doc.get("payment_method"):
        for raw in doc.get("payment_method"):
            if raw.method=="Points":
                if raw.otp==None and raw.points==None:
                    frappe.throw(_("You have not entered otp and points "))
                if raw.otp==None:
                    frappe.throw(_("You have not entered otp"))
                if raw.points==None:
                    frappe.throw(_("You have not entered points "))
                # if raw.otp!=doc.otp:
                #         frappe.throw(_("Please enter correct otp "))
                cust=frappe.get_doc("Customer",doc.customer_mobile_no)
                if raw.otp!=cust.otp:
                    frappe.throw(_("Please enter correct otp "))
def payment_check(doc):
    # """ Checks if the payment is complete"""
    total=0
    print ("Grand total is",doc.grand_total)
    for raw in doc.get("payment_method"):
        if raw.method=="COD" or raw.method=="CC":
            total+=float(raw.amount)
        else:
            total+=float(raw.points)
    if total< doc.grand_total:
        return 0


def redeem_amount(doc):
    # """Returns redeem amount i.e amount payed by COD and CC"""
    total=0
    for raw in doc.get("payment_method"):
        if raw.method=="COD" or raw.method=="CC":
            total+=float(raw.amount)
        return total
        if raw.method=="Points":
            return 0
def require_points_check(customer,n):
    remaining=n
    for raw in customer.get("points_table"):
        if raw.status=="Active" or raw.status=="Partially Consumed":
            if int(remaining)< int(raw.remaining_points):
                # print " n is ",remaining
                raw.remaining_points=int(raw.remaining_points)-int(remaining)
                raw.status="Partially Consumed"
                remaining=0
            if int(remaining)==int(raw.remaining_points):
                raw.status="Consumed"
                raw.remaining_points=0
                remaining=0
            if int(remaining)>int(raw.remaining_points):
                raw.status="Consumed"
                # print " n is ",remaining
                # print "status is",raw.status
                remaining=int(remaining)-int(raw.remaining_points)
                # print " n is ",remaining
                raw.remaining_points=0
                # below code is just included to show the status flags correctly the application runs smoothly without this also
                if raw.points_earned==0:
                    raw.status=="None"
                if remaining==0:
                    break