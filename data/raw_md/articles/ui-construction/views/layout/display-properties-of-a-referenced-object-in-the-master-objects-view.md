---
uid: "115793"
seealso:
- linkId: DevExpress.ExpressApp.Editors.EditorAliases
- linkId: "117395"
title: Display Properties of a Referenced Object in the Master Object's View
---
# Display Properties of a Referenced Object in the Master Object's View

By default, properties of the current object type are displayed in a View. However, you may want to add editors for properties that are exposed by a related object, declared using a [reference property](xref:113572). This topic describes the different approaches you can use to display properties of such an associated object.

The following `Project` and `Task` business classes are used in this topic.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
using System.ComponentModel;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
// ...
[DefaultClassOptions]
public class Project : BaseObject {
    public virtual string ProjectName { get; set; }
    public virtual DateTime? Deadline { get; set; }
    public virtual IList<Task> Tasks { get; set; }= new ObservableCollection<Task>();
}
[DefaultClassOptions]
public class Task : BaseObject {
    public virtual string Subject { get; set; }
    public virtual string Description { get; set; }
    public virtual Project Project { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

***

Although these classes are Entity Framework Core Code-First entities, you can use the same approaches with XPO persistent classes.

## Apply the ExpandObjectMembers Attribute
When you apply the [](xref:DevExpress.Persistent.Base.ExpandObjectMembersAttribute) to a reference property, all properties of the related object are added to the model of the List and Detail Views of the current object type.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;
// ...
public class Task : BaseObject {
    // ...
    [ExpandObjectMembers(ExpandObjectMembers.Always)]
    public virtual Project Project { get; set; }
}
```

***

As a result, all visible properties of the `Project` class will be added to `Task` Views (to the [!include[Node_Views_ListView_Columns](~/templates/node_views_listview_columns111387.md)] and [!include[Node_Views_DetailView_Items](~/templates/node_views_detailview_items111383.md)] nodes in the [Application Model](xref:112579)). New columns and View Items are highlighted in red in the image below.

![WaysToDisplayRef_ExpandObjectMembers](~/images/waystodisplayref_expandobjectmembers122595.png)

Unnecessary columns/items can be removed in the [Model Editor](xref:112582).

You can pass other values of the [](xref:DevExpress.Persistent.Base.ExpandObjectMembers) enumeration to add Project properties only to `Task` List Views, or only to `Task` Detail Views. You can also pass the _memberName_ parameter to add a single specific property instead of all visible properties. For details, refer to the [](xref:DevExpress.Persistent.Base.ExpandObjectMembersAttribute) class description.

## Add an Editor or Column in the Model Editor
You can add a column/item to a List or Detail View in the [Model Editor](xref:112582), using the context menu of [!include[Node_Views_ListView_Columns](~/templates/node_views_listview_columns111387.md)] and [!include[Node_Views_DetailView_Items](~/templates/node_views_detailview_items111383.md)] nodes. Use the `ReferencePropertyName.PropertyName` notation when specifying the [IModelMemberViewItem.PropertyName](xref:DevExpress.ExpressApp.Model.IModelMemberViewItem.PropertyName) value. The image below demonstrates how to add the `Project.Deadline` column to the `Task` List View in the Model Editor.

![WaysToDisplayRef_ME](~/images/waystodisplayref_me122596.png)

You can add a **PropertyEditor** node to the [!include[Node_Views_DetailView_Items](~/templates/node_views_detailview_items111383.md)] in a similar manner, but note that you should also add a corresponding layout item to the [!include[Node_Views_DetailView_Layout](~/templates/node_views_detailview_layout111385.md)] node. An example is provided in the [Add an Editor to a Detail View](xref:403217) tutorial.

## Use the DetailPropertyEditor in a Detail View
You can use the **DetailPropertyEditor** Property Editor to display a reference property as an embedded Detail View in WinForms applications. For this purpose, you can apply the `EditorAlias` attribute to the reference property.

# [C#](#tab/tabid-csharp)

```csharp
using DevExpress.ExpressApp.Editors;
// ...
public class Task : BaseObject {
    // ...
    [EditorAlias(EditorAliases.DetailPropertyEditor)]
    public virtual Project Project { get; set; }
}
```

***

Alternatively, you can run the [Model Editor](xref:112582) for the _platform-specific_ project (WinForms) and set the [IModelCommonMemberViewItem.PropertyEditorType](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.PropertyEditorType) property of the **BOModel** | **_\<Class\>_** | **OwnMembers** | **_\<Member\>_** node to **DetailPropertyEditor**.

![WaysToDisplayRef_DetailPropertyEditor_ME](~/images/waystodisplayref_detailpropertyeditor_me122598.png)

The image below demonstrates the `Project` property displayed using the **DetailPropertyEditor**.

![WaysToDisplayRef_DetailPropertyEditor](~/images/waystodisplayref_detailpropertyeditor122597.png)

## Add a Calculated Property
You can declare a property whose value is calculated as follows.

# [C#](#tab/tabid-csharp)

```csharp
public class Task : BaseObject {
    // ...
    public DateTime? Deadline {
        get { return Project != null ? Project.Deadline : null; }
    }
}
```

***

You can also [add a custom calculated field in the Model Editor](xref:113583) and refer to the required property using [IModelMember.Expression](xref:DevExpress.ExpressApp.Model.IModelMember.Expression).

![WaysToDisplayRef_CustomField](~/images/waystodisplayref_customfield122599.png)

In both these cases, the `Deadline` property will be readonly in `Task` Views. If you need to edit it, implement the [INotifyPropertyChanged](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.inotifypropertychanged) interface and declare `Deadline` as follows.

# [C#](#tab/tabid-csharp)

```csharp
using System.ComponentModel.DataAnnotations.Schema;
// ...
public class Task : BaseObject, INotifyPropertyChanged {
    // ...
    private void OnChanged(String propertyName) {
        if (PropertyChanged != null) {
            PropertyChanged(this, new PropertyChangedEventArgs(propertyName));
        }
    }
    public event PropertyChangedEventHandler PropertyChanged;
    [NotMapped]
    public DateTime? Deadline {
        get { return Project != null ? Project.Deadline : null; }
        set {
            if (Project != null) {
                Project.Deadline = value;
                OnChanged(nameof(Project));
            }
        }
    }
}
```

***
In XPO, you do not need to implement `INotifyPropertyChanged`; the `OnChanged` protected method is available in the base [](xref:DevExpress.Xpo.XPBaseObject) class. Additionally, the [](xref:DevExpress.Xpo.NonPersistentAttribute) is used instead of [NotMappedAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.dataannotations.schema.notmappedattribute) in XPO.
