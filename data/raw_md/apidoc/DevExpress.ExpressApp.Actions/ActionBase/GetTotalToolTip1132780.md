---
uid: DevExpress.ExpressApp.Actions.ActionBase.GetTotalToolTip(System.String)
name: GetTotalToolTip(String)
type: Method
summary: Returns the [Action](xref:112622)'s total tooltip. Intended for internal use.
syntax:
  content: public virtual string GetTotalToolTip(string itemCaption)
  parameters:
  - id: itemCaption
    type: System.String
    description: A string holding an additional message to be included in the total tooltip.
  return:
    type: System.String
    description: A string holding the Action's total tooltip.
seealso:
- linkId: DevExpress.ExpressApp.Actions.ActionBase.ToolTip
---
The total tooltip comprises the caption specified by the [ActionBase.ToolTip](xref:DevExpress.ExpressApp.Actions.ActionBase.ToolTip) property and additional messages supplied by **XAF**. For instance, if the **ToolTip** property value is "New tool tip" and the Action requires selected objects, the total tooltip value can be "New tool tip\r\nSelected object required".