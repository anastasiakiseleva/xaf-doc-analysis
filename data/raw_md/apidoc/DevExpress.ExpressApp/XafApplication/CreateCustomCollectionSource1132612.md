---
uid: DevExpress.ExpressApp.XafApplication.CreateCustomCollectionSource
name: CreateCustomCollectionSource
type: Event
summary: Occurs when creating a Collection Source for a List View.
syntax:
  content: public event EventHandler<CreateCustomCollectionSourceEventArgs> CreateCustomCollectionSource
seealso:
- linkId: DevExpress.ExpressApp.XafApplication.CreateCustomPropertyCollectionSource
---
This event is raised as a result of calling the [XafApplication.CreateCollectionSource](xref:DevExpress.ExpressApp.XafApplication.CreateCollectionSource*) method. Handle this event to create a descendant of the [](xref:DevExpress.ExpressApp.CollectionSourceBase) class, if you need to create a custom behavior of a List View's Collection Source. Assign the custom Collection Source to the handler's **CollectionSource** property.

To create a custom Collection Source for a nested List View, handle the [XafApplication.CreateCustomPropertyCollectionSource](xref:DevExpress.ExpressApp.XafApplication.CreateCustomPropertyCollectionSource) event.