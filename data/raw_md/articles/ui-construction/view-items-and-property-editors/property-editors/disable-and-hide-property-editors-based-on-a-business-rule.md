---
uid: "113221"
seealso:
- linkId: "113286"
- linkId: "113374"
title: 'Disable and Hide Property Editors Based on a Business Rule'
---
# Disable and Hide Property Editors Based on a Business Rule

**XAF** is shipped with the [Conditional Appearance](xref:113286) module. One of the features provided by this module is an option to disable/enable and show/hide Property Editors based on business rules. This topic contains step-by-step instructions that demonstrate how the Conditional Appearance module can be used for this purpose. Several appearance rules will be created to dynamically hide and disable Property Editors.

![EditorStateExample](~/images/editorstateexample116388.png)

[!include[<Conditional Appearance>](~/templates/main-demo-tip.md)]

Use the [Template Kit](xref:405447) to create a new XAF Solution. Add the Conditional Appearance module to the module project. To do this, open the _MySolution.Module_\\_Module.cs_ (_Module.vb_) file and add the following code to the Module constructor:

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.ConditionalAppearance;
// ...
namespace MySolution.Module {
    public sealed partial class MySolutionModule : ModuleBase {
        public MySolutionModule() {
            // ...
            RequiredModuleTypes.Add(typeof(ConditionalAppearanceModule));
        }
    }
}
```
***

Declare the **Contact** business class in the solution's [Module Project](xref:118045). You can use the **XPO Business Object** template for this purpose. Replace the auto-generated class' code with the following.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
[DefaultClassOptions]
[ImageName("BO_Person")]
public class Contact : BaseObject {
    public virtual string Name { get; set; }
    public virtual bool IsMarried { get; set; }
    public virtual string SpouseName { get; set; }
    public virtual string Address1 { get; set; }
    public virtual string Address2 { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
[DefaultClassOptions]
[ImageName("BO_Person")]
public class Contact : BaseObject {
    public Contact(Session session) : base(session) { }        
    public string Name {
        get { return GetPropertyValue<string>(nameof(Name)); }
        set { SetPropertyValue<string>(nameof(Name), value); }
    }
    public bool IsMarried {
        get { return GetPropertyValue<bool>(nameof(IsMarried)); }
        set { SetPropertyValue<bool>(nameof(IsMarried), value); }
    }
    public string SpouseName {
        get { return GetPropertyValue<string>(nameof(SpouseName)); }
        set { SetPropertyValue<string>(nameof(SpouseName), value); }
    }
    public string Address1 {
        get { return GetPropertyValue<string>(nameof(Address1)); }
        set { SetPropertyValue<string>(nameof(Address1), value); }
    }
    public string Address2 {
        get { return GetPropertyValue<string>(nameof(Address2)); }
        set { SetPropertyValue<string>(nameof(Address2), value); }
    }
}
```
***

The sample **Contact** class contains five properties: Name, IsMarried, SpouseName, Address1, Address2.

To ensure that the **SpouseName** Property Editor is only displayed when a contact is married, add the following [](xref:DevExpress.ExpressApp.ConditionalAppearance.AppearanceAttribute) attribute. The **IsMarried** property should be decorated by the [](xref:DevExpress.Persistent.Base.ImmediatePostDataAttribute) attribute to ensure that the **SpouseName** Property Editor is immediately hidden when a user changes the **IsMarried** value.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.ConditionalAppearance;
using DevExpress.ExpressApp.Editors;
//...
[ImmediatePostData]
public bool IsMarried {
    // ...
}
[Appearance("Single", Visibility = ViewItemVisibility.Hide, Criteria = "!IsMarried", Context="DetailView")]
public string SpouseName {
    // ...
}
```
***

The appearance rule, declared by the following attribute, ensures that the **Address2** Property Editor is enabled only if the **Address1** field is filled. Otherwise, the **Address2** Property Editor should is disabled.

# [C#](#tab/tabid-csharp)

```csharp
[ImmediatePostData]
public string Address1 {
    // ...
}
[Appearance("AddressOneIsEmpty", Enabled = false, Criteria = "IsNullOrEmpty(Address1)", Context="DetailView")]
public string Address2 {
    // ...
}
```
***
