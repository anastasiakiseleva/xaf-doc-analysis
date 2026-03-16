---
uid: DevExpress.ExpressApp.Blazor.BlazorApplication
name: BlazorApplication
type: Class
summary: Manages an XAF Blazor UI application.
syntax:
  content: 'public class BlazorApplication : AspNetCoreApplication'
seealso:
- linkId: DevExpress.ExpressApp.Blazor.BlazorApplication._members
  altText: BlazorApplication Members
---
The `BlazorApplication` class is the platform-specific descendant of the [](xref:DevExpress.ExpressApp.XafApplication) class. In a Blazor UI [application project](xref:118045), this class is inherited (see the _MySolution.Blazor.Server/BlazorApplication.cs_ file). 


The descendant is instantiated in the `AddXaf` fabric (see _MySoution.Blazor.Server/Startup.cs_ file). 

Since the `BlazorApplication` object is often needed in code, it must be accessible. The following properties (cast to BlazorApplication) give you access to the current app: 
- [ActionBase.Application](xref:DevExpress.ExpressApp.Actions.ActionBase.Application), 
- [Controller.Application](xref:DevExpress.ExpressApp.Controller.Application), 
- [Frame.Application](xref:DevExpress.ExpressApp.Frame.Application), 
- [CustomizePopupWindowParamsEventArgs.Application](xref:DevExpress.ExpressApp.Actions.CustomizePopupWindowParamsEventArgs.Application), 
- [CreateCustomTemplateEventArgs.Application](xref:DevExpress.ExpressApp.CreateCustomTemplateEventArgs.Application), 
- [ModuleBase.Application](xref:DevExpress.ExpressApp.ModuleBase.Application)
- [](xref:DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem.Application), etc.
