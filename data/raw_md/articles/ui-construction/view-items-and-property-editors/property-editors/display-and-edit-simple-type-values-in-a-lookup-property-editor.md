---
uid: "403100"
title: 'Display and Edit Simple Type Values in a Lookup Property Editor'
owner: Dmitry Egorov
seealso: []
---
# Display and Edit Simple Type Values in a Lookup Property Editor

This help topic describes how to allow end users to select a property value of a simple type (string, integer, enumeration, and so on) in a lookup editor.

> [!IMPORTANT]
> The examples demonstrated in this help topic require calculation on the client side and do not support [Server, ServerView, InstantFeedback, and InstantFeedbackView](xref:118450) modes.

## Populate the Lookup Editor with Values from Another Property

This section demonstrates how to display user-friendly strings instead of simple type values in a lookup editor.

### Scenario
Suppose you have the following class and want to display user-friendly strings for the **Position** integer property:

**File**: _MySolution.Module\BusinessObjects\DemoClass.cs_.

# [C# (EF Core)](#tab/tabid-csharp-ef)
```csharp
using DevExpress.Persistent.Base;
using System.ComponentModel.DataAnnotations;
//...
[DefaultClassOptions]
public class DemoClass : BaseObject {
    public virtual int Position { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)
```csharp
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;
//...
[DefaultClassOptions]
public class DemoClass : BaseObject {
    public DemoClass(Session session) : base(session) { }
    int _position;
    public int Position {
        get { return _position; }
        set { SetPropertyValue(nameof(Position), ref _position, value); }
    }
}
```
***

> [!ImageGallery]
> 
> ![The UI with a numeric editor (before customization)](~/images/lookup_editor_with_values_from_another_property_before.png)
> ![The UI with a lookup editor (after customization)](~/images/lookup_editor_with_values_from_another_property_after.png)

### Solution

1. Apply the [Browsable](xref:System.ComponentModel.BrowsableAttribute) attribute to the `Position` property to hide its editor from the UI:

    # [C# (EF Core)](#tab/tabid-csharp-ef)
    ```csharp
    using System.ComponentModel;
    //...
    public class DemoClass : BaseObject {
        //...
        [Browsable(false)]
        public virtual int Position { get; set; }
    }

    // Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
    ```

    # [C# (XPO)](#tab/tabid-csharp-xpo)
    ```csharp
    using System.ComponentModel;
    //...
    public class DemoClass {
        //...
        [Browsable(false)]
        public int Position {
            //...
        }
    }
    ```
    ***

2. Create an additional `PositionPropertyWrapper` class that is a wrapper for the `DemoClass.Position` property. Apply the [DomainComponent](xref:DevExpress.ExpressApp.DC.DomainComponentAttribute) attribute to this class to make it [non-persistent](xref:116516). In `PositionPropertyWrapper`, the `Key` property stores the original integer values, and the `DisplayName` property returns their user-friendly string representations.

    **File**: _MySolution.Module\BusinessObjects\PositionPropertyWrapper.cs_.

    # [C#](#tab/tabid-csharp)

    ```csharp
    using DevExpress.ExpressApp.DC;
    //...
    [DomainComponent, XafDefaultProperty(nameof(PositionName))]
    public class PositionPropertyWrapper {
        private int _key;
        private string _positionName;
        public PositionPropertyWrapper(string positionName, int key) {
            this._key = key;
            this._positionName = positionName;
        }
        [DevExpress.ExpressApp.Data.Key]
        public int Key { get { return _key; } }
        public string PositionName { get { return _positionName; } }
    }
    ```
    ***

    [`DomainComponent`]: xref:DevExpress.ExpressApp.DC.DomainComponentAttribute
    [`XafDefaultProperty`]: xref:DevExpress.ExpressApp.DC.XafDefaultPropertyAttribute
    [`DevExpress.ExpressApp.Data.Key`]: xref:DevExpress.ExpressApp.Data.KeyAttribute

    > [!IMPORTANT]
    > Use the `Key` attribute from the `DevExpress.ExpressApp.Data` namespace only (not from the [System.ComponentModel.DataAnnotations](xref:System.ComponentModel.DataAnnotations) or [](xref:DevExpress.Xpo) namespaces). This attribute is required for XAF ASP.NET Core Blazor applications.

3. Extend `DemoClass` with the `PositionDataSource` property that stores the collection of non-persistent `PositionPropertyWrapper` objects. The `Position` lookup editor displays these objects. Apply the [Browsable](xref:System.ComponentModel.BrowsableAttribute) attribute to the `PositionDataSource` property to hide its editor from the UI: 

    **File**: _MySolution.Module\BusinessObjects\DemoClass.cs_.

    # [C# (EF Core)](#tab/tabid-csharp-ef)

    ```csharp
    using System.ComponentModel;
    using System.ComponentModel.Annotations;
    //...
    public class DemoClass : BaseObject {
        //...
        private BindingList<PositionPropertyWrapper> _positionDataSource;
        [NotMapped, Browsable(false)]
        public BindingList<PositionPropertyWrapper> PositionDataSource {
            get {
                if (_positionDataSource == null) {
                    _positionDataSource = new BindingList<PositionPropertyWrapper>();
                    for (int i = 0; i < 5; i++) {
                        _positionDataSource.Add(new PositionPropertyWrapper("Position" + i.ToString(), i));
                    }
                }
                return _positionDataSource;
            }
        }
    }

    // Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
    ```

    # [C# (XPO)](#tab/tabid-csharp-xpo)

    ```csharp
    using System.ComponentModel;
    //...
    public class DemoClass {
        //...
        private BindingList<PositionPropertyWrapper> _positionDataSource;
        [Browsable(false)]
        public BindingList<PositionPropertyWrapper> PositionDataSource {
            get {
                if (_positionDataSource == null) {
                    _positionDataSource = new BindingList<PositionPropertyWrapper>();
                    for (int i = 0; i < 5; i++) {
                        _positionDataSource.Add(new PositionPropertyWrapper("Position" + i.ToString(), i));
                    }
                }
                return _positionDataSource;
            }
        }
    }
    ```
    ***

    [`BindingList`]: xref:System.ComponentModel.BindingList`1

