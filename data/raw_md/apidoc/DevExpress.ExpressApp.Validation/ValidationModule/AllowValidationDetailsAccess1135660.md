---
uid: DevExpress.ExpressApp.Validation.ValidationModule.AllowValidationDetailsAccess
name: AllowValidationDetailsAccess
type: Property
summary: Specifies whether end-users are allowed to view validation result details.
syntax:
  content: public bool AllowValidationDetailsAccess { get; set; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if end-users are allowed to view validation result details; otherwise, **false**.'
seealso:
- linkId: "113008"
---
When an object does not pass validation, a window listing failed validation rules is displayed. If the **AllowValidationDetailsAccess** property is set to **true**, end-users can click individual failed validation rules to view detailed information on them. Generally, this feature if only useful while debugging an application.