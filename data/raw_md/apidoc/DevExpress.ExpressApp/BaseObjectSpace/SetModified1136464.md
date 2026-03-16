---
uid: DevExpress.ExpressApp.BaseObjectSpace.SetModified(System.Object,DevExpress.ExpressApp.DC.IMemberInfo)
name: SetModified(Object, IMemberInfo)
type: Method
summary: Sets the state of the specified object to be Modified.
syntax:
  content: public void SetModified(object obj, IMemberInfo memberInfo)
  parameters:
  - id: obj
    type: System.Object
    description: A persistent object whose state is the subject to be Modified.
  - id: memberInfo
    type: DevExpress.ExpressApp.DC.IMemberInfo
    description: An [](xref:DevExpress.ExpressApp.DC.IMemberInfo) object providing metadata on the property whose value has been changed.
seealso: []
---
Generally, the changes made to persistent object properties are tracked, to then be committed (see [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges)). For the object changes that cannot be tracked internally, use the **SetModified** method. This method calls a protected virtual **SetModified** method, which must be implemented in the **BaseObjectSpace** class' descendants.

This **SetModified** method overload takes an additional _memberInfo_ parameter that allows you to specify the property that has been changed.