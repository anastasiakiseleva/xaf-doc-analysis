---
uid: "403248"
title: 'Group List View Data'
---
# Group List View Data

This lesson explains how to group the **Employee** List View data by department and position.

> [!NOTE]
> Before you proceed, take a moment to review the previous lessons:
> * [Place an Action in a Different Location](xref:402145)

## Step-by-Step Instructions

1. Open the _Model.DesignedDiffs.xafml_ file in the [Model Editor](xref:112582).

2. Click the **Views** | **MySolution.Module.BusinessObjects** | **Employee** | **Employee_ListView** | **Columns** node to open the **Grid List Editor Designer**. Right-click the table header and select the **Show Group By Box** item.

   ![|Show Group By Box|](~/images/blazor-tutorial-show-group-box.png)

3. The **Group Panel** appears above the column headers. 

   ![|Group Panel|](~/images/blazor-tutorial-show-group-panel.png)

4. Drag the **Department** and **Position** column headers to the **Group Panel**. Note that multiple columns in the group area create nested groups. 

   ![Group Panel with columns](~/images/blazor-tutorial-show-group-columns.gif)

   When you add a column to the **Group Panel**, the column's `GroupIndex` property value changes. You can also directly specify a column's `GroupIndex` property to group List View data. See the following topic for more information: [List View Columns Customization](xref:113679).   

5. Run the application. The **Employee** List View displays objects grouped by the **Department** and **Position** properties. You can see the **Group Panel** above the grid:

   ASP.NET Core Blazor
    
   :   ![|The grouped Employee List View in ASP.NET Core Blazor|](~/images/blazor-tutorial-show-group-result-blazor.png)

   Windows Forms:

   :   ![The grouped Employee List View in Windows Forms](~/images/blazor-tutorial-show-group-result-winforms.png)

> [!NOTE]
>
> Users can drag columns to and from the **Group Panel** to group and ungroup the List View objects.
> You can hide the **Group Panel** to prevent users from changing groups. Navigate to the **Views** | **MySolution.Module.BusinessObjects** | **Employee** | **Employee_ListView** node and set its **IsGroupPanelVisible** property to `False`.

## Next Lesson

[](xref:404203)
