---
uid: DevExpress.ExpressApp.ViewShowingEventArgs
name: ViewShowingEventArgs
type: Class
summary: Represents arguments passed to the [XafApplication.ViewShowing](xref:DevExpress.ExpressApp.XafApplication.ViewShowing) event.
syntax:
  content: 'public class ViewShowingEventArgs : EventArgs'
seealso:
- linkId: DevExpress.ExpressApp.ViewShowingEventArgs._members
  altText: ViewShowingEventArgs Members
---
The **ViewShowingEventArgs** class declares properties specific to the [XafApplication.ViewShowing](xref:DevExpress.ExpressApp.XafApplication.ViewShowing) event, which is designed to exchange data between the [Frame](xref:112608) that creates a [View](xref:112611) and the Frame where the View is displayed. This event is raised before showing the View. To access the source and target Frames, use the [ViewShowingEventArgs.SourceFrame](xref:DevExpress.ExpressApp.ViewShowingEventArgs.SourceFrame) and [ViewShowingEventArgs.TargetFrame](xref:DevExpress.ExpressApp.ViewShowingEventArgs.TargetFrame) properties. To access the View to be shown, use the [ViewShowingEventArgs.View](xref:DevExpress.ExpressApp.ViewShowingEventArgs.View) property.