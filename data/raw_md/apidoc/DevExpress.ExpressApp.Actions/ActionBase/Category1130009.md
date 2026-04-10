---
uid: DevExpress.ExpressApp.Actions.ActionBase.Category
name: Category
type: Property
summary: Specifies an [Action](xref:112622)'s category.
syntax:
  content: |-
    [DefaultValue("Unspecified")]
    public string Category { get; set; }
  parameters: []
  return:
    type: System.String
    description: A String value that represents a Category for the current Action.
seealso:
- linkId: 400495#add-an-action-to-a-controller
  altText: Add an Action to a Controller
---
Use the Action's `Category` property to specify the [Action Container](xref:112610) where XAF displays the current Action. You can specify a predefined category that corresponds to an Action Container used by built-in [Templates](xref:112609). These categories are available in the `DevExpress.Persistent.Base.PredefinedCategory` enumeration.

[!include[](~/templates/add-action.md)]

The `Category` property is set to `DevExpress.Persistent.Base.PredefinedCategory.Unspecified` (the default setting). You can specify a different value in the Controller's constructor. XAF saves this value to the [Application Model](xref:112580)'s [!include[Node_Action](~/templates/node_action111373.md)] node. You can change this value in the [Model Editor](xref:112830) (see [](xref:402145) and [How to: Reorder an Action Container's Actions Collection](xref:112815)).

In the UI, XAF displays the value specified in the Application Model's .xafml file that was loaded last. For more information about the load order of Application Model differences, refer to the following topic: [Application Model Basics](xref:112580).

If the `Category` property is set to `Unspecified`, XAF displays the Action in the current [Template](xref:112609)'s `DefaultContainer`.

> [!NOTE]
> A Template may return _null_ for this property. We recommend that you explicitly assign the required category to the Action's `Category` property. 

### How to Add an Action to a Context Menu or Command Column

You can use Action Containers that appear in Context Menus only. If you want to show an Action only in a Context Menu (in ASP.NET Core Blazor and Windows Forms), specify the `Menu` category.

For instructions on how to display an Action in a List View grid, refer to the following topic: [](xref:404559).

To see where a certain Action Container is located, [add a custom template](xref:112696) to your application and open it in the **Designer**.

The layout of Action Containers in an XAF ASP.NET Core Blazor UI is described in the following topic: [](xref:112610).

List View context menus generally do not display Actions mapped to the `Unspecified` category. These Actions only appear in Windows Forms applications that use the `TabbedMDI` or `StandardMDI` @DevExpress.ExpressApp.UIType.

To see how Actions are mapped to Action Containers in your application, open the **ActionDesign** | **ActionToContainerMapping** node in the [Model Editor](xref:112830).
