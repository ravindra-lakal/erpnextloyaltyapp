import frappe
def points_allocation(doc,method):
    a=frappe.get_all("Rule Engine", fields=["rule_type","minimum_amount","points ","points_multiplication_factor"], filters={"status":"Active","docstatus":1})
    # docstatus is 1 when document is submitted
    for i in a:
        if i.get('rule_type')=="Loyalty Points":
            print "in loyality points foor loop"
            minamount=int(i.get('minimum_amount'))
            pointsawarded=int(i.get('points'))
            factor=int(i.get('points_multiplication_factor'))
            amount=int(doc.total)
            points=(amount*pointsawarded)/minamount
            a=factor*points
            doc.amount=amount
            doc.points_earned=a
            doc.doc_no=doc.name
