---
uid: DevExpress.ExpressApp.XafApplication.CreateCustomPropertyCollectionSource
name: CreateCustomPropertyCollectionSource
type: Event
summary: Occurs when creating a Collection Source for a nested List View that displays a collection property.
syntax:
  content: public event EventHandler<CreateCustomPropertyCollectionSourceEventArgs> CreateCustomPropertyCollectionSource
seealso:
- linkId: DevExpress.ExpressApp.XafApplication.CreateCollectionSource*
---
This event is raised as a result of calling the [XafApplication.CreatePropertyCollectionSource](xref:DevExpress.ExpressApp.XafApplication.CreatePropertyCollectionSource*) method. Handle this event to create a descendant of the [](xref:DevExpress.ExpressApp.PropertyCollectionSource) class, if you need to create a custom behavior of a List View's Collection Source. Assign the custom Collection Source to the handler's **PropertyCollectionSource** property.

To create a custom Collection Source for a root List View, handle the [XafApplication.CreateCustomCollectionSource](xref:DevExpress.ExpressApp.XafApplication.CreateCustomCollectionSource) event.