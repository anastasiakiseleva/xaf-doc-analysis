---
uid: DevExpress.ExpressApp.Editors.ListEditor.ContextMenuTemplate
name: ContextMenuTemplate
type: Property
summary: Provides access to a [List Editor](xref:113189)'s Context Menu Template.
syntax:
  content: public virtual IContextMenuTemplate ContextMenuTemplate { get; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Templates.IContextMenuTemplate
    description: A control that implements the `IContextMenuTemplate` interface and represents a List Editor's Context Menu Template.
seealso:
- linkId: "112618"
---
A List Editor can show a context menu that contains a set of [Actions](xref:112622):

![ContextMenuTemplate](~/images/contextmenutemplate116134.png)

The context menu can be represented by any control. However, it must implement the `IContextMenuTemplate` interface to display Actions. This interface includes the following members:

* The `IContextMenuTemplate.CreateActionItems` method.
    
    This method receives a list of [Action Containers](xref:112610) as a parameter. Each Action Container creates controls for Actions that are mapped to it in the [Application Model](xref:112580)'s **ActionDesign** | **ActionToContainerMapping** node.

* The `IContextMenuTemplate.BoundItemCreating` event.
    
    The event is raised when XAF creates an Action in an Action Container. `ActionsCriteriaViewController` uses the event to determine the Action's availability in the current context. 
    If the Action's availability conditions are satisfied, `ActionsCriteriaViewController` sets the event argument's `BoundItemCreatingEventArgs.Enabled` property to `true`.

In the List Editor's constructor, create a control that implements the `IContextMenuTemplate` interface and assign this control to the `ContextMenuTemplate` property.

The list of the Action Containers to be added to the List Editor's Context Menu Template is specified by the [Template](xref:112609) of the active [Window or Frame](xref:112608).

To change the Context Menu Template's list of Action Containers, modify the corresponding Template.

For example, the following code snippet demonstrates a part of the _MainForm.Designer.cs_ file. The following lines specify Action Containers for Context Menu Templates:

# [C#](#tab/tabid-csharp)

```csharp
this.actionsContainersManager.ContextMenuContainers.Add(this.cObjectsCreation);
this.actionsContainersManager.ContextMenuContainers.Add(this.cSave);
this.actionsContainersManager.ContextMenuContainers.Add(this.cEdit);
this.actionsContainersManager.ContextMenuContainers.Add(this.cRecordEdit);
this.actionsContainersManager.ContextMenuContainers.Add(this.cOpenObject);
this.actionsContainersManager.ContextMenuContainers.Add(this.cUndoRedo);
this.actionsContainersManager.ContextMenuContainers.Add(this.cPrint);
this.actionsContainersManager.ContextMenuContainers.Add(this.cView);
this.actionsContainersManager.ContextMenuContainers.Add(this.cReports);
this.actionsContainersManager.ContextMenuContainers.Add(this.cExport);
this.actionsContainersManager.ContextMenuContainers.Add(this.cMenu);
```

***

There are two ways to assign an Action to an Action Container:

* Use an Action's [ActionBase.Category](xref:DevExpress.ExpressApp.Actions.ActionBase.Category) property. This property specifies the Action Container where the Action is assigned:
    
    ![ActionBase.Category](~/images/actionbase.category116125.png)
    
    If this property is not set, the Action is assigned to the Action Container used by default in a Template. Different Templates may have different default Action Containers. Depending on the current Template, the Action may be displayed in different Action Containers.
* Use the [Model Editor](xref:112582). Each child node of the **ActionToContainerMapping** node corresponds to an Action Container and contains a list of assigned Actions (their `Category` property specifies the Action Container's name):
    
    ![ActionToContainerMapping.ActionId](~/images/actiontocontainermapping.actionid116126.png)

The following table lists XAF's built-in Context Menu Templates:

| Platform | Name | List Editor | Description
|---|---|---|---|
| ASP.NET Core Blazor | `ListEditorContextMenuTemplate` | @DevExpress.ExpressApp.Blazor.Editors.DxGridListEditor | Allows you to customize inline Actions with the help of the `IContextMenuTemplate.BoundItemCreating` event.
| Windows Forms | `ActionsDXPopupMenu` | Built-in Windows Forms List Editors | Creates a pop-up menu with an item for each Action. |

When you inherit from the [](xref:DevExpress.ExpressApp.Editors.ListEditor) class, override the `ContextMenuTemplate` property to obtain the required Context Menu Template. For an example, refer to the following topic: [How to: Support a Context Menu for a Custom Windows Forms List Editor](xref:112660).