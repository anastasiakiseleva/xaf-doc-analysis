---
uid: DevExpress.ExpressApp.SystemModule.NewObjectViewController.ObjectCreated
name: ObjectCreated
type: Event
summary: Occurs after the object of the type selected in the [NewObjectViewController.NewObjectAction](xref:DevExpress.ExpressApp.SystemModule.NewObjectViewController.NewObjectAction)'s **Items** collection has been created and added to the associated object collection.
syntax:
  content: public event EventHandler<ObjectCreatedEventArgs> ObjectCreated
seealso:
- linkId: DevExpress.ExpressApp.SystemModule.NewObjectViewController.ObjectCreating
- linkId: DevExpress.ExpressApp.SystemModule.NewObjectViewController.CustomAddObjectToCollection
---
After this event has been raised, the Detail View is invoked to allow an end-user to customize the created object. Handle this event to access the created object. For this purpose, use the handler's **ObjectCreatedEventArgs.CreatedObject** parameter. The Detail View will not be shown if the [View.QueryCanChangeCurrentObject](xref:DevExpress.ExpressApp.View.QueryCanChangeCurrentObject) event handler's **ObjectCreatedEventArgs.ShowDetailView** parameter is set to **false**.

See an example of using this event in the [How to: Initialize an Object Created Using the New Action](xref:112912) topic.