---
uid: "113573"
seealso:
- linkId: DevExpress.Persistent.Base.ExpandObjectMembers
- linkId: DevExpress.Xpo.AggregatedAttribute
title: Reference Properties in XPO
owner: Ekaterina Kiseleva
---
# Reference Properties in XPO

The example below illustrates how to implement [Reference (Foreign Key, Complex Type) Properties](xref:113572) in an XPO persistent class.

# [C#](#tab/tabid-csharp)

```csharp
private ReferencedObject lookupReferencedObject;
// Displayed in a lookup control:
public ReferencedObject LookupReferencedObject {
    get { return lookupReferencedObject; }
    set { SetPropertyValue(nameof(LookupReferencedObject), ref lookupReferencedObject, value); }
}

private ExpandPropertiesObject expandPropertiesObject;
// Displayed in a set of editors. Each editor represents an individual property of the referenced object:
[Aggregated, ExpandObjectMembers(ExpandObjectMembers.Always)]
public ExpandPropertiesObject ExpandPropertiesObject {
    get { return expandPropertiesObject; }
    set { SetPropertyValue(nameof(ExpandPropertiesObject), ref expandPropertiesObject, value); }
}

private EmbeddedDetailViewObject embeddedDetailViewObject;
// Displayed in a Detail Property Editor that shows a referenced object's Detail View:
[Aggregated, EditorAlias(EditorAliases.DetailPropertyEditor), ExpandObjectMembers(ExpandObjectMembers.Never)]
public EmbeddedDetailViewObject EmbeddedDetailViewObject {
    get { return embeddedDetailViewObject; }
    set { SetPropertyValue(nameof(EmbeddedDetailViewObject), ref embeddedDetailViewObject, value); }
}

private PopupDetailViewObject popupDetailViewObject;
// Displayed in a button edit that invokes a referenced object's Detail View in a separate modal window:
[Aggregated, ExpandObjectMembers(ExpandObjectMembers.Never)]
public PopupDetailViewObject PopupDetailViewObject {
    get { return popupDetailViewObject; }
    set { SetPropertyValue(nameof(PopupDetailViewObject), ref popupDetailViewObject, value); }
}
```
***

If you use **Detail Property Editor** for a reference property, or apply [](xref:DevExpress.Persistent.Base.ExpandObjectMembers) attribute to a reference property, it is required to initialize such a property in the when a new parent object is created. Otherwise, the reference property's fields will be read-only. The initialization should be done in the overridden **AfterConstruction** method the following way:

# [C#](#tab/tabid-csharp)

```csharp
public override void AfterConstruction() {
    base.AfterConstruction();
    embeddedDetailViewObject = new EmbeddedDetailViewObject(Session);
}
```
***