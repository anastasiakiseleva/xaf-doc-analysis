---
uid: DevExpress.ExpressApp.XafApplication.ViewShown
name: ViewShown
type: Event
summary: Occurs after a [View](xref:112611) is shown.
syntax:
  content: public event EventHandler<ViewShownEventArgs> ViewShown
seealso: []
---
In many scenarios, a View is not shown in the [Frames](xref:112608), in which the command to show this View has been performed, but in a separate Frames. Let these Frames be called a source Frame and a target Frame. When implementing custom features, you may need to pass some values from the source Frame to the target Frame. For instance, the **RecordsNavigationController**'s **PreviousObject** and **NextObject** [Actions](xref:112622) displayed in a Detail View allows navigating to the previous and next record in the List View from which this Detail View has been shown. Here, the target Frame (the Frame with the Detail View) obtains information on the order of objects in the source Frame (the Frame with the List View).

To implement such feature where you need to exchange data between the source and target Frames, handle the [XafApplication.ViewShowing](xref:DevExpress.ExpressApp.XafApplication.ViewShowing) and **ViewShown** events. The former event is raised before showing a View in the target Frame, the latter - after showing this View. To access the source and target Frames, use the handler's parameters. In addition, the [XafApplication.ViewShowing](xref:DevExpress.ExpressApp.XafApplication.ViewShowing) event handler provides the [ViewShowingEventArgs.View](xref:DevExpress.ExpressApp.ViewShowingEventArgs.View) parameter.