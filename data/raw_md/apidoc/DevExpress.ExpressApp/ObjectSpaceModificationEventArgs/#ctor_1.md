---
uid: DevExpress.ExpressApp.ObjectSpaceModificationEventArgs.#ctor(System.Boolean,System.Object,DevExpress.ExpressApp.DC.IMemberInfo,System.Object,System.Object)
name: ObjectSpaceModificationEventArgs(Boolean, Object, IMemberInfo, Object, Object)
type: Constructor
summary: Initializes a new instance of the @DevExpress.ExpressApp.ObjectSpaceModificationEventArgs class with specified settings.
syntax:
  content: public ObjectSpaceModificationEventArgs(bool cancel, object obj, IMemberInfo memberInfo, object oldValue, object newValue)
  parameters:
  - id: cancel
    type: System.Boolean
    description: '**true** if the @DevExpress.ExpressApp.BaseObjectSpace.IsModified property change should be canceled; otherwise, **false**.'
  - id: obj
    type: System.Object
    description: The object whose property value was changed.
  - id: memberInfo
    type: DevExpress.ExpressApp.DC.IMemberInfo
    description: An [](xref:DevExpress.ExpressApp.DC.IMemberInfo) object that stores information on the property whose value was changed.
  - id: oldValue
    type: System.Object
    description: The old value of a changed property.
  - id: newValue
    type: System.Object
    description: The new value of a changed property.
seealso: []
---
