---
uid: "117395"
seealso: []
title: The Importance of Property Change Notifications for Automatic UI Updates
seealso:
  - linkId: "404292"
---
# The Importance of Property Change Notifications for Automatic UI Updates

To display a consistent user interface, your XAF application must receive notifications from [business classes](xref:113664) when their property values are changed. For instance, [Conditional Appearance](xref:113286) and [Validation](xref:113684) modules may require an immediate UI update when a user modifies a certain value. This topic describes how to enable notifications from [XPO](xref:112600), [Entity Framework Core](xref:401886), and [non-persistent](xref:116516) business classes.

**For non-collection properties (for example, for simple value types)**, the notification mechanism requires that the standard @System.ComponentModel.INotifyPropertyChanged interface is supported and its @System.ComponentModel.INotifyPropertyChanged.PropertyChanged event is implemented. To send a notification to internal XAF code, trigger `PropertyChanged` from a property [set accessor](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/set) within a business class.

[Collection properties](xref:113568) in data model classes must implement the following interfaces depending on the target ORM:

- EF Core: `INotifyCollectionChanged` (for example, use `ObservableCollection<T>`)
- XPO: `IBindingList` (for example, use `XPCollection`).

The collection notifies the `ListView.CollectionSource` and other XAF code about relevant changes through the `INotifyCollectionChanged.CollectionChanged` and `IBindingList.ListChanged` events respectively (when items are added or removed, when the entire collection is refreshed, etc.). The UI will update its data automatically to reflect appropriate changes. Each item in the collection should also implement the `INotifyPropertyChanged` interface to notify the UI when a property value is changed.

## PropertyChanged and CollectionChanged Event in Entity Framework Core

XAF EF Core projects enable change-tracking proxies with the [UseChangeTrackingProxies](https://learn.microsoft.com/en-us/dotnet/api/microsoft.entityframeworkcore.proxiesextensions.usechangetrackingproxies) method. To support notifications in your business classes, define properties as described in the following article: [Change-tracking proxies](https://learn.microsoft.com/en-us/ef/core/change-tracking/change-detection#change-tracking-proxies):

```csharp
public class Blog {
    public virtual int Id { get; set; }
    public virtual string Name { get; set; }
    public virtual IList<Post> Posts { get; } = new ObservableCollection<Post>();
}
```

[!include[inotifycollectionchanged-note](~/templates/inotifycollectionchanged-note.md)]

[!include[security-system-important-note-about-change-tracking](~/templates/security-system-important-note-about-change-tracking.md)]

## PropertyChanged Event in XPO

You do not need to implement the `INotifyPropertyChanged` interface manually in an XPO business class. When you declare an XPO business class, you inherit [](xref:DevExpress.Persistent.BaseImpl.BaseObject) (or another [base persistent class](xref:113146)) that already supports this interface. You can trigger the `PropertyChanged` event from a property set accessor by executing the `XPBaseObject.OnChanged` or `PersistentBase.SetPropertyValue` helper method.

# [C#](#tab/tabid-csharp)

```csharp
public class Department : BaseObject {
    // ...
    private string title;
    public string Title {
        get {
            return title;
        }
        set {
            SetPropertyValue(nameof(Title), ref title, value);
        }
    }
}
```
***

**See Also:** [Creating a Persistent Object](xref:2077)

## PropertyChanged Event in Non-Persistent Classes
There are two ways to use the `PropertyChanged` event in a non-persistent class:

- Inherit your non-persistent class from base non-persistent classes, as described in [INotifyPropertyChanged Support](xref:116516#inotifypropertychanged-support)

- Implement this interface using the technique described above for the Entity Framework.

# [C#](#tab/tabid-csharp)

```csharp
public class NonPersistentObject1 : INotifyPropertyChanged {
    // ...
    private string sampleProperty; 
    public string SampleProperty {
        get { return sampleProperty; }
        set {
            if (sampleProperty != value) {
                sampleProperty = value;
                OnPropertyChanged();
            }
        }
    }
    private void OnPropertyChanged([System.Runtime.CompilerServices.CallerMemberName] string propertyName = null) {
        PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(propertyName));
    }
    public event PropertyChangedEventHandler PropertyChanged;
}
```
***

To create a new non-persistent class that supports `INotifyPropertyChanged`, use the **XAF Business Object** | **Non-Persistent Object** project item template.

![NonPersistentObject](~/images/nonpersistentobject125446.png)
