---
uid: DevExpress.ExpressApp.Actions.ActionBase.ActionMeaning
name: ActionMeaning
type: Property
summary: Specifies whether an Action is represented by an accept, cancel or ordinal button in a Window Forms application's pop-up Windows.
syntax:
  content: |-
    [DefaultValue(ActionMeaning.Unknown)]
    public ActionMeaning ActionMeaning { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.ActionMeaning
    description: An [](xref:DevExpress.ExpressApp.Actions.ActionMeaning) enumeration value.
seealso: []
---
This property is considered for Actions that are displayed in pop-up [Windows](xref:112608) in Windows Forms applications. The following values are available:

* **ActionMeaning.Accept**
    
    The Action is executed when an end-user presses ENTER.
* **ActionMeaning.Cancel**
    
    The Action is executed when an end-user presses ESC.
* **ActionMeaning.Unknown**
    
    The Action is executed when an end-user clicks it or uses a predefined shortcut.

You can add an Action to a pop-up Window. For this purpose, set its [ActionBase.Category](xref:DevExpress.ExpressApp.Actions.ActionBase.Category) property to the "ObjectsCreation" or "PopupActions"
value. This, means that the Action will be mapped to the ObjectsCreation or PopupActions [Action Container](xref:112610). So, the Action will be displayed in pop-up Windows which are represented by the **LookupControlTemplate** or **PopupForm** [Template](xref:112609), because the former contains both these Action Containers and the former - the "PopupActions" Action Container.

You can process the **ActionMeaning** property in a custom Action Container. In this instance, do not forget to add this Container to a built-in Template or a custom one (see [How to: Create a Custom WinForms Ribbon Template](xref:112618)).