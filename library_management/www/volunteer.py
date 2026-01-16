import frappe

def get_context(context):
    volunteers = frappe.get_all("Bodhya Volunteer", fields = ["name", "full_name", "email", "college_name", "picture", "banner_image", "volunteer_type", "bio", "company_name", "role"])

    for vol in volunteers : 
        vol.skills = frappe.get_all("Volunteer Skill",
                                        filters = {"parent": vol.name},
                                        fields=["skill", "level"])
        
        vol.socials = frappe.get_all("Volunteer Social Link",
                                     filters = {"parent" : vol.name},
                                     fields = ["icon", "url"])
        vol.full_name = vol.full_name.title()
        vol.college_name = vol.college_name.upper()
        vol.github = next((link['url'] for link in vol.socials if link['icon'] == "github"), None)
        vol.linkedin = next((link['url'] for link in vol.socials if link['icon'] == "linkedin"), None)

        vol.year = "3rd year"
    
    context.volunteers = volunteers