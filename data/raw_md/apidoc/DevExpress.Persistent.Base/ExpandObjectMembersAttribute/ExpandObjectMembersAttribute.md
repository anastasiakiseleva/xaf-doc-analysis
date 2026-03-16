---
uid: DevExpress.Persistent.Base.ExpandObjectMembersAttribute
name: ExpandObjectMembersAttribute
type: Class
summary: Specifies whether the target reference property is displayed via several Property Editors representing the referenced object's properties or via a single Lookup or Object Property Editor.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Struct | AttributeTargets.Property | AttributeTargets.Field | AttributeTargets.Interface, Inherited = true)]
    public class ExpandObjectMembersAttribute : Attribute
seealso:
- linkId: DevExpress.Persistent.Base.ExpandObjectMembersAttribute._members
  altText: ExpandObjectMembersAttribute Members
- linkId: DevExpress.Persistent.Base.ExpandObjectMembers
- linkId: "112612"
---
XAF can visualize a reference property in two ways. The first way is to display a non-aggregated property via a Lookup Property Editor to allow you to choose the property value by selecting one of the existing objects of the corresponding type; aggregated properties are displayed via an Object Property Editor. The second way is to display several Property Editors representing the referenced object's properties. This way you can customize the referenced object's property values, but you cannot change the reference property value by choosing another object since the Property Editor for the reference property is not displayed.

By default, non-aggregated reference properties are visualized via a Lookup Property Editor. Aggregated reference properties are visualized via several Property Editors representing the referenced object's properties. When the default behavior does not suit your needs, decorate a reference property with **ExpandObjectMembersAttribute**. Specify how the property must be displayed via the **expandingMode** parameter in the attribute constructor. There are four possible parameter values. The following example demonstrates their use. Suppose you have the **Contact** class that exposes the **Address** reference property of the **Address** type.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
[DefaultClassOptions]
public class Contact : BaseObject {
    public virtual string Name { get; set; }
    public virtual Address Address { get; set; }
}

[DefaultClassOptions, DefaultProperty(nameof(StreetAddress))]
public class Address : BaseObject {
    public virtual string StreetAddress { get; set; }
    public virtual string Phone { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
[DefaultClassOptions]
public class Contact : BaseObject {
    public Contact(Session session) : base(session) { }
    public string Name {
        get { return GetPropertyValue<string>(nameof(Name)); }
        set { SetPropertyValue<string>(nameof(Name), value); }
    }
    public Address Address {
        get { return GetPropertyValue<Address>(nameof(Address)); }
        set { SetPropertyValue<Address>(nameof(Address), value); }
    }
}
[DefaultClassOptions, DefaultProperty(nameof(StreetAddress))]
public class Address : BaseObject {
    public Address(Session session) : base(session) { }
    public string StreetAddress {
        get { return GetPropertyValue<string>(nameof(StreetAddress)); }
        set { SetPropertyValue<string>(nameof(StreetAddress), value); }
    }
    public string Phone {
        get { return GetPropertyValue<string>(nameof(Phone)); }
        set { SetPropertyValue<string>(nameof(Phone), value); }
    }
}
```
***

If you decorate the **Contact.Address** property with **ExpandObjectMembersAttribute**, here is how **Contact** [Views](xref:112611) will be affected.

* [ExpandObjectMembers.Always](xref:DevExpress.Persistent.Base.ExpandObjectMembers.Always)
    
    # [C# (EF Core)](#tab/tabid-csharp-ef)
    
    ```csharp
    [ExpandObjectMembers(ExpandObjectMembers.Always)]
    public virtual Address Address { 
    ```
    
    # [C# (XPO)](#tab/tabid-csharp-xpo)
    
    ```csharp
    [ExpandObjectMembers(ExpandObjectMembers.Always)]
    public Address Address { 
    ```
    
    ***
    
    The **Contact.Name** property is displayed alongside the properties declared in the **Address** class. You cannot assign another object to the **Contact.Address** property via this UI. All you can do is change the assigned **Address** object's property values.
    
    ![ExpandObjectMemebers.Always](~/images/expandobjectmemebers.always117009.png)
* [ExpandObjectMembers.Never](xref:DevExpress.Persistent.Base.ExpandObjectMembers.Never)
    
    # [C# (EF Core)](#tab/tabid-csharp-ef)
    
    ```csharp
    [ExpandObjectMembers(ExpandObjectMembers.Never)]
    public virtual Address Address { 
    ```
    
    # [C# (XPO)](#tab/tabid-csharp-xpo)
    
    ```csharp
    [ExpandObjectMembers(ExpandObjectMembers.Never)]
    public Address Address { 
    ```
    
    ***
    
    The **Contact.Name** property is displayed alongside the **Contact.Address** Lookup Property Editor. You can assign another object to the **Contact.Address** property via this Lookup Property Editor. You cannot directly modify the assigned **Address** object's property values.
    
    ![ExpandObjectMemebers.Never](~/images/expandobjectmemebers.never117012.png)
* [ExpandObjectMembers.InDetailView](xref:DevExpress.Persistent.Base.ExpandObjectMembers.InDetailView)
    
    # [C# (EF Core)](#tab/tabid-csharp-ef)
    
    ```csharp
    [ExpandObjectMembers(ExpandObjectMembers.InDetailView)]
    public virtual Address Address { 
    ```
    
    # [C# (XPO)](#tab/tabid-csharp-xpo)
    
    ```csharp
    [ExpandObjectMembers(ExpandObjectMembers.InDetailView)]
    public Address Address { 
    ```
    
    ***
    
    The **Contact.Name** property is displayed alongside the **Contact.Address** Lookup Property Editor in List Views. In Detail Views, the **Contact.Name** property is displayed alongside the properties declared in the **Address** class.
    
    ![ExpandObjectMemebers.InDetailView](~/images/expandobjectmemebers.indetailview117010.png)
* [ExpandObjectMembers.InListView](xref:DevExpress.Persistent.Base.ExpandObjectMembers.InListView)
    
    # [C# (EF Core)](#tab/tabid-csharp-ef)
    
    ```csharp
    [ExpandObjectMembers(ExpandObjectMembers.InListView)]
    public virtual Address Address {
    ```
    
    # [C# (XPO)](#tab/tabid-csharp-xpo)
    
    ```csharp
    [ExpandObjectMembers(ExpandObjectMembers.InListView)]
    public Address Address {
    ```
    
    ***
    
    The **Contact.Name** property is displayed alongside the properties declared in the **Address** class in List Views. In Detail Views, a Lookup Property Editor is used to represent the **Contact.Address** property.
    
    ![ExpandObjectMemebers.InListView](~/images/expandobjectmemebers.inlistview117011.png)