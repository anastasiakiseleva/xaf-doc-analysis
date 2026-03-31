---
uid: "112817"
seealso:
- linkId: "113335"
- linkType: HRef
  linkId: https://supportcenter.devexpress.com/ticket/details/q514530/how-to-change-a-detailview-editor-or-listview-column-caption-dynamically
  altText: How to Change a Detail View Editor or List View Column Caption Dynamically
title: Detail View Layout Customization
---
# Detail View Layout Customization


XAF allows you to customize the generated application layout using one of the following methods.


## Design-Time Customization

You can customize View layout in the [Model Editor](xref:112582). The **DashboardView** and **DetailView** nodes have a **Layout** child node, which allows you to access to the layout settings. 

When the **Layout** node is selected, the Model Designer displays a design surface that imitates the current View. This design surface allows you to see how the View will be displayed at runtime. The **Layout** node exposes a tree of nodes that comprises groups, tabbed groups, layout items, labels, separators, etc.

![Tutorial_UIC_Lesson21_1](~/images/tutorial_uic_lesson21_1115630.png)

To modify a default View Items layout, right-click on an empty space and choose **Customize Layout**. This will invoke the Customization form allowing you to drag View Items where required. The graphical prompts will display the item's target position.

![Tutorial_UIC_Lesson21_2](~/images/tutorial_uic_lesson21_2115631.png)

In the Model Designer, you can remove and restore View Items by dragging the required items from the View to the **Customization** form, and vice versa.

To see the View Items layout tree, use the **Layout Tree View** tab on the **Customization** form. Invoke the context menu for additional customization options.

![Tutorial_UIC_Lesson21_3](~/images/tutorial_uic_lesson21_3115632.png)

For more information about the **Customization** form, the Layout Tree View tab, and its context menu, refer to the following article: [Default Runtime Customization](xref:2307).

In the Layout node's child nodes, you can find the following customization options:

* **Reorder Layout Groups and Layout Items** 
	
	The LayoutGroup, TabbedGroup and LayoutItem nodes have the **Index** property. Use this property to set the order within specific levels, Layout Groups or Layout Items.
* **Modify a Caption**
	
	Specify whether a caption is displayed for a Layout Group, Tabbed Group or Layout Item using the **ShowCaption** property.
	
	Specify a Caption for a group or item if you have made it visible. To do this, use the **Caption** property.
	
	Specify the location of a group or item caption using the **CaptionLocation** property.
* **Specify the direction of nested Layout Groups or Layout Items**
	
	Specify whether the groups (or items) within one level are arranged consecutively from left to right or from top to bottom. To do that, use the Layout Group's **Direction** property.
* **Move a Layout Item to another Layout Group**
	
	Use the drag-and-drop operation to move a Layout Item to the desired Layout Group.

You can add new items to a Detail View. Right-click the **DetailView** | **Items** node, navigate to the **Add…** group, choose the required **View Item** type and customize the newly added item as needed.

![Tutorial_UIC_Lesson15_0](~/images/tutorial_uic_lesson15_0116423.png)

After the new item is added, put it on the Detail View as described above.

If you require layout customizations to affect all application platforms (WinForms and ASP.NET Core Blazor), adjust the layout at the Module Project level. To customize an application for a specific platform, adjust the layout at the corresponding project level. Refer to the [Application Solution Structure](xref:118045) article for additional information.

> [!NOTE]
> * **Splitter**, **Separator**, and **Label** items are specific to the DevExpress WinForms Layout Control. These items are not available in the Model Editor invoked for an ASP.NET Core Blazor or platform-independent project. They are also not available in the **Customization** form or in the **LayoutGroup** node's **Add…** context menu. This behavior protects you from errors during layout customization. Add and customize these items (splitter, separator, label) in WinForms projects only.
> * Several WinForms-specific properties are not available in the Model Editor invoked for an ASP.NET Core Blazor or platform-independent project.
> 	
> 	* **LayoutGroup** node's [IModelWinLayoutGroup.TextAlignMode](xref:DevExpress.ExpressApp.Win.SystemModule.IModelWinLayoutGroup.TextAlignMode) property
> 	* **LayoutItem** node's [IModelWinLayoutItem.TextAlignMode](xref:DevExpress.ExpressApp.Win.SystemModule.IModelWinLayoutItem.TextAlignMode) property
> 	* **LayoutItem** node's [IModelLayoutItem.SizeConstraintsType](xref:DevExpress.ExpressApp.Model.IModelLayoutItem.SizeConstraintsType) property
> 	
> 	Perform the customization of these properties at the WinForms project level. For more information about the size constraints for WinForms controls, refer to the following topic: [Size and Alignment](xref:17574).

