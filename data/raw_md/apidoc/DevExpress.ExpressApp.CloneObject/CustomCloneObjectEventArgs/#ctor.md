---
uid: DevExpress.ExpressApp.CloneObject.CustomCloneObjectEventArgs.#ctor(System.Object,System.Type,DevExpress.ExpressApp.XafApplication,DevExpress.ExpressApp.Frame,DevExpress.ExpressApp.View)
name: CustomCloneObjectEventArgs(Object, Type, XafApplication, Frame, View)
type: Constructor
summary: Initializes a new instance of the @DevExpress.ExpressApp.CloneObject.CustomCloneObjectEventArgs class with specified settings.
syntax:
  content: public CustomCloneObjectEventArgs(object sourceObject, Type targetType, XafApplication application, Frame frame, View view)
  parameters:
  - id: sourceObject
    type: System.Object
    description: The source object to be cloned.
  - id: targetType
    type: System.Type
    description: The type of the target object.
  - id: application
    type: DevExpress.ExpressApp.XafApplication
    description: An [](xref:DevExpress.ExpressApp.XafApplication) object that is the current application.
  - id: frame
    type: DevExpress.ExpressApp.Frame
    description: A [](xref:DevExpress.ExpressApp.Frame) that displays an object to be cloned.
  - id: view
    type: DevExpress.ExpressApp.View
    description: A [](xref:DevExpress.ExpressApp.View) that displays an object to be cloned.
seealso: []
---
XAF automatically creates instances of the [](xref:DevExpress.ExpressApp.CloneObject.CustomCloneObjectEventArgs) class and passes them to handlers of the [CloneObjectViewController.CustomCloneObject](xref:DevExpress.ExpressApp.CloneObject.CloneObjectViewController.CustomCloneObject) event.

You do not need to call this constructor from your applications.