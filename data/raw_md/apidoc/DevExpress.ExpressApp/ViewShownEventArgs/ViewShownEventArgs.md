---
uid: DevExpress.ExpressApp.ViewShownEventArgs
name: ViewShownEventArgs
type: Class
summary: Represents arguments passed to an application's [XafApplication.ViewShown](xref:DevExpress.ExpressApp.XafApplication.ViewShown) event.
syntax:
  content: 'public class ViewShownEventArgs : EventArgs'
seealso:
- linkId: DevExpress.ExpressApp.ViewShownEventArgs._members
  altText: ViewShownEventArgs Members
---
The [](xref:DevExpress.ExpressApp.ViewShownEventArgs) class declares properties specific to the [XafApplication.ViewShown](xref:DevExpress.ExpressApp.XafApplication.ViewShown) event designed to exchange data between the Frame that created a View and the Frames that showed the View. This event is raised after the View is shown. To access the Frames, use the [ViewShownEventArgs.SourceFrame](xref:DevExpress.ExpressApp.ViewShownEventArgs.SourceFrame) and [ViewShownEventArgs.TargetFrame](xref:DevExpress.ExpressApp.ViewShownEventArgs.TargetFrame) properties.