The changes that you perform in the Model Editor invoked for a module (application project) are saved to the _Model.DesignedDiffs.xafml_ (_Model.xafml_) file located in this module project. These changes will rewrite previous values when you run the application. It is important for you to ensure that values from other _*.xafml_ files will not rewrite your values. To do this, review the _*.xafml_ files that are loaded after your _*.xafml_ file, including the _Model.User.xafml_ generated at runtime. For details on the layer structure of the Application Model, refer to the [Application Model Basics](xref:112580) topic.

### General Layout Settings

A number of layout options that affect all Views are available in the Model Editor's **Options** | **LayoutManagerOptions** node. For example, you can disable the colon sign that is added to item captions using the [IModelLayoutManagerOptions.EnableCaptionColon](xref:DevExpress.ExpressApp.Model.IModelLayoutManagerOptions.EnableCaptionColon) property, or use a custom separator instead of a colon (see [IModelLayoutManagerOptions.CaptionColon](xref:DevExpress.ExpressApp.Model.IModelLayoutManagerOptions.CaptionColon).)


## DetailViewLayout Attribute
You can customize the Detail View's default layout in a business class code using the [](xref:DevExpress.ExpressApp.Model.DetailViewLayoutAttribute) applied to required properties.

```csharp
[DetailViewLayoutAttribute("NotesAndRemarks", LayoutGroupType.TabbedGroup, 100)]
public string Notes { get; set; }
```

Refer to this attribute description to see more examples.

## Runtime Customization

### In the Model Editor

This feature is available in XAF Windows Forms applications only. You can make changes to a Detail View's layout as described in the [Design Time Customization](#design-time-customization) section above.

To invoke the Model Editor, use the **EditModel** Action in the root window's **Tools** main menu. The **EditModel** Action is available when a user has permission to customize the Application Model. For additional information about permissions, refer to the following topic: [Edit Model Permission](xref:404633#edit-model-permission).

### In Customization Mode

This feature is available in XAF [ASP.NET Core Blazor](xref:404353) and [Windows Forms](xref:2307) applications.

To enter customization mode, right-click an empty space in the Detail View you want to edit and select the **Customize Layout** option in the context menu.

ASP.NET Core Blazor
:   ![|Customize Layout In a Detail View of an XAF ASP.NET Core Blazor Application, DevExpress|](~/images/xaf-blazor-detail-view-customization-mode-activation-devexpress.png)

    ![|Customization Form In a Detail View of an XAF ASP.NET Core Blazor Application, DevExpress|](~/images/xaf-blazor-detail-view-customization-form-devexpress.png)

Windows Forms
:   ![Layout_DetailView](~/images/xaf-winforms-detail-view-customization-mode-activation-devexpress.png)

    ![Layout_CustomizationForm_DetailView](~/images/xaf-winforms-detail-view-customization-form-devexpress.png)

> [!TIP]
> * To enable or disable runtime layout customization for the entire application, use the [IModelOptions.CustomizationFormEnabled](xref:DevExpress.ExpressApp.Model.IModelOptions.CustomizationFormEnabled) property.  
> * To enable or disable runtime layout customization for a specific View, use the [IModelView.CustomizationFormEnabled)](xref:DevExpress.ExpressApp.Model.IModelView.CustomizationFormEnabled) property.
> * You can also use the [](xref:DevExpress.Persistent.Base.HideInUI) attribute to control any property's visibility in a UI View.

XAF uses the Application Model to save layout changes made at runtime. The next time you invoke a customized View, the View shows the most recent changes. If you need to roll back the changes, right-click an empty space in the View at runtime and select the **Reset Layout** option in the context menu. In Windows Forms applications, you can also use the **ResetViewSettings** Action.

