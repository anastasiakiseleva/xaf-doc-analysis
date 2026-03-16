---
uid: "113525"
seealso: []
title: 'How to: Specify a Display Member for a Lookup Editor, Detail Form Caption, and more'
owner: Ekaterina Kiseleva
---
# How to: Specify a Display Member for a Lookup Editor, Detail Form Caption, and more

Business classes in your XAF application should have the [default member](xref:DevExpress.ExpressApp.DC.ITypeInfo.DefaultMember). We recommend that you declare a default property with human-readable values because XAF displays them in the following UI elements: 

* Detail View captions
* The first column of List Views
* Lookup List Views
* Lookup Editors in an unexpanded state

If you do not specify the default property, these elements display an object identifier or a class name.

## Default Property of a Business Class

This section describes how to declare the default property in your business class. The default property must be declared public and visible (not decorated with the [Browsable(false)](xref:System.ComponentModel.BrowsableAttribute) attribute). 

Note that the following sections are arranged in priority order: if you use different techniques in one class, the first described technique determines the default member.

### Apply the DefaultProperty or XafDefaultProperty Attribute 

Apply the @System.ComponentModel.DefaultPropertyAttribute or @DevExpress.ExpressApp.DC.XafDefaultPropertyAttribute to a business class and pass the default property name as the attribute's parameter. 

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp.DC;
// ...
[XafDefaultProperty(nameof(StringProperty))]
public class Task : BaseObject {
    // ...
    public virtual string StringProperty { get; set; }
    // ...
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
using DevExpress.ExpressApp.DC;
// ...
[XafDefaultProperty(nameof(StringProperty))]
public class Task : BaseObject {
    // ...
    public string StringProperty {
    // ...
}

```

***

### Declare a Property with a Specific Name

Declare a property whose name matches or contains one of the **DevExpress.ExpressApp.DC.TypeInfo.DefaultPropertyNames** values (Name, Title, Subject, Caption, Description, Benennung, Nombre, Nome). In this case, you do not need to apply the attributes described in the section above. 

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
public class Task : BaseObject {
    // ...
    public virtual string Subject { get; set; }
    // ...
}
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
public class Task : BaseObject {
    // ...
    public string Subject {
    // ...
}
```

***

> [!Note]
> The **DefaultPropertyNames** values are arranged in priority order. For example, if a business class has both **ObjectName** and **Description** properties, XAF uses **ObjectName** as the default property.

You can also modify the **DefaultPropertyNames** collection in the static constructor of the platform-agnostic Module (the _MySolution.Module\Module.cs_ file).

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp;
using DevExpress.ExpressApp.DC;
// ...
public sealed partial class MySolutionNameModule : ModuleBase {
    // ...
    static MySolutionNameModule() {
        TypeInfo.DefaultPropertyNames.Add("Nombre");
    }
}
```
***

### Apply the FriendlyKeyProperty Attribute 

Apply the @DevExpress.Persistent.Base.FriendlyKeyPropertyAttribute to a business class and pass the default property name as the attribute's parameter. 

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
using DevExpress.ExpressApp.DC;
// ...
[FriendlyKeyProperty(nameof(StringProperty))]
public class Task : BaseObject {
    // ...
    public virtual string StringProperty { get; set; }
    // ...
}
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
[FriendlyKeyProperty(nameof(StringProperty))]
public class Task : BaseObject {
    // ...
    public string StringProperty {
    // ...
}
```

***

> [!NOTE]
> If you do not implement any of the techniques above, XAF uses a key property as the default property.

## Property Displayed in a Lookup Property Editor

In the [Model Editor](xref:112582), set [IModelCommonMemberViewItem.LookupProperty](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.LookupProperty) to the property you want to display in a Lookup Editor instead of the default property.

![LookupProperty](~/images/lookupproperty119384.png)
