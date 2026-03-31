---
uid: "404203"
title: Enable Split Layout in a List View
---

# Enable Split Layout in a List View

This lesson explains how to enable a Split Layout in a List View.

The Detail View opens when you select an object from the List View. In ASP.NET Core Blazor applications, this Detail View replaces the List View. In Windows Forms applications, XAF renders a new window.

The instructions below explain how to show the Detail View of the selected `Department` object alongside the `Department` List View.

## Step-by-Step Instructions

1. In the _MySolution.Module_ project, open the _Model.DesignedDiffs.xafml_ file in the [Model Editor](xref:112582). Navigate to the **Views** | **MySolution.Module.BusinessObjects** | **Department** | **Department_ListView** node. Set the **MasterDetailMode** property of this node to `ListViewAndDetailView`.

   ![|Split View activation in Model Editor|](~/images/blazor-tutorial-masterdetailmode-property.png)

2. Run the application. Open the **Department** List View and select an object to see the object's Detail View in the same window:

   ASP.NET Core Blazor

   :   ![|Split View in ASP.NET Core Blazor](~/images/blazor-tutorial-department-splitview-blazor.png)

   Windows Forms:

   :   ![Split View in Windows Forms](~/images/blazor-tutorial-department-splitview-winforms.png)

   The Detail View is context-sensitive and its content depends on the selected `Department` object.

> [!TIP]
>
> To specify the Detail View that appears alongside the List View, use the [](xref:DevExpress.ExpressApp.Model.IModelListView.MasterDetailView) property.
> To customize the Detail View location, use the [](xref:DevExpress.ExpressApp.Model.IModelSplitLayout.Direction) and [](xref:DevExpress.ExpressApp.Model.IModelListViewSplitLayout.ViewsOrder) properties of the **\<Class\>_ListView** | **SplitLayout** node.

## Next Lesson

[](xref:404202)