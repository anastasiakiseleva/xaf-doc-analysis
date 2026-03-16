---
uid: DevExpress.Persistent.BaseImpl.BaseObject.AfterConstruction
name: AfterConstruction()
type: Method
summary: Invoked when the current object is about to be initialized after its creation.
syntax:
  content: public override void AfterConstruction()
seealso: []
---
The **BaseObject** class overrides this method to initialize the [BaseObject.Oid](xref:DevExpress.Persistent.BaseImpl.BaseObject.Oid) property, when the [BaseObject.OidInitializationMode](xref:DevExpress.Persistent.BaseImpl.BaseObject.OidInitializationMode) is set to [OidInitializationMode.AfterConstruction](xref:DevExpress.Persistent.BaseImpl.OidInitializationMode.AfterConstruction).

This method is not intended to be called from your code. However, when deriving from the **BaseObject** class, you may need to override this method to initialize new objects with default property values. For additional information, refer to the [How to: Initialize Business Objects with Default Property Values in XPO](xref:113258) help topic.