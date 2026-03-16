---
uid: "112612"
seealso:
- linkId: "113189"
- linkId: "113610"
- linkId: "120092"
title: View Items and Property Editors
owner: Ekaterina Kiseleva
---
# View Items and Property Editors

[Dashboard Views and Detail Views](xref:112611) consist of View Items - abstract UI entities represented by [](xref:DevExpress.ExpressApp.Editors.ViewItem) class descendants. To create actual controls, each item type overrides the protected **CreateControlCore** method, called when an item needs to be displayed in a UI. WinForms-specific View Items are supplied in the **DevExpress.ExpressApp.Win** assembly.

XAF provides the following basic View Item types:

{|
|-

! Item Type
! Description
|-

| [](xref:DevExpress.ExpressApp.Editors.ActionContainerViewItem)
| Displays an [Action Container](xref:112610) specified by the [IModelActionContainerViewItem.ActionContainer](xref:DevExpress.ExpressApp.Model.IModelActionContainerViewItem.ActionContainer) property of the [Application Model](xref:112580)'s corresponding **ActionContainerViewItem** node. Used to display [Actions](xref:112622) on a Detail View layout.

**Tutorial**: [How to: Include an Action to a Detail View Layout](xref:112816)
|-

| [](xref:DevExpress.ExpressApp.Layout.ControlViewItem)
| Displays a control specified by the [IModelControlDetailItem.ControlTypeName](xref:DevExpress.ExpressApp.Model.IModelControlDetailItem.ControlTypeName) property of the [Application Model](xref:112580)'s corresponding **ControlDetailItem** node (see [How to: Show a Custom Data-Bound Control in an XAF View (WinForms)](xref:114159)). You can specify a control that is displayed in the UI.
|-

| `DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem`
| Displays a control specified by the [IModelControlDetailItem.ControlTypeName](xref:DevExpress.ExpressApp.Model.IModelControlDetailItem.ControlTypeName) but can also display any parameter-less [Razor component](https://learn.microsoft.com/en-us/aspnet/core/blazor/components/). The Component can access `CascadingParameter` of the `DevExpress.ExpressApp.Blazor.Editors.BlazorControlViewItem` type to access the `View`, `ObjectSpace`, and `Application` instances.
|-

| [](xref:DevExpress.ExpressApp.Editors.DashboardViewItem)
| Displays a [View](xref:112611) in a nested [Frame](xref:112608). Used to display several Views side-by-side on a Dashboard View.
|-

| [](xref:DevExpress.ExpressApp.Editors.PropertyEditor)
| Displays an editor control bound to a property. There are multiple property editor types in XAF. They are intended for different data types, and therefore use different controls. For example:

* [ListPropertyEditor](xref:113568) - Displays a collection property in a nested List View.
* [DetailPropertyEditor](xref:113572) - Displays a reference property in a nested Detail View.

More Property Editors intended for various property types are listed in the [Data Types Supported by built-in Editors](xref:113014) section.
|-

| [](xref:DevExpress.ExpressApp.Editors.StaticImage)
| Displays an image.
|-

| [](xref:DevExpress.ExpressApp.Editors.StaticText)
| Displays a label.
|}

## Customize View Items

You can use the following approaches to customize View Items:

* [Access and Customize View Items in Code](#access-and-customize-view-items-in-code)
* [Customize the Application Model](#customize-the-application-model)
* [Create Custom View Items](#create-custom-view-items)

### Access and Customize View Items in Code

You can use the following approaches to access or customize View Items:

* [](xref:402154)
* [How to: Access the Dashboard Control](xref:117454)
* [How to: Access the Master Object from a Nested List View](xref:113161)
* [How to: Customize a Built-in Property Editor (WinForms)](xref:113104) 
* [How to: Disable and Hide Property Editors Based on a Business Rule](xref:113221)
* [How to Implement Dependent Views in a Dashboard View Filter Based on Selection](https://github.com/DevExpress-Examples/xaf-how-to-implement-dependent-views-in-a-dashboardview-filter-based-on-selection)
* [Validate a Property Editor Value](xref:113251)
* [](xref:404428)
* [Secure or Protect a Property Editor Value](xref:113366)
* [Ways to Access UI Elements and Their Controls](xref:120092)

### Customize the Application Model

The [Application Model](xref:112580) displays nodes for all View Items in your application. You can use the Application Model to customize View Items.

* **ViewItems** node
	
	This node has child nodes that correspond to the basic View Item types. These View Items are used to construct Detail Views. Examples of these base types are Static Text, Static Image, Property Editor, etc. Each base type is actually represented in the UI by a particular descendant class. This descendant is specified via the **DefaultItemType** property. If there are multiple descendants available, you can select the desired class via the property's drop-down list.
	
	Since different data types require different Property Editors, the PropertyEditors node supplies child nodes corresponding to data types. These child nodes specify the default Property Editor for each data type, using the EditorType property.
	
	The following picture illustrates the **ViewItems** node:
	
	![DetailViewItemsNode](~/images/detailviewitemsnode115383.png)
* **Views** | **DashboardView** or **DetailView** | **Items** node
	
	This node lists the current Detail View's items. By default, it contains only Property Editor nodes. Their **PropertyEditorType** property specifies the Property Editor type used in a UI. Of course, you can change the default property value by selecting another property editor type from the dropdown list.
	
	![DetailView_ItemsNode](~/images/detailview_itemsnode117040.png)

	You can change other properties such as [DisplayFormat](xref:DevExpress.ExpressApp.Editors.PropertyEditor.DisplayFormat), [EditMask](xref:DevExpress.ExpressApp.Editors.PropertyEditor.EditMask) etc. See [](xref:402141).
	
	You can also add other View Items to a Detail View. To do this, use the [Model Editor](xref:112582)'s context menu. If you add a Static Text, Static Image or Control item, you can use the **ItemType** property to specify the actual class used to represent this item in a UI.
* **Views** | **DashboardView** or **DetailView** | **Layout** node.
	
	This node specifies the layout of the current View's items. Items can be grouped or located separately. You can change the default layout, by using the context menu and specifying property values in the Model Editor. In addition, the Model Editor allows you to view the resulting items layout. When the Layout node is selected, the property list to the right is displayed with a design surface that emulates the current View. To drag the View Items, right-click on the empty space, and select **Customize Layout**. The Customization form will be invoked. Close this form, to go back to the view mode of the emulated View.
	
	![Tutorial_UIC_Lesson21_1](~/images/tutorial_uic_lesson21_1115630.png)
	
	For details, refer to the [View Items Layout Customization](xref:112817) topic.

### Create Custom View Items

You can use a custom View Item if XAF's built-in View Items do not meet your requirements. The following articles describe how to create a View Item and use it to implement additional functionality: 

* [](xref:113610)
* [Implement Custom Property Editors](xref:113097)
* [How to: Add a Button to a Detail View Using a Custom View Item](xref:113653)
* [How to: Implement a Property Editor Based on a Custom Control (WinForms)](xref:112679)
* [How to: Implement a Property Editor Using a DevExpress WinForms Control](xref:113015)
* [](xref:405483)
* [How to: Create a Custom Control Detail Item](xref:113652)
* [How to: Include an Action to a Detail View Layout](xref:112816)
* [](xref:404698)
* [How to: Show a Custom Data-Bound Control in an XAF View (WinForms)](xref:114159)
* [How to Access XafApplication and IObjectSpace from a Custom View Item](xref:DevExpress.ExpressApp.Editors.IComplexViewItem)


> [!NOTE]
> You can find built-in View Items from XAF libraries in the **Model Editor** invoked for a Windows Forms application project, since the **DevExpress.ExpressApp.Win** assembly is referenced in Windows Forms application projects.
