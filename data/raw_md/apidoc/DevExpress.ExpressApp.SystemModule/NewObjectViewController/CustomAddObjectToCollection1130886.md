---
uid: DevExpress.ExpressApp.SystemModule.NewObjectViewController.CustomAddObjectToCollection
name: CustomAddObjectToCollection
type: Event
summary: Occurs before adding a newly created object of the type selected in the [NewObjectViewController.NewObjectAction](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction)'s control to an associated collection.
syntax:
  content: public event EventHandler<ProcessNewObjectEventArgs> CustomAddObjectToCollection
seealso: []
---
By default, after an object of the specified type has been created, it is added to the View's collection source, if the View is a List View. If the current View is a Detail View opened from a List View, the newly created object is added to the List View's collection source. Handle this event if you need to customize the way the object is added. To cancel the default process of adding the object to the described collections, set the handler's **ProcessNewObjectEventArgs.Handled** parameter to **true**.

After this event has been raised, the Detail View is invoked to allow an end-user to customize the created object. However, the Detail View will not be shown if the [View.QueryCanChangeCurrentObject](xref:DevExpress.ExpressApp.View.QueryCanChangeCurrentObject) event handler's **ObjectCreatingEventArgs.ShowDetailView** parameter is set to **false**. By default, it is set to **false**.