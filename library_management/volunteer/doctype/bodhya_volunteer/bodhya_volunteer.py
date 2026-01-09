# Copyright (c) 2025, satyma and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class BodhyaVolunteer(Document):
	pass
class BodhyaVolunteer(Document):
	pass

# 👇 Ye code file ke end mein paste karo (Class ke bahar)
@frappe.whitelist(allow_guest=True)
def get_volunteer_data():
    try:
        # 1. Basic Details fetch karo
        volunteers = frappe.get_all("Bodhya Volunteer", 
            fields=["name", "full_name", "image", "i_am_student", "college_name", "course", "company_name", "role", "bio", "github_link", "linkedin_link"]
        )

        # 2. Skills (Child Table) fetch karo
        for vol in volunteers:
            # Full document load karke skills nikal rahe hain (Safety ke liye)
            doc = frappe.get_doc("Bodhya Volunteer", vol.name)
            
            skill_list = []
            
            # Check kar rahe hain ki skills table exist karta hai ya nahi
            if hasattr(doc, 'skills') and doc.skills:
                # Sirf bhare huye skills utha rahe hain
                skill_list = [row.skill for row in doc.skills if row.skill]
            
            # List ko wapas volunteer object mein daal diya
            vol['skills_list'] = skill_list

        return volunteers

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Bodhya Volunteer Error")
        return []