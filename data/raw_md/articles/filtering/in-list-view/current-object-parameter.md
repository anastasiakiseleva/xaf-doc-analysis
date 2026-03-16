---
uid: "113204"
seealso:
- linkId: "113307"
- linkId: "112681"
title: Current Object Parameter
owner: Ekaterina Kiseleva
---
# Current Object Parameter

This topic describes the purpose of the Current Object Parameter and includes a usage example.

You may need a Current Object Parameter to filter a [List View](xref:112611) in a Lookup Property Editor. To apply a filter, set the `DataSourceCriteria` attribute for the corresponding reference property. The attribute sets a condition that may need access to business object property values. Use the Current Object Parameter to obtain those values. 

> [!Important]
> You cannot use the Current Object Parameter feature in scenarios not described in this article (for example, with [](xref:DevExpress.Xpo.XPCollection), [appearance rules](xref:113286) or [security permissions](xref:113366)).

Consider an example with 3 classes: `Employee`, `Position`, and `Department`. Both `Employee` and `Position` expose the `Department` [reference property](xref:113572). Additionally, `Employee` exposes the `Position` reference property.

# [EF Core](#tab/tabid-efcore)

```csharp{13,15,23,31,33}
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;

namespace YourApplicationName.Module.BusinessObjects;

[DefaultClassOptions]
public class Employee : BaseObject {

    public virtual string Name { get; set; }

    private Department department;
    
    public virtual Department Department { get; set; }
    
    public virtual Position Position { get; set; }
}

[DefaultClassOptions]
public class Position : BaseObject {

    public virtual string Title { get; set; }

    public virtual Department Department { get; set; }
}

[DefaultClassOptions]
public class Department : BaseObject {

    public virtual string Title { get; set; }

    public virtual IList<Position> Positions { get; set; } = new ObservableCollection<Position>();

    public virtual IList<Employee> Employees { get; set; } = new ObservableCollection<Employee>();
}
```

# [XPO](#tab/tabid-xpo)

```csharp{15}
public class Employee : BaseObject {
    public Employee(Session session) : base(session) { }

    public string Name {
        get { return GetPropertyValue<string>(nameof(Name)); }
        set { SetPropertyValue<string>(nameof(Name), value); }
    }
    
    [Association("Employee-Department")]
    public Department Department {
        get { return GetPropertyValue<Department>(nameof(Department)); }
        set { SetPropertyValue<Department>(nameof(Department), value); }
    }    
    
    public Position Position {
        get { return GetPropertyValue<Position>(nameof(Position)); }
        set { SetPropertyValue<Position>(nameof(Position), value); }
    }
}

public class Position : BaseObject {
    public Position(Session session) : base(session) { }

    public string Title {
        get { return GetPropertyValue<string>(nameof(Title)); }
        set { SetPropertyValue<string>(nameof(Title), value); }
    }

    [Association("Department-Position")]
    public Department Department {
        get { return GetPropertyValue<Department>(nameof(Department)); }
        set { SetPropertyValue<Department>(nameof(Department), value); }
    }
}

public class Department : BaseObject {
    public Department(Session session) : base(session) { }

    public string Title {
        get { return GetPropertyValue<string>(nameof(Title)); }
        set { SetPropertyValue<string>(nameof(Title), value); }
    }

    [Association("Employee-Department")]
    public XPCollection<Employee> Employees {
        get { return GetCollection<Employee>(nameof(Employees)); }
    }

    [Association("Department-Position")]
    public XPCollection<Position> Positions {
        get { return GetCollection<Position>(nameof(Positions)); }
    }
}
```

***

An XAF UI displays reference properties with the help of the Lookup Property Editor:

![|Unfiltered Lookup Property Editor, DevExpress|](~/images/current-object-parameter-lookup-property-editor-unfiltered-devexpress.png)

You may need to filter the drop-down list in a Lookup Property Editor. For example, you may want to display only those positions that correspond to the department where the employee works. To do so, apply the `DataSourceCriteria` attribute to the `Employee.Position` property and specify the filtering criterion as displayed in the following code snippet:

