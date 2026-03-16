---
uid: DevExpress.ExpressApp.Win.WinApplication
name: WinApplication
type: Class
summary: Manages a WinForms XAF application.
syntax:
  content: 'public class WinApplication : XafApplication, ISupportSplashScreen, ISupportRunSetupInNewThread'
seealso:
- linkId: DevExpress.ExpressApp.Win.WinApplication._members
  altText: WinApplication Members
- linkId: "113115"
- linkId: "113119"
---
The **WinApplication** class is the platform-specific descendant of the [](xref:DevExpress.ExpressApp.XafApplication) class. In the WinForms [application project](xref:118045), this class is inherited (see _WinApplication.cs_ or _WinApplication.vb_ file). The descendant is instantiated in the **Program.Main** method (see _Program.cs_ or _Program.vb_ file). You can access the class' members to perform customizations before the [XafApplication.Setup](xref:DevExpress.ExpressApp.XafApplication.Setup*) and [WinApplication.Start](xref:DevExpress.ExpressApp.Win.WinApplication.Start) methods are invoked.

Since the **WinApplication** object can be useful at many points in your code, it must be easily accessed. The following properties, cast to the **WinApplication** type, provide access to the current WinForms application: [ActionBase.Application](xref:DevExpress.ExpressApp.Actions.ActionBase.Application), [Controller.Application](xref:DevExpress.ExpressApp.Controller.Application), [Frame.Application](xref:DevExpress.ExpressApp.Frame.Application), [CustomizePopupWindowParamsEventArgs.Application](xref:DevExpress.ExpressApp.Actions.CustomizePopupWindowParamsEventArgs.Application), [CreateCustomTemplateEventArgs.Application](xref:DevExpress.ExpressApp.CreateCustomTemplateEventArgs.Application), [ModuleBase.Application](xref:DevExpress.ExpressApp.ModuleBase.Application), etc.