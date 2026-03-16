---
uid: DevExpress.ExpressApp.ObjectView
name: ObjectView
type: Class
summary: Represents a base class for [Views](xref:112611) that display object(s) of a particular type.
syntax:
  content: 'public abstract class ObjectView : CompositeView'
seealso:
- linkId: DevExpress.ExpressApp.ObjectView._members
  altText: ObjectView Members
- linkId: "112611"
---
**XAF** has two actual Object View types - the [](xref:DevExpress.ExpressApp.DetailView) and [](xref:DevExpress.ExpressApp.ListView).  Detail Views are used to view and edit an individual object's properties. List Views are used to view and edit object collections.

Compared to Composite Views, Object Views introduce an additional property to the [Application Model](xref:112580)'s [!include[Node_Views](~/templates/node_views112047.md)] nodes, specifying the type of objects represented by an Object View. For this purpose, the **ObjectView** class supplies a derived version of the [ObjectView.Model](xref:DevExpress.ExpressApp.ObjectView.Model) property which has its type changed to [](xref:DevExpress.ExpressApp.Model.IModelObjectView). The **IModelObjectView** interface exposes a single [IModelObjectView.ModelClass](xref:DevExpress.ExpressApp.Model.IModelObjectView.ModelClass) property, specifying the objects' type.