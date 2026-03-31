---
uid: "113680"
seealso:
- linkId: "112817"
- linkId: "113285"
title: Detail View Layout Generation
---
# Detail View Layout Generation

The XAF automatically generates all Dashboard Views and Detail Views according to the Application Model information. There are certain rules used to generate a default layout that minimize required customizations. These rules are described in this topic.

To generate Dashboard Views and Detail Views, XAF uses the information stored in the [Application Model](xref:112580)'s **Views** | **DashboardView** and **DetailView** nodes. These nodes have two child nodes:

* **Items** is used to populate the [CompositeView.Items](xref:DevExpress.ExpressApp.CompositeView.Items) collection.
* **Layout** is used by the View's Layout Manager to arrange the Layout Items created for each item from the **Items** collection.

The following image demonstrates both the **Items** and **Layout** nodes.

![Layout_ModelEditor](~/images/layout_modeleditor115600.png)

## Detail View Layout Generation Rules

* XAF generates a Layout Item for each View Item form in the **Items** node. Note that the **Items** node only contains [Property Editors](xref:112612) by default (for more information, refer to the following topic: [Business Model in the Application Model](xref:112580)). XAF does not generate Items for the properties that use the [](xref:DevExpress.Persistent.Base.VisibleInDetailViewAttribute) attribute with the parameter value set to `false`.
* If there is a single Property Editor that displays a [collection](xref:113568) property, XAF creates an individual Layout Group.
* If there are several Property Editors that display a [collection](xref:113568) property, XAF creates an individual Tabbed Group.
* If there are Property Editors that display simple properties, such as value type or enumeration properties, XAF creates an individual Layout Group ("SimpleEditors" group). If there are more than four of these Property Editors, XAF creates two Layout Groups in the "Simple Editors" group, and the Property Editors are divided between these groups. These Layout Groups are aligned horizontally, and Editors are placed vertically within them.
* For all remaining Property Editors, XAF creates a "Sizeable Editors" Layout Group.
* For Property Editors that display inherited properties, XAF creates individual groups in the common Layout Groups.
* In a group, Property Editors are sorted first by [IModelCommonMemberViewItem.RowCount](xref:DevExpress.ExpressApp.Model.IModelCommonMemberViewItem.RowCount), then by [IModelNode.Index](xref:DevExpress.ExpressApp.Model.IModelNode.Index), then by business class property declaration order. You can set the `Index` property in code with the [](xref:DevExpress.Persistent.Base.IndexAttribute).

In the following picture, the image on the left illustrates an auto-generated layout for a sample `Contact` business class' Detail View. The image on the right illustrates the auto-generated layout's structure.

![LayoutSideBySide](~/images/layoutsidebyside116218.png)

* The `Contact` class inherits from the `Person` class that has some public properties. XAF creates two nested Layout Groups in the "Simple Editors" Layout Group: "Contact" and "Person".
* The `Contact` class has only four public properties. XAF places the corresponding property editors directly in the "Contact" Layout Group.
* Since the `Person` business class exposes more than four public properties, XAF creates two nested Layout Groups are created: the "Person_col1" and "Person_col2". The Property Editors that display the public properties of the `Person` class are divided between these Layout Groups.
* The string type `Notes` public property belongs to the `Contact` class. However, it has the `Size(-1)` attribute, therefore its Property Editor has a variable height. This condition places the `Notes` Property Editor in the "Sizeable Editors" Layout Group.
* Finally, `Task`, `Change History` and `Phone Numbers` are [collection](xref:113568) properties. XAF creates the "Tabs" Tabbed Group and places each Property Editor in an individual Layout Group.

## Automatically Generated GUID Layout Groups

XAF can generate layout groups automatically when you customize the layout at runtime or design time in the Model Editor. This happens when you add a layout element next to another layout element in a way that breaks the containing layout group's [flow direction](xref:DevExpress.ExpressApp.Model.IModelLayoutGroup.Direction), for example, when you place layout item "A" to the left or right of layout item "B" in a layout group where items are arranged vertically. Since all layout elements within the same group must have the same flow direction, XAF has to create a wrapping layout group with the horizontal flow direction containing the items "A" and "B". This behavior is called wrapping. Auto-generated wrapping groups usually have a random ID with the "Auto" prefix. These groups may not immediately appear in the "Layout Tree View" tab of the layout customization window.

Before rearrangement
:   ![Before layout customization](~/images/layout_before_customization.png)

After rearrangement (with an auto-generated wrapping group)
:   ![After layout customization](~/images/layout_after_customization.png)
