---
uid: DevExpress.ExpressApp.View.CanChangeCurrentObject
name: CanChangeCurrentObject()
type: Method
summary: Determines whether a [View](xref:112611)'s current object can be changed.
syntax:
  content: public bool CanChangeCurrentObject()
  return:
    type: System.Boolean
    description: '**true** if the current object can be changed; otherwise, **false**.'
seealso: []
---
This method raises the [View.QueryCanChangeCurrentObject](xref:DevExpress.ExpressApp.View.QueryCanChangeCurrentObject) event and returns the value opposite to the event handler's **Cancel** parameter value.

Handle the **QueryCanChangeCurrentObject** event to prohibit changing the current object by setting the event handler's **Cancel** parameter to **true**. By default, this parameter is set to **false**.