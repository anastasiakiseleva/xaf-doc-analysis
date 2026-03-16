---
uid: DevExpress.ExpressApp.Win.Core.Messaging.GetMessaging(DevExpress.ExpressApp.XafApplication)
name: GetMessaging(XafApplication)
type: Method
summary: Returns a new [](xref:DevExpress.ExpressApp.Win.Core.Messaging) instance for a specific [](xref:DevExpress.ExpressApp.XafApplication).
syntax:
  content: public static Messaging GetMessaging(XafApplication application)
  parameters:
  - id: application
    type: DevExpress.ExpressApp.XafApplication
    description: An [](xref:DevExpress.ExpressApp.XafApplication) object for which the **Messaging** is created.
  return:
    type: DevExpress.ExpressApp.Win.Core.Messaging
    description: A [](xref:DevExpress.ExpressApp.Win.Core.Messaging) object.
seealso: []
---
The [Application Model](xref:112580)'s [IModelOptionsWin.Messaging](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.Messaging) property value is considered when instantiating a Messaging object. If this property value is not specified, the [Messaging.DefaultMessaging](xref:DevExpress.ExpressApp.Win.Core.Messaging.DefaultMessaging) value is returned.