4. Extend `DemoClass` with the non-persistent `PositionWrapper` property of the `PositionPropertyWrapper` type to update the persistent `Position` property. Apply the [DataSourceProperty](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute) attribute to `PositionWrapper` to populate the lookup editor data source:

    # [C# (EF Core)](#tab/tabid-csharp-ef)
    ```csharp
    using System.Linq;
    using System.ComponentModel.Annotations;
    // ...
    public class DemoClass : BaseObject {
        // ...
        private PositionPropertyWrapper _positionPropertyWrapper;
        [NotMapped, XafDisplayName("Position")]
        [DataSourceProperty(nameof(PositionDataSource))]
        public PositionPropertyWrapper PositionWrapper {
            get {
                if (_positionPropertyWrapper == null || _positionPropertyWrapper.Key != Position) {
                    _positionPropertyWrapper = PositionDataSource.FirstOrDefault(i => i.Key == Position);
                }
                return _positionPropertyWrapper;
            }
            set {
                _positionPropertyWrapper = value;
                Position = value.Key;
            }
        }
    }

    // Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
    ```

    # [C# (EF XPO)](#tab/tabid-csharp-xpo)
    ```csharp
    using System.Linq;
    // ...
    public class DemoClass {
        // ...
        private PositionPropertyWrapper _positionPropertyWrapper;
        [NonPersistent, XafDisplayName("Position")]
        [DataSourceProperty(nameof(PositionDataSource))]
        public PositionPropertyWrapper PositionWrapper {
            get {
                if (_positionPropertyWrapper == null || _positionPropertyWrapper.Key != Position) {
                    _positionPropertyWrapper = PositionDataSource.FirstOrDefault(i => i.Key == Position);
                }
                return _positionPropertyWrapper;
            }
            set {
                SetPropertyValue(nameof(PositionWrapper), ref _positionPropertyWrapper, value);
                if (!IsLoading && !IsSaving) {
                    Position = value.Key;
                }
            }
        }
    }
    ```
    ***

    [`NonPersistent`]: xref:DevExpress.Xpo.NonPersistentAttribute
    [`XafDisplayName`]: xref:DevExpress.ExpressApp.DC.XafDisplayNameAttribute
    [`DataSourceProperty`]: xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute

5. **Optional**. You can also hide the lookup editor's **Clear** button for a [non-nullable](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/nullable-value-types) `PositionWrapper` property. To do this, set its @DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.AllowClear property to `false` in the Model Editor or apply @DevExpress.ExpressApp.Model.ModelDefaultAttribute to `PositionWrapper`:

    # [C#](#tab/tabid-csharp)
    ```csharp
    using DevExpress.ExpressApp.Model;
    // ...
    public class DemoClass : BaseObject {
        // ...
        [ModelDefault("AllowClear", "false")]
        public PositionPropertyWrapper PositionWrapper {
            // ...
        }
    }
    ```
    ***
    [`ModelDefault`]: xref:DevExpress.ExpressApp.Model.ModelDefaultAttribute

## Populate the Lookup Editor with Persistent Business Objects

This section demonstrates how to display a lookup editor with persistent objects instead of a simple type editor. Use this technique if you have legacy databases and cannot modify their schemas to create associations between tables.

### Scenario
Suppose you have the following classes and want to display the `Position.Title` lookup editor instead of the `DemoClass.PositionTitle` string editor.

# [C# (EF Core)](#tab/tabid-csharp-ef)
```csharp
using DevExpress.ExpressApp.DC;
using DevExpress.Persistent.Base;
using DevExoress.Persistent.BaseImpl.EF;
using System.ComponentModel.DataAnnotations;
//...
[DefaultClassOptions]
public class DemoClass : BaseObject {
    public virtual string PositionTitle { get; set; }
}

[DefaultClassOptions, XafDefaultProperty(nameof(Title))]
public class Position : BaseObject {
    public virtual string Title { get; set; }
}

// Make sure that you use options.UseChangeTrackingProxies() in your DbContext settings.
```

