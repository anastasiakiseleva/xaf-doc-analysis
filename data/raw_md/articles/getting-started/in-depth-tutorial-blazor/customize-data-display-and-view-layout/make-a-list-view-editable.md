---
uid: "404202"
title: Make a List View Editable
---
# Make a List View Editable

This lesson explains how to make a List View editable.

The instructions below show how to create new objects of the `DemoTask` type directly in the **Task** List View.

## Step-by-Step Instructions

1. In the _MySolution.Module_ project, open the _Model.DesignedDiffs.xafml_ file in the [Model Editor](xref:112582). Navigate to the **Views** | **MySolution.Module.BusinessObjects** | **DemoTask** | **DemoTask_ListView** node. Set the **AllowEdit** property of this node to `True`.
	
	When the application renders a List View in edit mode, you can create new objects directly in the List View. To add this functionality, set the **NewItemRowPosition** property to `Top` or `Bottom`.
	
	![|Enable edit mode for List View in Model Editor|](~/images/tutorial_uic_lesson18_1115510.png)
	
2. Run the application and edit one of the **Task** objects in the List View:

   ASP.NET Core Blazor
	
   :   ![|Editable List View in ASP.NET Core Blazor](~/images/blazor-tutorial-editable-listview-result-blazor.png)

       To show property editors in a grid row, click the **Edit** button in that row.

       To create a new object in this List View, click the **New** button in the grid header.

   Windows Forms

   :   ![Editable List View in Windows Forms](~/images/blazor-tutorial-editable-listview-result-winforms.png)

   To create a new object in this List View, click the empty row directly below the grid header.

> [!TIP]
> * List Views in DataView, ServerView, and InstantFeedbackView [data access modes](xref:113683) do not support this functionality.
> * To enable the edit mode for a List View in code, add the [](xref:DevExpress.ExpressApp.DefaultListViewOptionsAttribute) attribute to the `DemoTask` class.

## Next Lesson

[](xref:402153)