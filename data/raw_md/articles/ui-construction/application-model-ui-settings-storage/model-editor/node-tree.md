---
uid: "113328"
seealso: []
title: Node Tree
owner: Ekaterina Kiseleva
---
# Node Tree

The [Model Editor](xref:112582) provides a tree list, representing the Application Model structure. You can use this tree to navigate to a certain node and modify the Application Model structure by adding, removing and rearranging nodes.

## Application Model Structure Visualization
Each node has a caption specified by its **Id** property and an associated image. Nodes that are modified in the current model layer have captions displayed in bold. Properties of the currently focused node are displayed in the [property grid](xref:113329) to the right.

![ModelEditor_Tree](~/images/modeleditor_tree116754.png)

## Context Menu Commands
The following context menu is available when right-clicking a node.

![ModelEditor_ContextMenu](~/images/modeleditor_contextmenu115349.png)

Most of the commands available in this menu can be applied not only to a single focused node, but to several selected nodes at once. To select several nodes use the standard approach - hold down <kbd>SHIFT</kbd> and click a node to select sequential nodes, or hold down <kbd>CTRL</kbd> and click a node to select individual nodes. The context menu commands are described in the table below.

| Command | Shortcut | Description |
|---|---|---|
| **Add…** | - | Creates a child of the current node. The command is not available when multiple nodes are selected. |
| **Group** | <kbd><kbd>CTRL</kbd></kbd>+<kbd>G</kbd> | This command enables [grouping](#grouping). |
| **Ungroup** | <kbd>CTRL</kbd>+<kbd>G</kbd> | Disables grouping, specified by the **Group** command. |
| **Go to Source** | <kbd>CTRL</kbd>+<kbd>ENTER</kbd> | Available for child nodes of the **Links** nodes. Navigates to the [linked node](#linked-nodes). |
| **Delete** | <kbd>CTRL</kbd>+<kbd>D</kbd> | Deletes the current node(s). |
| **Show&nbsp;Differences** | - | Shows the XML code that represents the current node(s) differences existing in the current layer and aspect. |
| **Reset&nbsp;Differences** | - | Resets the current node(s) differences. The node will revert to the generated state. |
| **Merge&nbsp;Differences** | - | Available in the Model Editor that is invoked at run time. Merges the current node(s) differences into the underlying model layer. See the [Model Merge Tool](xref:113334) topic for details. |
| **Copy** | <kbd>CTRL</kbd>+<kbd>C</kbd> | Copies the current node(s). |
| **Paste** | <kbd>CTRL</kbd>+<kbd>V</kbd> | Pastes nodes that were previously copied using the **Copy** command as the children of the current node. If the current node already has a child with the same ID, the "_Copy' suffix will be added to the pasted node ID. |
| **Clone** | <kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>C</kbd> | Creates the current node(s) duplicate at the same hierarchy level. The **Id** property of the new node is appended by the "_Copy" suffix and other properties remain intact. |
| **Generate&nbsp;Content** | - | Generates the hierarchical content of the newly created empty **View** node or an existing **View** node that has been customized incorrectly.  The information is generated using the **BOModel** \| **_\<Class\>_** node that corresponds to the **ModelClass** property value of the current node. The command is not available when multiple nodes are selected. |
| **Up** | <kbd>ALT</kbd>+<kbd>UP</kbd> | Moves the current node(s) one position up in the current collection. The indexes (see [IModelNode.Index](xref:DevExpress.ExpressApp.Model.IModelNode.Index)) of collection nodes are automatically modified to correspond to the rearrangement. Multiple selected nodes should be the children of the same parent. |
| **Down** | <kbd>ALT</kbd>+<kbd>DOWN</kbd> | Moves the current node(s) one position down in the current collection. The indexes (see [IModelNode.Index](xref:DevExpress.ExpressApp.Model.IModelNode.Index)) of nodes are automatically modified to correspond to the rearrangement. Multiple selected nodes should be the children of the same parent. |

## Drag-and-Drop Functionality
* You can move a child node from one parent node to another using drag-and-drop. It is convenient to move an Action to another action container, move a navigation item to another group and modify the Detail View layout. The yellow arrow to the left indicates the target node.
	
	![ModelEditor_DragAndDrop_1](~/images/modeleditor_draganddrop_1116703.png)
	
	When dragging, you can place a pointer over the target node and it will be expanded automatically after a small delay. To create a copy of the node instead of moving it, just hold down the <kbd>CTRL</kbd> key when dragging. If the target node already has a child with the same ID, the "_Copy' suffix will be added.
* You can rearrange child items of a certain parent node using drag-and-drop. It is convenient when reordering list view columns or navigation items. Hold down the SHIFT key and drag a child node up or down the list within the bounds of its parent node. The blue arrow to the left indicates the node's new position.
	
	![ModelEditor_DragAndDrop_2](~/images/modeleditor_draganddrop_2116704.png)
	
	The indexes of child nodes will be automatically modified to correspond to the rearrangement.

You can select multiple nodes and drag-and-drop several nodes at once.

## Linked Nodes

Certain nodes have a "virtual" child node named **Links**. It is hidden by default; you can toggle its visibility using the **Show Links / Hide Links** [toolbar command](xref:113327). Under this node, you can see nodes that contain references to the current node. The screenshot below illustrates the **Department** node of the [](xref:DevExpress.ExpressApp.Model.IModelClass) type. Within the **Links** node, you can see the **Creatable Item** for the Department object, **Members** of the Department type and **Views** designed for the Department type.

![ModelEditor_LinksNode](~/images/modeleditor_linksnode116859.png)

You can edit properties of linked nodes in place, or navigate to an actual node location using the **Go to Source** command.

## Grouping
Use the **Group/Ungroup** context menu command to enable/disable grouping. The screenshot below illustrates the grouped **Views** node.

![ModelEditor_GroupUngroup](~/images/modeleditor_groupungroup116860.png)

Views that do not depend on a certain business class (e.g., DashboardView) fall into the **Unspecified** node.

![ModelEditor_Unspecified](~/images/modeleditor_unspecified117698.png)

By default, grouping is supported for the child nodes of **Views**, **BOModel**, **Controllers** and **Actions**. To customize default grouping, or implement grouping rules for other nodes, use the [](xref:DevExpress.ExpressApp.ModelEditor.ModelEditorGroupingHelper) class.
