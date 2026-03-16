---
uid: "113329"
seealso: []
title: Property Grid
owner: Ekaterina Kiseleva
---
# Property Grid

The [Model Editor](xref:112582) provides the property grid displayed to the right of the [nodes tree](xref:113328). This topic provides information on the following capabilities and features of this grid.

![ModelEditor](~/images/modeleditor_propertygrid115334.png)

The property grid allows you to customize property values for the focused node. Depending on a property type, you can edit its value in a textbox, select one of the predefined values in a drop-down list or use an [enhanced editor](xref:113330) (invokable in a pop-up window via the ellipsis button). You can also edit property values of several nodes at the same time. Select several nodes in the nodes tree. The property grid will contain their common properties. If you change some values, the changes will be applied to all selected nodes.

## Properties Visualization
The property grid is categorized and you can collapse and expand categories, or switch to alphabetic sorting. A focused property is highlighted. Modified values are displayed in bold. Grid cells have different font colors and styles, so you can easily distinguish between properties of different types. Some of the property types have images assigned for the purpose of better visualization. The following types are available.

| Type | Image | Description |
|---|---|---|
| **Calculated** | &nbsp; | Properties whose values are taken from other property values. For instance, the **PropertyEditorType** property value of the [!include[Node_Views_DetailView_Items_PropertyEditor](~/templates/node_views_detailview_items_propertyeditor111384.md)] node is taken from the same property of the corresponding **BOModel** \| **_\<Class\>_** \| **OwnMembers** \| **_\<Member\>_** node. Calculated property names are displayed in blue and underlined. |
| **Localizable** | ![ME_Localization](~/images/me_localization116738.png)&nbsp; | Properties that can have different values, depending on the current Application Model language aspect. For instance, the Caption properties of all the nodes are localizable. To learn more on how to set localization, refer to the [Localization Basics](xref:112595) topic. |
| **Key** | ![ME_Key](~/images/me_key116755.png) | Key property of the current node. Used to identify nodes. |
| **Read-only** | &nbsp; | Properties that are intended for viewing only. Read-only property names and values are displayed in gray. |
| **Required** | ![ME_Required](~/images/me_required116756.png) | Properties, whose values must be specified. Required property names are displayed in bold and italicized. |

A property can fit several of these types. In this case, the markups are combined. For instance, the **Id** property in the image above is required and is read-only. So, its font is gray, bold and italicized.

## Mini-Toolbar
The mini-toolbar displayed above the property grid provides the following buttons.

| Button | Shortcut | Description |
|---|---|---|
| **Categorized** | - | Switches a grid to a categorized view. |
| **Alphabetic** | - | Switches a grid to an alphabetic view. |
| **Undo&nbsp;Changes** | <kbd>CTRL</kbd>+<kbd>Z</kbd> | Resets the focused property value to its default value. It acts in the same way as the **Reset Differences** command, but it is applied to a single property. |
| **Open&nbsp;Object** | <kbd>ALT</kbd>+<kbd>O</kbd> | Moves the focus to the node associated with a currently selected value. This button is duplicated to the left of each value that represents a node (for instance, the [IModelVariant.View](xref:DevExpress.ExpressApp.ViewVariantsModule.IModelVariant.View) property of the **Variant** node). |
| **Open&nbsp;Source&nbsp;Propety** | <kbd>ALT</kbd>+<kbd>N</kbd> | Moves the focus to the source property of the currently focused calculated value. Alternatively, you can give focus to a calculated property and then click its name to navigate to the source property. |

## Property Values Validation
Required property values are validated. If you create a node, leave its required property value empty and attempt to navigate to another node, the validation warning will be displayed. To resolve an issue, you should either supply the required value or delete the current node if it was created in error.