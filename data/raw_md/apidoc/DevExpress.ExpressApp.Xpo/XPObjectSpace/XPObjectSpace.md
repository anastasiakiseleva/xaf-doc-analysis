---
uid: DevExpress.ExpressApp.Xpo.XPObjectSpace
name: XPObjectSpace
type: Class
summary: An [Object Space](xref:113707) that is used for data manipulation using the [DevExpress ORM Tool](xref:1998) (XPO).
syntax:
  content: 'public class XPObjectSpace : CompositeObjectSpace, IDataLockingManager, ISessionProvider, IObjectLayerProvider, IXPDictionaryProvider, IDataLayerProvider, IObjectSpaceAsync, ISupportServerViews, IQuerySupport, ICriteriaProcessor, ISupportServerExpressionEvaluator, ISupportCriteriaCompiler'
seealso:
- linkId: DevExpress.ExpressApp.Xpo.XPObjectSpace._members
  altText: XPObjectSpace Members
- linkId: "405388"
  altText: How to customize the Object Space behavior in XPO-based XAF applications
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/Ticket/Details/T591324/how-to-customize-the-unitofwork-behavior-in-xpo-based-xaf-applications
  altText: How to customize the UnitOfWork behavior in XPO-based XAF applications
---
When an XAF application uses XPO as an ORM layer, an Object Space of the [](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace) class is created. This class is a wrapper over of the [Unit of Work](xref:DevExpress.Xpo.UnitOfWork) which is used in XPO as a cache for persistent objects. To access the UnitOfWork used by the current Object Space, use the [XPObjectSpace.Session](xref:DevExpress.ExpressApp.Xpo.XPObjectSpace.Session) property. The Object Space uses its UnitOfWork to create, manage and delete persistent objects.

The UnitofWork tracks every change to every persistent object. All the changes made to persistent objects are automatically saved to the database by making a single method call (see [BaseObjectSpace.CommitChanges](xref:DevExpress.ExpressApp.BaseObjectSpace.CommitChanges)). For details, refer to the [Session](xref:DevExpress.Xpo.Session) and [Unit of Work](xref:DevExpress.Xpo.UnitOfWork) topics from the XPO documentation. To be sure that changes made to a persistent object's properties are cached and then committed with other changes, call the **SetPropertyValue** method with three parameters in the property setters. This is the recommended way to implement persistent properties if you want changes to be recognized automatically in Units of Work with which XAF's Object Spaces work. If you need to track a custom object change, use the [BaseObjectSpace.SetModified](xref:DevExpress.ExpressApp.BaseObjectSpace.SetModified*) method.

**XPObjectSpace** works with collections of the [](xref:DevExpress.Xpo.XPCollection) type when it is required to load all required objects to a client at once, and with the [](xref:DevExpress.Xpo.XPServerCollectionSource) collection type when loading objects in small portions on demand.

To create a new Object Space, use the [XafApplication.CreateObjectSpace(Type)](xref:DevExpress.ExpressApp.XafApplication.CreateObjectSpace*) method. This method finds a suitable Object Space Provider for the specified business object type. Different Object Space Provider types return different @DevExpress.ExpressApp.BaseObjectSpace descendants. For more information about Object Space and Object Space Provider types, see the following topics:

* [](xref:113707)
* @DevExpress.ExpressApp.BaseObjectSpace

