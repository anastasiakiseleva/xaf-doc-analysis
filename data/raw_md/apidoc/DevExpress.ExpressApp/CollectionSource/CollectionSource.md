---
uid: DevExpress.ExpressApp.CollectionSource
name: CollectionSource
type: Class
summary: The Collection Source used for the [List Views](xref:112611) that display collections of business objects.
syntax:
  content: 'public class CollectionSource : CollectionSourceBase'
seealso:
- linkId: DevExpress.ExpressApp.CollectionSource._members
  altText: CollectionSource Members
---
The **CollectionSource** is used by the root (see [View.IsRoot](xref:DevExpress.ExpressApp.View.IsRoot)) List Views. Generally, you can expect a List View to use the **CollectionSource** in the following cases:

* A List View that is displayed in the **XAF** main window. In this case, the List View uses an instance of the **CollectionSource** class as its Collection Source.
    
    ![CollectionSource1](~/images/collectionsource1116264.png)
* A nested List View that displays a collection property uses the [](xref:DevExpress.ExpressApp.PropertyCollectionSource) as the data source. However, the List View displayed in a pop-up [](xref:DevExpress.ExpressApp.Window) invoked by the [LinkUnlinkController.LinkAction](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.LinkAction) uses the **CollectionSource** if the [](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute) is not applied to the collection property.
    
    ![CollectionSource2](~/images/collectionsource2116265.png)
    
    If the collection property has the [](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute) applied, the [](xref:DevExpress.ExpressApp.LookupEditPropertyCollectionSource) is used instead.
* To display a drop-down list of the possible values for a reference property, a Lookup Property Editor creates a [List View](xref:112611). This List View uses an instance of the **CollectionSource** class as a data source if the [](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute) is not applied to the reference property.
    
    ![LookupPropetyEditors_1](~/images/lookuppropetyeditors_1115398.png)
    
    If the reference property has the **DataSourceProperty** attribute applied, the [](xref:DevExpress.ExpressApp.LookupEditPropertyCollectionSource) is used instead.

A **CollectionSource** instance is created in [Client](xref:118449) mode (the default setting), but you can set a [DataView](xref:118452), [Server, ServerView, InstantFeedback, InstantFeedbackView](xref:118450), or [Queryable](xref:402925) mode (see [CollectionSourceBase.DataAccessMode](xref:DevExpress.ExpressApp.CollectionSourceBase.DataAccessMode)) in the Application Model. In the Model Editor, navigate to the target List View node and set the [IModelListView.DataAccessMode](xref:DevExpress.ExpressApp.Model.IModelListView.DataAccessMode) property to one of the [](xref:DevExpress.ExpressApp.CollectionSourceDataAccessMode) enumeration values.

> [!NOTE]
> If you want to create a Collection Source for a nested List View in **Server**, **ServerView**, **InstantFeedback**, **InstantFeedbackView**, or **Queryable** mode, make sure that there is no logic for sorting, filtering or something else in the collection's getter, and there are no subscribers to the collection's events. This logic and subscribers won't be taken into account, because a standalone server collection will be created instead of the original one.

**XAF** automatically creates and manipulates a Collection Source when it creates a List View. However, the following typical tasks require you to instantiate or access a Collection Source manually:

* Create a custom List View. To be able to do it, you need to first create the required collection source.
* Filter a collection of objects that a List View displays on the data source level. To do this, you need to access the List View's Collection Source (see [Criteria Property of a List View's Collection Source](xref:112988)).
