---
uid: DevExpress.ExpressApp.Frame.SetControllersActive(System.String,System.Boolean)
name: SetControllersActive(String, Boolean)
type: Method
summary: Activates or deactivates the current [](xref:DevExpress.ExpressApp.Frame)'s [Controllers](xref:112621) for a specified reason.
syntax:
  content: public void SetControllersActive(string reason, bool isActive)
  parameters:
  - id: reason
    type: System.String
    description: A string value that specifies a reason by which Controllers are activated or deactivated.
  - id: isActive
    type: System.Boolean
    description: '**true** if you need to activate Controllers; otherwise, **false**.'
seealso: []
---
Use this method to add a specified element to the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active) collection of each Controller from the [](xref:DevExpress.ExpressApp.Frame)'s [Frame.Controllers](xref:DevExpress.ExpressApp.Frame.Controllers) collection. This element, which represent a key/value pair, will be formed from values passed as the _reason_ and _isActive_ parameters. By calling this method, you can change a Controller's active state. A Controller is active, when none of the [Controller.Active](xref:DevExpress.ExpressApp.Controller.Active)collection elements have the **false** value. So, use this method in the following situations:

* Deactivate all Controllers. To do this, pass **false** as the _isActive_ parameter.
* Activate the Controllers that have been deactivated by a particular reason. To do this, pass **true** as the _isActive_ parameter and the required reason as the _reason_ parameter. The Controllers that have been deactivated by another reason will not be activated until you call this method and pass this reason.
*