# Copyright (c) 2025, rayan aouf and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CTNBOX(Document):
	pass



@frappe.whitelist()
def get_transactions(ctn_box_name):
    return frappe.db.get_list(
        "CTN Box Transaction",
        filters={"ctn": ctn_box_name, "docstatus": 1},
        fields=["*"]  
    )
   