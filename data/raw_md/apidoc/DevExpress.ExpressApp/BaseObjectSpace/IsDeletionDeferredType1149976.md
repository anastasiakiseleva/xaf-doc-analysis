---
uid: DevExpress.ExpressApp.BaseObjectSpace.IsDeletionDeferredType(System.Type)
name: IsDeletionDeferredType(Type)
type: Method
summary: Returns a value that indicates if the deferred deletion is enabled for persistent objects of a given type.
syntax:
  content: public virtual bool IsDeletionDeferredType(Type objectType)
  parameters:
  - id: objectType
    type: System.Type
    description: A [](xref:System.Type) object that is a type of persistent object.
  return:
    type: System.Boolean
    description: '**true**, if the deferred deletion is enabled; otherwise - **fale**.'
seealso: []
---
In [](xref:DevExpress.ExpressApp.BaseObjectSpace), this method always returns false, but this behavior is overridden in descendant [](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace) class (see [XPObjectSpace.IsDeletionDeferredType](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.IsDeletionDeferredType(System.Type))).