For more information on how XAF stores Application Model changes in different applications, refer to the following topic: [Application Model Differences: Storage Types](xref:112580#application-model-differences-storage-types).

> [!NOTE]
> For more information about customization mode in Windows Forms applications, refer to the following topic: [](xref:2307).
>
> For more information about customization mode in ASP.NET Core Blazor applications, refer to the following topic: [](xref:404353).

## Important Notes
The following are important notes concerning Layout Items.

1. When you add a new property and thus make a change to the [business class](xref:113664) structure you created at the start of this XAF application, the Detail View's layout of the business class is programmed to automatically regenerate. If this occurs, all your layout customizations are discarded. To prevent this, set the [IModelDetailView.FreezeLayout](xref:DevExpress.ExpressApp.Model.IModelDetailView.FreezeLayout) property to `true`. This allows you to retain the Detail View's layout according to the last saved changes, and prohibit regeneration. However, you need to add new layout items to your Detail View layout if you use this property.
	
	![Layout_FreezeLayout](~/images/layout_freezelayout116768.png)
	
	If you set the [IModelDetailView.FreezeLayout](xref:DevExpress.ExpressApp.Model.IModelDetailView.FreezeLayout) property to `true`, then the Model Editor copies the current state of the layout to the currently edited [Application Model](xref:112580) layer. Note that you can still remove a child node from the **Items** child node of the **DetailView** node. In this instance, however, it is impossible to retain a frozen layout. The [View Item](xref:112612) corresponding to the removed node is replaced by an empty space item in the [Detail View](xref:112611). Setting the **FreezeLayout** property to `false` is analogous to executing the [Model Editor](xref:112582)'s "Reset Differences" command that reverts all customizations to their original default state.
	
	[!include[FreezeLayoutWarning](~/templates/freezelayoutwarning11127.md)]
2. In Windows Forms application, the width of a Layout Item is not locked by default. XAF calculates the width based on the parent Layout Group's dimensions. Thus, Layout Items from different Layout Groups may have different alignment.
	
	![Layout_GroupAlignment](~/images/layout_groupalignment116679.png)
	
	Place Items in the same Group to keep them aligned.
3. In Windows Forms applications, if you move a Layout Item to a higher-level group, additional spacing between the Item moved and the next Item appears. See the image below.
	
	![Layout_GroupSpacing](~/images/layout_groupspacing116678.png)
	
	If you wish to keep equal spacing between Items, keep them in the same Group.
4. Items and nested Groups inside each Group can be arranged either vertically or horizontally (see [IModelLayoutGroup.Direction](xref:DevExpress.ExpressApp.Model.IModelLayoutGroup.Direction)). The following image illustrates a layout fragment with complex nesting.
	
	![Layout_GroupDirection](~/images/layout_groupdirection116680.png)
	
	All components within the same group have the same orientation, as shown by dual arrows. To arrange two groups horizontally and form two columns of Items, you must put these two groups into another group. This process is called wrapping. Extra wrapping groups are created automatically when you drag items on the Layout design surface. Autogenerated wrapping groups usually have a random ID with the "Auto" prefix, except in ASP.NET Core Blazor apps where they are named "Group" with an optional number after.
5. In Windows Forms applications, if you move or hide a Layout Item, its Layout Group stays on the form. In the image below, the "Notes" Item moves from the "Notes" to the "Photo" group.
	
	![Layout_EmptyGroup](~/images/layout_emptygroup116677.png)
	
	The "Notes" Group is now empty. This empty Layout Group may interfere with your layout and you may need to remove it. You can also use the [IModelWinLayoutManagerOptions.InvisibleGroupVerticalDistance](xref:DevExpress.ExpressApp.Win.SystemModule.IModelWinLayoutManagerOptions.InvisibleGroupVerticalDistance) property to specify how the empty group affects vertical space between visible items.
6. The Application Model's **Options** node contains the **LayoutManagerOptions** child node. As the name implies, this node's properties allow you to customize certain settings concerning layout generation.
	
	![Layout_LayoutManagerOptionsNode](~/images/layout_layoutmanageroptionsnode116681.png)
	
	> [!NOTE]
	> The **LayoutManagerOptions** node exposes several WinForms specific properties (see the [](xref:DevExpress.ExpressApp.Win.SystemModule.IModelWinLayoutManagerOptions) interface's members list). Perform the customizations of these properties at the WinForms project level.

For more information about the **Layout Control** and Layout Items, refer to the following topic: [Layout Manager](xref:3406).
