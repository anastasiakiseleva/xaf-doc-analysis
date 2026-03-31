---
uid: "113574"
title: Reference Properties in EF Core
seealso:  
- linkId: "117395"
- linkId: "404862"
- linkId: "404429"
---
# Reference Properties in EF Core

The example below illustrates how to implement [Reference (Foreign Key, Complex Type) Properties](xref:113572) in an EF Core class.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.DC;
using DevExpress.ExpressApp.Editors;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
// ...
[DefaultClassOptions]
public class ReferencedPropertiesObject : BaseObject {
    // Displayed in a lookup control: 
    public virtual ReferencedObject LookupReferencedObject { get; set; }
    // Displayed in a set of editors. Each editor represents an individual property of the referenced object: 
    [Aggregated, ExpandObjectMembers(ExpandObjectMembers.Always)]
    public virtual ExpandPropertiesObject ExpandPropertiesObject { get; set; }
    // Displayed in a Detail Property Editor that shows a referenced object's Detail View: 
    [Aggregated, EditorAlias(EditorAliases.DetailPropertyEditor)]
    [ExpandObjectMembers(ExpandObjectMembers.Never)]
    public virtual EmbeddedDetailViewObject EmbeddedDetailViewObject { get; set; }
    // Displayed in a button edit that invokes a referenced object's Detail View in a separate modal window: 
    [Aggregated, ExpandObjectMembers(ExpandObjectMembers.Never)]
    public virtual PopupDetailViewObject PopupDetailViewObject { get; set; }

    public override void OnCreated() {
        EmbeddedDetailViewObject = ObjectSpace.CreateObject<EmbeddedDetailViewObject>();
        ExpandPropertiesObject = ObjectSpace.CreateObject<ExpandPropertiesObject>();
    }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

***

Note that reference properties should be declared as _virtual_ in EF.

If you use **Detail Property Editor** to edit a reference property, or apply the [](xref:DevExpress.Persistent.Base.ExpandObjectMembers) attribute to a reference property, it is required to initialize such a property when a new parent object is created. Otherwise, the reference property's fields will be read-only. The initialization should be done in the following way:

* Implement the [](xref:DevExpress.ExpressApp.IXafEntityObject) interface in the parent entity class.
* Implement the [](xref:DevExpress.ExpressApp.IObjectSpaceLink) interface in the parent entity class.
* In the [IXafEntityObject.OnCreated](xref:DevExpress.ExpressApp.IXafEntityObject.OnCreated) method, initialize the referenced property using the [IObjectSpace.CreateObject](xref:DevExpress.ExpressApp.IObjectSpace.CreateObject(System.Type)) method.

The code snippet above demonstrates these steps.