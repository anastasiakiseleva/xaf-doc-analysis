---
uid: DevExpress.ExpressApp.Win.Core.Messaging.DefaultMessaging
name: DefaultMessaging
type: Property
summary: Specifies the default messaging.
syntax:
  content: public static Messaging DefaultMessaging { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Win.Core.Messaging
    description: The [](xref:DevExpress.ExpressApp.Win.Core.Messaging) object, which is the default messaging.
seealso: []
---
This property value is used by the [Messaging.GetMessaging](xref:DevExpress.ExpressApp.Win.Core.Messaging.GetMessaging(DevExpress.ExpressApp.XafApplication)) method when the [Application Model](xref:112580)'s [IModelOptionsWin.Messaging](xref:DevExpress.ExpressApp.Win.SystemModule.IModelOptionsWin.Messaging) property value is not specified.