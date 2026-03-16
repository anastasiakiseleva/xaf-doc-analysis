---
uid: DevExpress.ExpressApp.Security.HasRightsToModifyMemberController.UpdatePropertyEditors
name: UpdatePropertyEditors()
type: Method
summary: Makes the Property Editors' states read-only or editable, dependent on the current user's permissions.
syntax:
  content: public void UpdatePropertyEditors()
seealso: []
---
The **UpdatePropertyEditors** method iterates through all the Property Editors available in the current Detail View. The method makes them read-only when the current user has no permission to modify the displayed property.