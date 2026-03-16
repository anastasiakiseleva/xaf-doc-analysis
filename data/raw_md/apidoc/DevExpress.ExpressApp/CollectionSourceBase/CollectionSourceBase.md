---
uid: DevExpress.ExpressApp.CollectionSourceBase
name: CollectionSourceBase
type: Class
summary: An abstract class that serves as the base class for Collection Source classes.
syntax:
  content: 'public abstract class CollectionSourceBase : IDisposable'
seealso:
- linkId: DevExpress.ExpressApp.CollectionSourceBase._members
  altText: CollectionSourceBase Members
---
To display a collection of objects in a UI, the **XAF** uses [List Views](xref:112611). These Views allow end-users to browse and manipulate a collection of objects of the same class, whether persistent or not. By default, a List View is displayed as a grid in which a column represents the class' property and a row represents a single object.

A Collection Source serves as the data source for a List View. A Collection Source is a mediator between a List View and an Object Space (see [](xref:DevExpress.ExpressApp.BaseObjectSpace)).  A Collection Source retrieves a typed collection of objects from an **ObjectSpace**, stores them in the internal [CollectionSourceBase.Collection](xref:DevExpress.ExpressApp.CollectionSourceBase.Collection) and feeds this collection to a List View. Besides object retrieval, a Collection Source exposes additional methods that allow a List View to manipulate the Collection Source's object collection. These include methods to add and remove objects from the Collection Source's collection, methods that deal with the collection filtering, various event notifications and more.

The **CollectionSourceBase** class is an abstract class from which all the Collection Sources derive. The following table lists XAF's built-in Collection Sources.

| **CollectionSourceBase Descendant** | Description |
|---|---|
| [](xref:DevExpress.ExpressApp.CollectionSource) | Used by default for the root List Views. |
| [](xref:DevExpress.ExpressApp.PropertyCollectionSource) | Used by the nested List Views that display collection properties. |
| [](xref:DevExpress.ExpressApp.LookupEditPropertyCollectionSource) | Used by the [Lookup Property Editors](xref:113014)' List Views. |

**XAF** automatically creates and manipulates a Collection Source when it creates a List View. However, there are few typical tasks that require you to instantiate or access a Collection Source manually. Here they are:

* Create a custom List View. To be able to do it, you need to first create the required collection source.
* Filter a collection of objects that a List View displays on the data source level. To do so, you need to access the List View's Collection Source. The [Criteria Property of a List View's Collection Source](xref:112988) topic describes this.

There are certain rare cases in which you may need to create a custom Collection Source. While implementing a custom Collection Source derived from the [](xref:DevExpress.ExpressApp.CollectionSourceBase) class, the following methods, not described in the documentation, can be overridden.

{|
|-

! Member Name
! Description
|-

| **ApplyCriteriaCore**
| Abstract. Filters the Collection Source's collection using the specified [](xref:DevExpress.Data.Filtering.CriteriaOperator).
|-

| **DefaultAllowAdd**
| Returns a Boolean value that indicates whether an object can be added to the Collection Source's collection. For instance, if the Collection Source's collection has not been instantiated, this method returns **false**.
|-

| **DefaultAllowRemove**
| Returns a Boolean value that indicates whether an object can be removed from the Collection Source's collection. For instance, if the Collection Source's collection is read-only, this method returns **false**.
|-

| **GetInitialCountForLookup**
| This method returns an estimate on the total number of objects in the Collection Source's [CollectionSourceBase.Collection](xref:DevExpress.ExpressApp.CollectionSourceBase.Collection). The value returned by this method is used to decide whether or not the [search functionality](xref:112925) must be enabled for a Lookup Property Editor's List View. The returned value is considered if the [IModelCommonMemberViewItem.LookupEditorMode](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.LookupEditorMode) property of the **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node that corresponds to the property being edited, is set to **Auto**.
|-

| **OnCollectionChanging**
| Called in the [CollectionSourceBase.ResetCollection](xref:DevExpress.ExpressApp.CollectionSourceBase.ResetCollection(System.Boolean)) method, before recreating the Collection Source's collection. Raises the [CollectionSourceBase.CollectionChanging](xref:DevExpress.ExpressApp.CollectionSourceBase.CollectionChanging) event.
|-

| **OnCollectionChanged**
| Called in the private **EnsureCollection** method, invoked by the [CollectionSourceBase.ResetCollection](xref:DevExpress.ExpressApp.CollectionSourceBase.ResetCollection(System.Boolean)) method, after the Collection Source's collection has been recreated. Raises the [CollectionSourceBase.CollectionChanged](xref:DevExpress.ExpressApp.CollectionSourceBase.CollectionChanged) event.
|-

| **OnCollectionReloading**
| Called in the [CollectionSourceBase.Reload](xref:DevExpress.ExpressApp.CollectionSourceBase.Reload) method, before the Collection Source's collection has been reloaded. Raises the [CollectionSourceBase.CollectionReloading](xref:DevExpress.ExpressApp.CollectionSourceBase.CollectionReloading) event.
|-

| **OnCollectionReloaded**
| Called in the [CollectionSourceBase.Reload](xref:DevExpress.ExpressApp.CollectionSourceBase.Reload) method, after the Collection Source's collection has been reloaded. Raises the [CollectionSourceBase.CollectionReloaded](xref:DevExpress.ExpressApp.CollectionSourceBase.CollectionReloaded) event.
|-

| **OnCriteriaApplying**
| Called in the protected **ApplyCriteria** method before the **ApplyCriteriaCore** method has been called. Raises the [CollectionSourceBase.CriteriaApplying](xref:DevExpress.ExpressApp.CollectionSourceBase.CriteriaApplying) event.
|-

| **OnCriteriaApplied**
| Called in the protected **ApplyCriteria** method after the **ApplyCriteriaCore** method has been called. Raises the [CollectionSourceBase.CriteriaApplied](xref:DevExpress.ExpressApp.CollectionSourceBase.CriteriaApplied) event.
|-

| **OnCriteriaChanging**
| Called after the [CollectionSourceBase.Criteria](xref:DevExpress.ExpressApp.CollectionSourceBase.Criteria) dictionary has been changed. Override this method in your descendant to throw an exception, if your Collection Source's collection does not support changing the criteria applied to it.
|-

| **RecreateCollection**
| Abstract. Creates and returns a collection of the [CollectionSourceBase.ObjectTypeInfo](xref:DevExpress.ExpressApp.CollectionSourceBase.ObjectTypeInfo).**Type** objects. The collection's objects satisfy the criteria passed as the method's first parameter. The collection's objects are sorted in the order specified by the method's second parameter.
|-

| **SetDisplayableProperties**
| If the Collection Source's collection is derived from the [](xref:DevExpress.Xpo.XPBaseCollection), this method sets the 
collection's [XPBaseCollection.DisplayableProperties](xref:DevExpress.Xpo.XPBaseCollection.DisplayableProperties) property to the specified value.
|}
