from frappe.model.naming import make_autoname
def autoname(doc,method):
    doc.naming_series="CUST-"
    doc.name = make_autoname(doc.naming_series+'.#####')
    doc.customer_id=doc.name
def validate(doc,method):
    #checks if the mobile number is unique if email and mobile number are same then it allows to save the customer
    # username=frappe.db.get_value("Customer",{"username":self.username},"username")
    # email_address=frappe.db.get_value("Customer",{"username":self.username},"email_address")
    # if username==self.username and email_address!=self.email_address:
    #     frappe.throw(_("Username already used please enter diffrent one"))
    #counts total points on each update
    points_earned=0
    points_consumed=0
    total_points=0
    if  doc.get("points_table"):
        for raw in doc.get("points_table"):
            if raw.points_earned:
                points_earned+=int(raw.points_earned)
            else:
                raw.points_earned=0
            points_consumed+=int(raw.points_consumed)
        doc.total_points=points_earned - points_consumed
        #self.pos_customer_id=self.name
