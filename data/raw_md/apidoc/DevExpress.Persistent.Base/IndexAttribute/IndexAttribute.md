---
uid: DevExpress.Persistent.Base.IndexAttribute
name: IndexAttribute
type: Class
summary: Specifies the target business class property's order index, that will be considered when generating layout items in a Detail View, and columns in a List View.
syntax:
  content: |-
    [AttributeUsage(AttributeTargets.Property, Inherited = false, AllowMultiple = false)]
    public class IndexAttribute : ModelExportedValueAttribute
seealso:
- linkId: DevExpress.Persistent.Base.IndexAttribute._members
  altText: IndexAttribute Members
---
Apply the **Index** attribute to business class properties, to specify the order by which they will be added to the property list used to arrange corresponding layout items in a Detail View, and columns in a List View. To set the required index, pass it as the attribute's _index_ parameter. When generating the [Application Model](xref:112580)'s nodes, the index specified via this attribute will be assigned to the appropriate **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node's [IModelNode.Index](xref:DevExpress.ExpressApp.Model.IModelNode.Index) property.

The property list that is used to arrange corresponding layout items in a Detail View and columns in a List View is populated in the following way. First, the properties that are indexed via the **Index** attribute are added in index order. Then, non-indexed properties are added in a particular order. In a List View, only the properties that are declared in the represented class are made visible, and arranged according to their order in the list. The inherited properties are made invisible (their **Index** property in the Application Model's [!include[Node_Views_ListView_Columns_Column](~/templates/node_views_listview_columns_column111388.md)] node is set to -1). In a Detail View, the layout items corresponding to properties are grouped according to particular rules. These rules are fully detailed in the [View Items Layout Customization](xref:112817) topic. However, the order in which they follow in a group is determined by the order in which the corresponding properties are listed.

The following example demonstrates how the **Index** attribute influences the column order in a List View and the layout items order in a Detail View.

# [C# (EF Core)](#tab/tabid-csharp-ef)

```csharp
[DefaultClassOptions]
public class DomainObject1 : BaseObject {
    [Index(1)]
    public virtual int Property1 { get; set; }
    [Index(2)]
    public virtual int Property2 { get; set; }
    [Index(3)]
    public virtual int Property3 { get; set; }
    [Index(5)]
    public virtual int Property4 { get; set; }
    [Index(4)]
    public virtual int Property5 { get; set; }
}

[DefaultClassOptions]
public class DomainObject2 : DomainObject1 {
    [Index(7)]
    public virtual int Property6 { get; set; }
    [Index(6)]
    public virtual int Property7 { get; set; }
    public virtual int Property8 { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)

```csharp
[DefaultClassOptions]
public class DomainObject1 : BaseObject {
    public DomainObject1(Session session) : base(session) { }
    [Index(1)]
    public int Property1 {
        get { return GetPropertyValue<int>(nameof(Property1)); }
        set { SetPropertyValue<int>(nameof(Property1), value); }
    }
    [Index(2)]
    public int Property2 {
        get { return GetPropertyValue<int>(nameof(Property2)); }
        set { SetPropertyValue<int>(nameof(Property2), value); }
    }
    [Index(3)]
    public int Property3 {
        get { return GetPropertyValue<int>(nameof(Property3)); }
        set { SetPropertyValue<int>(nameof(Property3), value); }
    }
    [Index(5)]
    public int Property4 {
        get { return GetPropertyValue<int>(nameof(Property4)); }
        set { SetPropertyValue<int>(nameof(Property4), value); }
    }
    [Index(4)]
    public int Property5 {
        get { return GetPropertyValue<int>(nameof(Property5)); }
        set { SetPropertyValue<int>(nameof(Property5), value); }
    }
}
[DefaultClassOptions]
public class DomainObject2 : DomainObject1 {
    public DomainObject2(Session session) : base(session) { }
    [Index(7)]
    public int Property6 {
        get { return GetPropertyValue<int>(nameof(Property6)); }
        set { SetPropertyValue<int>(nameof(Property6), value); }
    }
    [Index(6)]
    public int Property7 {
        get { return GetPropertyValue<int>(nameof(Property7)); }
        set { SetPropertyValue<int>(nameof(Property7), value); }
    }
    public int Property8 {
        get { return GetPropertyValue<int>(nameof(Property8)); }
        set { SetPropertyValue<int>(nameof(Property8), value); }
    }
}
```
***

In the Detail and List Views of the DomainObject1 class, properties are arranged according to the indexes specified for them:

![IndexAttribute_DetailView1](~/images/indexattribute_detailview1116304.png)

![IndexAttribute_ListView1](~/images/indexattribute_listview1116306.png)

In the Detail View of the DomainObject2 class, inherited properties are grouped and arranged according to the indexes specified for them in the base class. The properties declared in the DomainObject2 class are combined in a separate group, within which they are arranged in the order they are added to the property list: first, indexed properties and then, non-indexed properties are displayed.

![IndexAttribute_DetailView2](~/images/indexattribute_detailview2116305.png)

In the List View of the DomainObject2 class, properties follow each other according to the order they are added to the properties list: first, indexed properties and then, non-indexed properties are displayed. Inherited properties are made invisible.

![IndexAttribute_ListView2](~/images/indexattribute_listview2116307.png)

Since Property Editors are automatically grouped according to specific rules, apply the **Index** attribute in code when you are sure that the target properties will be contained in the same group. For instance, if you index an unlimited string within the properties that will be represented by simple editors, the memo editor representing this string will be located in a separate group, irrespective of the index you specified.