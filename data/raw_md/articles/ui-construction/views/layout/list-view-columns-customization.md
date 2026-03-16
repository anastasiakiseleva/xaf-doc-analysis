---
uid: "113679"
seealso:
- linkId: "113285"
- linkType: HRef
  linkId: https://www.youtube.com/watch?v=1Q4xZMSs2BU
  altText: 'DevExpress XAF: Grid Designer for ListView'
title: List View Columns Customization
seealso:
- linkType: HRef
  linkId: https://github.com/DevExpress-Examples/xaf-how-to-sort-a-listview-in-code
  altText: 'GitHub example: XAF - How to sort a ListView in code'
---
# List View Columns Customization

When you implement a persistent object, XAF automatically generates two [List Views](xref:112611) to display this object in the UI – the general List View and Lookup List View. The **Views** | **_ClassName_\_ListView** and **Views** | **_ClassName_\_LookupListView** [Application Model](xref:112580) nodes are where you configure these List View settings. These nodes expose lists of columns (see [IModelListView.Columns](xref:DevExpress.ExpressApp.Model.IModelListView.Columns)). XAF generates the default column set according to rules described in the [List View Column Generation](xref:113285) topic. You can change a column's visibility, width, order, filtering, etc., either at runtime or using the [Model Editor](xref:112582). This topic describes different aspects of List View customization if the [](xref:DevExpress.ExpressApp.Win.Editors.GridListEditor) displays a List View.

* [Design-Time Customization](#design-time-customization)
* [Runtime Customization](#runtime-customization)
* [Freezing Column Indices](#freezing-column-indices)

## Design-Time Customization
Design-time customizations can be performed in the [Model Editor](xref:112582).

To customize a WinForms application, apply the changes at the [Windows Forms application project](xref:118045) level.

Each **ListView** node has a **Columns** child node, providing access to column settings. When the **Columns** node is selected, the property list to the right is replaced with a design surface that imitates the current View's grid and filled with sample data to show how the grid is displayed at runtime. Note that the WinForms Data Grid is displayed at design time. The **Columns** node exposes a tree of nodes (columns available in the current view). Each node provides access to the complete set of column properties.

![GridListEditorDesigner_1](~/images/gridlisteditordesigner_1117544.png)

You can modify the default configuration if it does not meet your requirements. Scale columns by dragging a separator between two column headers, or drag and drop column headers to re-arrange columns. You can hide a column by dragging it outside the table. You can also apply [sorting](xref:827), [grouping](xref:828), and [filtering](xref:829). To show hidden columns, right-click on the table header and select the **Column Chooser**.

![Tutorial_UIC_Lesson16_1](~/images/tutorial_uic_lesson16_1115506.png)

The Customization window is invoked and you can drag the required column from this window to the View, and vice versa. Follow the graphical prompts that show the column's future location.

![Tutorial_UIC_Lesson16_1_2](~/images/tutorial_uic_lesson16_1_2117540.png)

You can use the **Add…** and **Remove** buttons to manage the properties displayed in the **Customization** window. To display a property that is not in the list (for instance, a referenced object's property or [custom field](xref:113583)), click **Add…**, and in the **Object Model** window, choose the required property and click **Add**. The property now appears in the **Customization** window, and you can add it to the grid as described above.

![GridListEditorDesigner_4](~/images/gridlisteditordesigner_4117550.png)

If you need to [apply a summary](xref:830), select the **ListView** node, set its `IsFooterVisible` property to `True`, then select **ListView** | **Columns** node. The footer now displays in the List View, and you can add the required summaries to it.

![GridListEditorDesigner_6](~/images/gridlisteditordesigner_6117552.png)

In addition to the capability to visually configure columns, the following customizations are available using the **Columns** node's child nodes:

* **Show, hide and reorder columns** 
	
	The **Columns**' child nodes have the `Index` property. Use this property to set the column order. A negative value hides the corresponding column.
* **Group columns**
	
	Set a column's `GroupIndex` property to a non-negative integer value. This value indicates the column's position within the group column collection. The `GroupIndex` property value determines the grouping level. For instance, if the index is 0, rows are grouped against this column first and then against the column groups that follow. Set the column's `GroupIndex` property to -1 to ungroup a row by a specific column.
* **Edit caption**
	
	Assign a string to a column's `Caption` property. This string is displayed as the column name.

For more information about available customizations, refer to the [](xref:DevExpress.ExpressApp.Model.IModelColumn) members list.

> [!TIP]
> You can arrange columns into logical groups (bands). Refer to the [List View Bands Layout](xref:113695) topic for more details.

> [!NOTE]
> The changes you make in the Model Editor invoked for a module project (application project) are saved to the _Model.DesignedDiffs.xafml_ (_Model.xafml_) file located in this module project. These changes replace the previous values when you run the application. Make sure that values from other _*.xafml_ files do not replace your values. To do this, review the _*.xafml_ files that are loaded after your _*.xafml_ file, including the _Model.User.xafml_, generated at runtime. For details on the layer structure of the Application Model, refer to the [Application Model Basics](xref:112580) topic.

## Runtime Customization

### ASP.NET Core Blazor

Use the grid's context menu to customize List View columns.

![|XAF ASP.NET Core Blazor Grid List Editor Designer, DevExpress](~/images/xaf-blazor-grid-header-context-menu-devexpress.png)

Use the **Reset View Settings** Action from the grid row context menu to undo all runtime customizations in the current List View.

![|XAF ASP.NET Core Blazor Reset View Settings in List View, DevExpress](~/images/blazor-reset-view-settings-action.png)

#### Column Chooser

To add new columns, use the **Column Chooser** option.

You can customize the options available in the Column Chooser itself. In the invoked **Column Chooser** window, click the **Customize** button to open the **Object Model** dialog window where you can select items that you want to hide or display in the **Column Chooser**.

![XAF ASP.NET Core Blazor Column Chooser, DevExpress](~/images/xaf-blazor-columnchooser-customize-devexpress.png)

> [!TIP]
> * To enable or disable column chooser windows for the entire application, use the [IModelOptions.CustomizationFormEnabled](xref:DevExpress.ExpressApp.Model.IModelOptions.CustomizationFormEnabled) property.
> * To enable or disable a column chooser for a specific View, use the [IModelView.CustomizationFormEnabled)](xref:DevExpress.ExpressApp.Model.IModelView.CustomizationFormEnabled) property.

[!include[disableobjectmodelcontroller](~/templates/disableobjectmodelcontroller.md)]

[!include[customizemodelobjectdialog](~/templates/customizemodelobjectdialog.md)]

### Windows Forms

Windows Forms runtime customization capabilities are the same as in the [Model Editor](xref:112582)'s **ListView** | **Columns** node. For more information, refer to the [Design-Time Customization](#design-time-customization) section in this topic.

![XAF Windows Forms Grid List Editor Designer, DevExpress](~/images/gridlisteditordesigner_2117545.png)

## Freezing Column Indices

If you have configured columns for a business class List View, and then added or removed the class's public properties, the column set automatically changes, and you may need to reconfigure it. However, you can "lock" customizations by setting the **ListView** node's `FreezeColumnIndices` property to `True`. In this case, the current column index state is copied to the model differences, and any changes on previous layers are ignored. Columns that are subsequently generated are hidden. Setting the `FreezeColumnIndices` property back to `False` resets the column configuration to the generated configuration.

![GridListEditorDesigner_5](~/images/gridlisteditordesigner_5117551.png)