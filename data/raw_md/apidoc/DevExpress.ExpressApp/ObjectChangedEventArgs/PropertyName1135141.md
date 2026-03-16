---
uid: DevExpress.ExpressApp.ObjectChangedEventArgs.PropertyName
name: PropertyName
type: Property
summary: Specifies the name of a property that had its value changed. Returns `null` if it is impossible to determine what property causes the change.
syntax:
  content: public string PropertyName { get; }
  parameters: []
  return:
    type: System.String
    description: A string containing the name of a property that had its value changed.
seealso: []
---
The returned value is `null` when the [IObjectSpace.SetModified](xref:DevExpress.ExpressApp.IObjectSpace.SetModified*) method is called and the _memberInfo_ parameter is not passed to it. For instance, it may occur when a new object is created and when a nested Object Space is committed.