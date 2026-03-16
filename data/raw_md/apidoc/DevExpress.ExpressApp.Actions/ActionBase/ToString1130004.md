---
uid: DevExpress.ExpressApp.Actions.ActionBase.ToString
name: ToString()
type: Method
summary: Returns an [Action](xref:112622)'s textual representation.
syntax:
  content: public override string ToString()
  return:
    type: System.String
    description: A [](xref:System.String) value which is the current Action's textual representation.
seealso: []
---
The **ToString** method returns the human readable name of the current **Action**. This name is formed from the Action's [ActionBase.Id](xref:DevExpress.ExpressApp.Actions.ActionBase.Id) and [ActionBase.Controller](xref:DevExpress.ExpressApp.Actions.ActionBase.Controller). For instance, **RefreshAction** is represented by the "ID=\Refresh, Controller=\RefreshController" string representation.