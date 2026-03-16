---
uid: DevExpress.ExpressApp.DC.IMemberInfo.IsDelayed
name: IsDelayed
type: Property
summary: If the current member is a property, indicates whether it is marked as delayed.
syntax:
  content: bool IsDelayed { get; }
  parameters: []
  return:
    type: System.Boolean
    description: '**true**, if the property is marked as delayed; otherwise, **false**.'
seealso: []
---
When a property is marked as delayed, its value remains unassigned until it is accessed for the first time.