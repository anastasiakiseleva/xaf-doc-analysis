---
uid: DevExpress.ExpressApp.Actions.ActionBase.SelectionDependencyType
name: SelectionDependencyType
type: Property
summary: Specifies a context for enabling an [Action](xref:112622).
syntax:
  content: |-
    [DefaultValue(SelectionDependencyType.Independent)]
    public SelectionDependencyType SelectionDependencyType { get; set; }
  parameters: []
  return:
    type: DevExpress.ExpressApp.Actions.SelectionDependencyType
    description: A [](xref:DevExpress.ExpressApp.Actions.SelectionDependencyType) enumeration value identifying a context type.
seealso:
- linkId: "113103"
---
Use this property to make the current Action dependent on whether a single object or multiple objects are selected in the current [View](xref:112611). 

> [!NOTE]
> The Action is hidden if the selection context is not available (for example, when the Controller is not derived from [](xref:DevExpress.ExpressApp.ViewController)).

You can set another value in the Controller's constructor. This value is saved to the [Application Model](xref:112580)'s [!include[Node_Action](~/templates/node_action111373.md)] node. You can change this value in the [Model Editor](xref:112830). In a UI, the value which is specified in the Application Model's .xafml file that was loaded last, will be displayed. For information on the order of Application Model differences loading, refer to the [Application Model Basics](xref:112580) topic.