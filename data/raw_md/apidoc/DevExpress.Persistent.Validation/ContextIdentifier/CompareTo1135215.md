---
uid: DevExpress.Persistent.Validation.ContextIdentifier.CompareTo(System.Object)
name: CompareTo(Object)
type: Method
summary: Compares the current [](xref:DevExpress.Persistent.Validation.ContextIdentifier) with another **ContextIdentifier**.
syntax:
  content: public int CompareTo(object obj)
  parameters:
  - id: obj
    type: System.Object
    description: An object which can be cast to the **ContextIdentifier** type, to compare to the current context identifier.
  return:
    type: System.Int32
    description: An integer value indicating whether the current instance precedes, follows, or occurs in the same position in the sort order as the other object.
seealso: []
---
This method returns a negative value if the current context identifier precedes the _obj_ context identifier in the sort order. If the current context identifier follows the _obj_ context identifier in the sort order, the method returns a positive value. If the context identifiers being compared occur in the same position in the sort order, zero is returned.