---
uid: "113569"
seealso: []
title: Collection Properties in XPO
---
# Collection Properties in XPO

The examples below illustrate how to implement [collection properties](xref:113568) in an XPO persistent class.

Different collection properties have different Actions in a UI. You can manage the **New**, **Delete**, **Link**, or **Unlink** Action's visibility in the Model Editor. Set the List View's [AllowNew](xref:DevExpress.ExpressApp.Model.IModelView.AllowNew), [AllowDelete](xref:DevExpress.ExpressApp.Model.IModelView.AllowDelete), [AllowLink](xref:DevExpress.ExpressApp.Model.IModelListView.AllowLink), or [AllowUnlink](xref:DevExpress.ExpressApp.Model.IModelListView.AllowUnlink) property to **false** to hide these Actions.

> [!Note]
> Refer to the **FeatureCenter** demo to see an example on how to implement collection properties (see _[!include[PathToFeatureCenter](~/templates/path-to-feature-center.md)]\CS\FeatureCenter.Module\PropertyEditors\CollectionPropertiesObject.cs_).

## A collection of the XPCollection type

# [C#](#tab/tabid-csharp)

```csharp
[Association("CollectionProperties-AssociatedObject")]
public XPCollection<AssociatedObject> Association {
    get { return GetCollection<AssociatedObject>(nameof(Association)); }
}
```
***

Refer to the [Relationships Between Persistent Objects in Code and UI](xref:112654#one-to-many-non-aggregated) article for more information on associated collections in XPO.

## An aggregated collection of the XPCollection type

# [C#](#tab/tabid-csharp)

```csharp
[Association("CollectionProperties-AggregatedObject"), Aggregated]
public XPCollection<AggregatedObject> AggregatedAssociation {
    get { return GetCollection<AggregatedObject>(nameof(AggregatedAssociation)); }
}
```
***

Refer to the [Relationships Between Persistent Objects in Code and UI](xref:112654#one-to-many-aggregated) article for more information on aggregated collections in XPO.

## A non-associated collection with persistent objects 
Populate this collection with objects and implement custom logic used to manage them if the collection is not a part of the association. To hide or display the **New** and **Link** or **Delete** and **Unlink** Actions in a UI, decorate the collection property with the **CollectionOperationSet** attribute, and specify the **AllowAdd** and **AllowRemove** parameters.

### A collection of the XPCollection type
The **New**, **Delete**, **Link**, and **Unlink** Actions are available for this collection. We recommend using this collection to display objects, and not to edit them in the UI. In the code snippet below, the **CollectionOperationSet**'s **AllowAdd** and **AllowRemove** parameters are set to **false** to deny a user to change the collection in the UI:

# [C#](#tab/tabid-csharp)

```csharp
private XPCollection<NoAssociationObject> noAssociation;
[CollectionOperationSet(AllowAdd = false, AllowRemove = false)]
public XPCollection<NoAssociationObject> NoAssociation {
    get {
        if(noAssociation == null) {
            noAssociation = new XPCollection<NoAssociationObject>(Session);
        }
    return noAssociation;
    }
}
```
***

You can use the @DevExpress.Xpo.XPBaseCollection.Criteria property to filter collection objects, or set the @DevExpress.Xpo.XPBaseCollection.LoadingEnabled property to **false** and add objects to the collection. Subscribe to the collection's [CollectionChanged](xref:DevExpress.Xpo.XPBaseCollection.CollectionChanged) event to implement the required logic for **New**, **Delete**, **Link**, and **Unlink** Actions.

### A collection of the BindingList type
The **New**, **Delete**, **Link**, and **Unlink** Actions are available for this collection. 

# [C#](#tab/tabid-csharp)

```csharp
private BindingList<NoAssociationObject> persistentBindingList;
public BindingList<NoAssociationObject> PersistentBindingList {
  get {
    if(persistentBindingList == null) {
      persistentBindingList = new BindingList<NoAssociationObject>();
      foreach(NoAssociationObject obj in NoAssociation) {
        persistentBindingList.Add(obj);
      }
    }
    return persistentBindingList;
  }
}
```
***

Subscribe to the collection's [ListChanged](xref:DevExpress.ExpressApp.XafDataView.ListChanged) event to implement the required logic for **New**, **Delete**, **Link**, and **Unlink** Actions.

## The BindingList collection with non-persistent objects
The **New**, **Delete**, **Link**, and **Unlink** Actions are not available for this collection if its master object is a persistent object. If the master object is non-persistent, the **New** and **Delete** Actions are available. To activate **Link** and **Unlink**, set the [LinkUnlinkController.RequirePersistentType](xref:DevExpress.ExpressApp.SystemModule.LinkUnlinkController.RequirePersistentType) property to **false** and handle the @DevExpress.ExpressApp.SystemModule.LinkUnlinkController.CustomCreateLinkView event.

# [C#](#tab/tabid-csharp)

```csharp
private BindingList<SomeObject> nonPersistentObjectBindingList;
private void EnsureNonPersistentObjectBindingList() {
    if(nonPersistentObjectBindingList == null) {
        nonPersistentObjectBindingList = new BindingList<SomeObject>();
        // ...
    }
}
public BindingList<SomeObject> NonPersistentBindingList {
  get {
    EnsureNonPersistentObjectBindingList();
    return nonPersistentObjectBindingList;
  }
}
```
***
