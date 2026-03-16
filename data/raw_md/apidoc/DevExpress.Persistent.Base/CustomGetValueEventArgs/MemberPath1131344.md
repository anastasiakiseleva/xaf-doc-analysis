---
uid: DevExpress.Persistent.Base.CustomGetValueEventArgs.MemberPath
name: MemberPath
type: Property
summary: Returns the name of the property that is being queried for its value.
syntax:
  content: public string MemberPath { get; }
  parameters: []
  return:
    type: System.String
    description: A name of the property that is being queried for its value.
seealso: []
---
When handling the [ObjectFormatter.CustomGetValue](xref:DevExpress.Persistent.Base.ObjectFormatter.CustomGetValue) event, use this property to determine the value that must be supplied to the [CustomGetValueEventArgs.Value](xref:DevExpress.Persistent.Base.CustomGetValueEventArgs.Value) property.