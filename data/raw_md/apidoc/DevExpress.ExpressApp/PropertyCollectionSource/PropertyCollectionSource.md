---
uid: DevExpress.ExpressApp.PropertyCollectionSource
name: PropertyCollectionSource
type: Class
summary: Serves as the data source for the nested [List Views](xref:112611) that display collection properties.
syntax:
  content: 'public class PropertyCollectionSource : CollectionSourceBase'
seealso:
- linkId: DevExpress.ExpressApp.PropertyCollectionSource._members
  altText: PropertyCollectionSource Members
- linkId: "113161"
---
When an object is displayed in a [Detail View](xref:112611), its collection properties are displayed via nested List Views. All the nested List Views that display collection properties, by default, use instances of the **PropertyCollectionSource** as data sources.

The **PropertyCollectionSource** introduces new members as compared to the [](xref:DevExpress.ExpressApp.CollectionSourceBase) class. These members provide information on the object whose collection property the Collection Source represents. The following table lists them.

| Name | Description |
|---|---|
| [PropertyCollectionSource.MasterObject](xref:DevExpress.ExpressApp.PropertyCollectionSource.MasterObject) | Provides access to the object, whose collection property is represented by the **PropertyCollectionSource**. |
| [PropertyCollectionSource.MasterObjectType](xref:DevExpress.ExpressApp.PropertyCollectionSource.MasterObjectType) | Returns the type of the object whose collection property is represented by the **PropertyCollectionSource**. |
| [PropertyCollectionSource.DeclaredType](xref:DevExpress.ExpressApp.PropertyCollectionSource.DeclaredType) | Returns the type in which the collection property represented by the **PropertyCollectionSource** is declared. |
| [PropertyCollectionSource.MemberInfo](xref:DevExpress.ExpressApp.PropertyCollectionSource.MemberInfo) | Provides access to the **IMemberInfo** object that contains metadata information on the collection property represented by the **PropertyCollectionSource**. |

To create a PropertyCollectionSource instance, use the [XafApplication.CreatePropertyCollectionSource](xref:DevExpress.ExpressApp.XafApplication.CreatePropertyCollectionSource*) method. There are several overloads of this method. If you use the one that does not include a _dataAccessMode_ parameter, a value of the Application Model's [IModelListView.DataAccessMode](xref:DevExpress.ExpressApp.Model.IModelListView.DataAccessMode) property will be used to initialize the [CollectionSourceBase.DataAccessMode](xref:DevExpress.ExpressApp.CollectionSourceBase.DataAccessMode) property of the created collection source. Otherwise, use the overload with the _dataAccessMode_ parameter. In this instance, the **DataAccessMode** property value from the Application Model will be ignored. By default, nested collections are created in [Client](xref:118449) mode, because their [IModelListView.DataAccessMode](xref:DevExpress.ExpressApp.Model.IModelListView.DataAccessMode) property in the Application Model is set to **Client**.

> [!NOTE]
> If you want to create a Collection Source for a nested List View in [Server, ServerView, InstantFeedback, or InstantFeedbackView](xref:118450) mode, make sure that there is no logic for sorting, filtering or something else in the collection's getter, and there are no subscribers to the collection's events. This logic and subscribers won't be taken into account, because a standalone server collection will be created instead of the original one.