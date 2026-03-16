---
uid: DevExpress.ExpressApp.XafApplication.SetupComplete
name: SetupComplete
type: Event
summary: Occurs after the [](xref:DevExpress.ExpressApp.XafApplication) class instance has been initialized.
syntax:
  content: public event EventHandler<EventArgs> SetupComplete
seealso:
- linkId: DevExpress.ExpressApp.XafApplication.SettingUp
---
Handle this event to customize settings of the [](xref:DevExpress.ExpressApp.XafApplication) class instance after it has been initialized via the [XafApplication.Setup](xref:DevExpress.ExpressApp.XafApplication.Setup*) method.

The [](xref:DevExpress.ExpressApp.Win.WinApplication) class instance is used in the Windows Forms application project. This class inherits from the [](xref:DevExpress.ExpressApp.XafApplication) class.

> [!NOTE]
> When the `SetupComplete` event is triggered, the [Application Model](xref:112580)'s end-user customizations layer is not yet created from the _Model.User.xafml_ file. So, if you need to access the Application Model in its final state, including customizations that a user might have created, handle the [XafApplication.LoggedOn](xref:DevExpress.ExpressApp.XafApplication.LoggedOn) event instead.