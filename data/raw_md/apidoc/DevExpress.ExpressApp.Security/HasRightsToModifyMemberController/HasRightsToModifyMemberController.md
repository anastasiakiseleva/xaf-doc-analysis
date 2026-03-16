---
uid: DevExpress.ExpressApp.Security.HasRightsToModifyMemberController
name: HasRightsToModifyMemberController
type: Class
summary: A [](xref:DevExpress.ExpressApp.ViewController) descendant that makes Property Editors read-only or editable, dependent on the current user's permissions.
syntax:
  content: 'public class HasRightsToModifyMemberController : ObjectViewController'
seealso:
- linkId: DevExpress.ExpressApp.Security.HasRightsToModifyMemberController._members
  altText: HasRightsToModifyMemberController Members
- linkId: "113366"
---
The **HasRightsToModifyMemberController** [Controller](xref:112621) is provided by the [SecuritySystem](xref:113366) module. It is activated for Detail [Views](xref:112611). This Controller makes Property Editors read-only when the current user has no permission to modify the object displayed in the current Detail View. When a Property Editor represents a reference property, the Controller sets this editor as read-only, if the user has no permission to modify the referenced object.

By default, Property Editors states  ([PropertyEditor.AllowEdit](xref:DevExpress.ExpressApp.Editors.PropertyEditor.AllowEdit) properties) are updated when:

* the **HasRightsToModifyMemberController** Controller is activated;
* the object displayed in a current Detail View is changed (see [View.CurrentObjectChanged](xref:DevExpress.ExpressApp.View.CurrentObjectChanged));
* an item is added to, or removed from the current Detail View.

If it is required to enforce the update, invoke the [HasRightsToModifyMemberController.UpdatePropertyEditors](xref:DevExpress.ExpressApp.Security.HasRightsToModifyMemberController.UpdatePropertyEditors) method exposed by the **HasRightsToModifyMemberController** class.