---
uid: DevExpress.ExpressApp.XafApplication.SettingUp
name: SettingUp
type: Event
summary: Occurs before initializing the [](xref:DevExpress.ExpressApp.XafApplication) class instance.
syntax:
  content: public event EventHandler<SetupEventArgs> SettingUp
seealso: []
---
This event is raised as a result of calling the [XafApplication.Setup](xref:DevExpress.ExpressApp.XafApplication.Setup*) method. Handle this event to set custom settings for the [](xref:DevExpress.ExpressApp.XafApplication) class instance. To do this, use the handler's `SetupEventArgs.SetupParameters` parameter. It provides access to the following: [Controllers](xref:112621) Manager, module list, connection string, [XafApplication.ApplicationName](xref:DevExpress.ExpressApp.XafApplication.ApplicationName), and [XafApplication.ObjectSpaceProvider](xref:DevExpress.ExpressApp.XafApplication.ObjectSpaceProvider).

The [](xref:DevExpress.ExpressApp.Win.WinApplication) class instance is used in the Windows Forms application project. This class inherits from the [](xref:DevExpress.ExpressApp.XafApplication) class.