# [C# (XPO)](#tab/tabid-csharp-xpo)
```csharp
using DevExpress.ExpressApp.DC;
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl;
using DevExpress.Xpo;
//...
[DefaultClassOptions]
public class DemoClass : BaseObject {
    public DemoClass(Session session) : base(session) { }
    string positionTitle;
    public string PositionTitle {
        get { return positionTitle; }
        set { SetPropertyValue(nameof(PositionTitle), ref positionTitle, value); }
    }
}

[DefaultClassOptions, XafDefaultProperty(nameof(Title))]
public class Position : BaseObject {
    public Position(Session session) : base(session) { }
    string _title;
    [Size(SizeAttribute.DefaultStringMappingFieldSize)]
    public string Title {
        get {
            return _title;
        }
        set {
            SetPropertyValue(nameof(Title), ref _title, value);
        }
    }
}
```
***

> [!ImageGallery]
> 
> ![The UI with a string editor (before customization)](~/images/lookup_editor_with_values_from_another_data_table_before.png)
> ![The UI with a lookup editor (after customization)](~/images/lookup_editor_with_values_from_another_data_table_after.png)

### Solution

1. Apply the [Browsable](xref:System.ComponentModel.BrowsableAttribute) attribute to the `PositionTitle` property to hide its editor from the UI:

    # [C#](#tab/tabid-csharp)
    ```csharp
    using System.ComponentModel;
    //...
    public class DemoClass : BaseObject {
        //...
        [Browsable(false)]
        public string PositionTitle {
            //...
        }
    }
    ```
    ***

2. Create a non-persistent wrapper property (`LookupPropertyForDisplay`) to fetch records from the `Position` data table:

    # [C# (EF Core)](#tab/tabid-csharp-ef)

    ```csharp
    using DevExpress.Data.Filtering;
    using DevExpress.ExpressApp.DC;
    //...
    public class DemoClass : BaseObject {
        //...
        private Position _LookupPropertyForDisplay;
        [NotMapped, XafDisplayName("Position")]
        public virtual Position LookupPropertyForDisplay {
            get {
                if ((_LookupPropertyForDisplay == null && !string.IsNullOrEmpty(positionTitle)) || 
                (_LookupPropertyForDisplay != null && _LookupPropertyForDisplay.Title != PositionTitle)) {
                    _LookupPropertyForDisplay = 
                        ObjectSpace.GetObjectsQuery<Position>().FirstOrDefault(t => t.Title == positionTitle);
                }
                return _LookupPropertyForDisplay;
            }
            set {
                _LookupPropertyForDisplay = value;
                PositionTitle = value != null ? value.Title : string.Empty;
            }
        }
    }

    // Make sure that you use options.UseChangeTrackingProxies() and options.UseObjectSpaceLinkProxies() in your DbContext settings.
    ```

    # [C# (XPO)](#tab/tabid-csharp-xpo)

    ```csharp
    using DevExpress.Data.Filtering;
    using DevExpress.ExpressApp.DC;
    using DevExpress.Xpo;
    //...
    public class DemoClass : BaseObject {
        //...
        private Position _LookupPropertyForDisplay;
        [NonPersistent, XafDisplayName("Position")]
        public Position LookupPropertyForDisplay {
            get {
                if ((_LookupPropertyForDisplay == null && !string.IsNullOrEmpty(positionTitle)) || 
                (_LookupPropertyForDisplay != null && _LookupPropertyForDisplay.Title != PositionTitle)) {
                    _LookupPropertyForDisplay = 
                        Session.FindObject<Position>(new BinaryOperator("Title", positionTitle));
                }
                return _LookupPropertyForDisplay;
            }
            set {
                SetPropertyValue<Position>(nameof(LookupPropertyForDisplay), 
                                           ref _LookupPropertyForDisplay, value);
                if (!IsLoading && !IsSaving) {
                    PositionTitle = value != null ? value.Title : string.Empty;
                }
            }
        }
    }
    ```
    ***

## Notes

* You can also filter the Lookup Property Editor data sources as described in the following help topic: [How to: Implement Cascading Filtering for Lookup List Views](xref:112681).
* Refer to the following help topics for more information on other ways to implement similar tasks: 

    - [How to: Display an Integer Property as an Enumeration](xref:113563)
    - [How to: Implement a Property Editor Based on a Custom Control (WinForms)](xref:112679)
    - [How to: Implement a Property Editor Based on a Custom Component (Blazor)](xref:402189)
    - [](xref:404599)
    - [How to: Show a Hyper Link for a Business Class Property](https://github.com/DevExpress-Examples/xaf-how-to-show-a-hyper-link-url-email-etc-for-a-business-class-property)
