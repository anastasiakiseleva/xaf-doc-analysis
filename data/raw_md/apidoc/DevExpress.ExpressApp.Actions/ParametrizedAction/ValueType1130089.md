---
uid: DevExpress.ExpressApp.Actions.ParametrizedAction.ValueType
name: ValueType
type: Property
summary: Specifies the type of values that must be entered in a Parametrized Action's editor.
syntax:
  content: |-
    [DefaultValue(typeof(string))]
    public Type ValueType { get; set; }
  parameters: []
  return:
    type: System.Type
    description: A [](xref:System.Type) value that indicates the type of the current Parametrized Action's [ParametrizedAction.Value](xref:DevExpress.ExpressApp.Actions.ParametrizedAction.Value).
seealso: []
---
A Parametrized Action is displayed via an editor whose type depends on the type of values that will be entered in it. Use this property to specify the values type. The following types are supported:

* string
* int
* float
* double
* DateTime

Built-in [Action Containers](xref:112610) will display an appropriate editor for each of them.