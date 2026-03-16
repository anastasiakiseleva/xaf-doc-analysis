---
uid: "402979"
title: Implement Dependent Reference Properties
owner: Alexey Kazakov
seealso:
  - linkId: "4928"
  - linkId: "112998"
---
# Implement Dependent Reference Properties

This lesson explains how to implement properties whose values depend on other properties. 

For this purpose, add a new `Manager` property to the `Employee` class. The editor for this property displays a list of managers who work in the same department.

> [!NOTE]
> Before you proceed, take a moment to review the previous lessons:
> 
> * [](xref:402981)
> * [](xref:402978)
> * [](xref:402984)

## Step-by-Step Instructions

1. Add the new `Manager` property to the `Employee` class:
    
    ```csharp{5}
    using DevExpress.ExpressApp.DC;
    //...
    public class Employee : BaseObject {
        //...
        public virtual Employee Manager { get; set; }
    }
    ```    
2. Apply the `DataSourceProperty` and `DataSourceCriteria` attributes to the newly added property:
    
    ```csharp{5}
    using DevExpress.ExpressApp.DC;
    //...
    public class Employee : BaseObject {
        //...
        [DataSourceProperty("Department.Employees", DataSourcePropertyIsNullMode.SelectAll), DataSourceCriteria("Position.Title = 'Manager'")]
        public virtual Employee Manager { get; set; }
    }
    // ...
    ```
    [`DataSourceProperty`]: xref:DevExpress.Persistent.Base.DataSourcePropertyAttribute
    [`DataSourceCriteria`]: xref:DevExpress.Persistent.Base.DataSourceCriteriaAttribute

   In this code, the `DataSourceProperty` attribute accepts two parameters: `dataSourceProperty` and `mode`.
   
   The `dataSourceProperty` parameter is a string value that specifies the name of the collection property used as the data source for a List View displayed in a Lookup Property Editor. In this tutorial, you set this parameter to `"Department.Employees"`.
   
   The `mode` parameter is optional. It specifies how the lookup items are populated if the application could not find any items from the path. In this tutorial, you set it to [](xref:DevExpress.Persistent.Base.DataSourcePropertyIsNullMode.SelectAll).
   
   You can also set it to [](xref:DevExpress.Persistent.Base.DataSourcePropertyIsNullMode.SelectNothing) or [](xref:DevExpress.Persistent.Base.DataSourcePropertyIsNullMode.CustomCriteria). In the latter case, you also have to use the `DataSourcePropertyIsNullCriteria` parameter to specify criteria to filter the List View by the target property's Lookup Property Editor.

   The `DataSourceCriteria` attribute restricts the **Manager** lookup editor items to specific objects. With the `"Position.Title = 'Manager'"` filter, the lookup editor displays only the `Employee` objects whose `Position` property value is `"Manager"`.
    
3. Run the application and make the following changes:

   * Add a **Department** object (for example, "Development").
   * Add multiple **Position** objects (for example, "Manager", "Developer", "QA").
   * Add multiple **Employee** objects with the **Department** property set to "Development".
   * Set the **Position** property of two **Employee** objects to "Manager".
   * Set the **Position** property of the remaining **Employee** objects to "Developer".

4. Create a new `Employee` object. In the **Employee** Detail View, specify the `Department` property and expand the **Manager** lookup editor. Notice that it only shows the managers from the specified department.

   ASP.NET Core Blazor
   
   :   ![|ASP.NET Core Blazor filtered lookup editor items|](~/images/btutorial_bmd_department_dependent_properties.png)

   Windows Forms

   :   ![|Windows Forms filtered lookup editor items|](~/images/department-manager-dependency-winforms.png)

>[!TIP]
> You can use integrated XAF designers to implement the same behavior without code. For details, refer to the following article: [](xref:112681).

## Next Lesson

[](xref:404195)