# [EF Core](#tab/tabid-efcore)

```csharp{15}
using DevExpress.Persistent.Base;
using DevExpress.Persistent.BaseImpl.EF;

namespace YourApplicationName.Module.BusinessObjects;

[DefaultClassOptions]
public class Employee : BaseObject {

    public virtual string Name { get; set; }

    private Department department;
    
    public virtual Department Department { get; set; }

    [DataSourceCriteria("Department = '@This.Department'")]
    public virtual Position Position { get; set; }
}
```

# [XPO](#tab/tabid-xpo)

```csharp{15}
public class Employee : BaseObject {
    public Employee(Session session) : base(session) { }

    public string Name {
        get { return GetPropertyValue<string>(nameof(Name)); }
        set { SetPropertyValue<string>(nameof(Name), value); }
    }
    
    [Association("Employee-Department")]
    public Department Department {
        get { return GetPropertyValue<Department>(nameof(Department)); }
        set { SetPropertyValue<Department>(nameof(Department), value); }
    }    
    
    [DataSourceCriteria("Department = '@This.Department'")]
    public Position Position {
        get { return GetPropertyValue<Position>(nameof(Position)); }
        set { SetPropertyValue<Position>(nameof(Position), value); }
    }
}
```

***

Without Current Object Parameter, the filter condition can only compare `Position` properties to constant/predefined values. Conditions may also use [Function Criteria Operators](xref:113307). To define a criterion that uses `Employee` property values, use the Current Object Parameter. Note the string that starts with `\@This` in the example above. 

Now the drop-down List View of the Lookup Property Editor in this example displays only positions that fit the specified criterion:

![|Filtered Lookup Property Editor, DevExpress|](~/images/current-object-parameter-lookup-property-editor-filtered-devexpress.png)

Another example of the Current Object Parameter implementation is available in the _MainDemo.Module_\\_BusinessObjects_\\_Employee.cs_ file of the **MainDemo** application shipped with XAF. 

> [!TIP]
> [!include[MainDemoLocationNote](~/templates/maindemolocationnote111127.md)] The ASP.NET Core Blazor version is available online at https://demos.devexpress.com/XAF/BlazorMainDemo.

The following example specifies a filter condition for the `Employee.Manager` property. The dropdown list only displays employees whose `Position` is "Manager". The Current Object Parameter helps exclude the current employee.

# [EF Core](#tab/tabid-efcore)

```csharp{6}
namespace MainDemo.Module.BusinessObjects;

[DefaultClassOptions]
public class Employee : Person {
    // ...
    [DataSourceCriteria("Position.Title = 'Manager' AND ID != '@This.ID'")]
    public virtual Employee Manager { get; set; }
    // ...
}
```

# [XPO](#tab/tabid-xpo)

```csharp{9}
namespace MainDemo.Module.BusinessObjects;

[DefaultClassOptions]
public class Employee : Person, IMapsMarker {
    // ...
    public Employee(Session session) :
        base(session) { }
    // ...
    [DataSourceCriteria("Position.Title = 'Manager' AND Oid != '@This.Oid'")]
    public Employee Manager {
        get {
            return manager;
        }
        set {
            SetPropertyValue(nameof(Manager), ref manager, value);
        }
    }
    // ...
}
```

***

You can use the Current Object Parameter in the following expressions/conditions:

* The [](xref:DevExpress.Persistent.Base.DataSourceCriteriaAttribute)'s [DataSourceCriteriaAttribute.DataSourceCriteria](xref:DevExpress.Persistent.Base.DataSourceCriteriaAttribute.DataSourceCriteria) property.
* The [](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute)'s [DataSourcePropertyAttribute.DataSourcePropertyIsNullCriteria](xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute.DataSourcePropertyIsNullCriteria) property (for Windows Forms applications only).

[!include[DataSourceCriteria_This](~/templates/datasourcecriteria_this111276.md)]
