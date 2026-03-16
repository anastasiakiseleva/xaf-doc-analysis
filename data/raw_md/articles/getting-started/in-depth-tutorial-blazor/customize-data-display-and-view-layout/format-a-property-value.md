---
uid: "402141"
title: Format a Property Value
owner: Alexey Kazakov
seealso: []
---
# Format a Property Value

This lesson explains how to format an entity class property and specify its [input mask](xref:583) settings. 

The instructions below describe how to customize the display format for the `Task.StartDate`, `Task.DueDate`, and `Task.PercentCompleted` properties.

> [!NOTE]
> Before you proceed, take a moment to review the previous lessons:
> 
> * [](xref:402981)
> * [](xref:402145)

## Step-by-Step Instructions

1. In the **MySolution.Module** project, open the _Model.DesignedDiffs.xafml_ file in the [Model Editor](xref:112582).
2. Navigate to the **BOModel** | **MySolution.Module.BusinessObjects** | **DemoTask** | **OwnMembers** node.
3. For the **DueDate** and **StartDate** child nodes, set the [DisplayFormat](xref:DevExpress.ExpressApp.Editors.PropertyEditor.DisplayFormat) property value to `D` (the long date pattern).

   ![|Date-time mask display format|](~/images/tutorial_uic_datetime_mask.png)

   Note that the `EditMask` property value is `d` (the short date pattern).

4. For the **PercentCompleted** child node, set the `DisplayFormat` property to `{0:N0}%`.
	
   ![|Percent integer display format|](~/images/tutorial_uic_integer_display_format.png)

5. Run the application. Invoke a Detail List for any **Task** object.

   ASP.NET Core Blazor
	
   :   ![|Property editor input masks in ASP.NET Core Blazor|](~/images/blazor-tutorial-editmask-display-format.gif)

   Windows Forms

   :   ![|Property editor input masks in Windows Forms|](~/images/blazor-tutorial-editmask-display-format-winforms.gif)
   
Note how the text format changes when **StartDate** and **DueDate** editors receive or lose focus. If you focus an editor, its `EditMask` property takes effect (the `d` value corresponding to the short date pattern). If the editor loses focus, its `DisplayFormat` property has priority (the `D` value corresponding to the long date pattern).
   
The value displayed in the **Percent Completed** property editor includes the percentage sign ('%').

## Global Default Format

In ASP.NET Core Blazor and Windows Forms applications, you can specify the default format for all properties of one type, for example, `System.Decimal` or `System.DateTime`.

Open the Application Model of a platform-specific project, navigate to the corresponding child node of the **ViewItems** | **Property Editors** node, and specify the [IModelRegisteredPropertyEditor.DefaultDisplayFormat](xref:DevExpress.ExpressApp.Editors.IModelRegisteredPropertyEditor.DefaultDisplayFormat) property value.

## Global Default Edit Mask

In ASP.NET Core Blazor applications, you can specify the default edit mask for all properties of one type.

Open the Application Model of a platform-specific project and navigate to the corresponding child node of the **ViewItems** | **Property Editors** node. Specify the [IModelRegisteredPropertyEditor.DefaultEditMask](xref:DevExpress.ExpressApp.Editors.IModelRegisteredPropertyEditor.DefaultEditMask) property value.

You can localize the [IModelRegisteredPropertyEditor.DefaultDisplayFormat](xref:DevExpress.ExpressApp.Editors.IModelRegisteredPropertyEditor.DefaultDisplayFormat) and [IModelRegisteredPropertyEditor.DefaultEditMask](xref:DevExpress.ExpressApp.Editors.IModelRegisteredPropertyEditor.DefaultEditMask) properties. Note that the values you specify for them in localization resources override the corresponding values from satellite assemblies in any culture except "en-US".

[!include[net5-currency-symbol-note](~/templates/currency-symbol-note.md)]

## Next Lesson

[](xref:403184)
